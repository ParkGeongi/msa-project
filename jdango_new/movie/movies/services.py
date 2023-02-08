from __future__ import print_function
import random

import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import sys
import dlib     #conda install -c conda-forge dlib
import cv2
import openface

'''
Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks
Alec Radford, Luke Metz, Soumith Chintala
In recent years, supervised learning with convolutional networks (CNNs) has seen huge adoption in computer vision applications. 
Comparatively, unsupervised learning with CNNs has received less attention. 
In this work we hope to help bridge the gap between the success of CNNs for supervised learning and unsupervised learning. 
We introduce a class of CNNs called deep convolutional generative adversarial networks (DCGANs),
that have certain architectural constraints, and demonstrate that they are a strong candidate for unsupervised learning. 
Training on various image datasets, we show convincing evidence 
that our deep convolutional adversarial pair learns a hierarchy of representations from object parts to scenes in both the generator and discriminator. 
Additionally, we use the learned features for novel tasks - demonstrating their applicability as general image representations.
'''
class DcGan(nn.Module):

    def __init__(self):
        self.dataroot = './data'
        self.workers = 2
        self.batch_size = 128
        self.image_size = 64
        self.nc = 3
        self.nz = 100
        self.ngf = 64
        self.ndf = 64
        self.num_epochs = 2
        self.lr = 0.0002
        self.beta1 = 0.5
        self.ngpu = 1
        self.device = torch.device("cuda:0" if (torch.cuda.is_available() and self.ngpu > 0) else "cpu")
        self.dataset =None
        self.dataloader = None

    def hook(self):
        self.show_face()
        self.print_netG()
        self.print_netD()
        self.fake_imgs()

    def seed(self):
        manualSeed = 999
        # manualSeed = random.randint(1, 10000) # use if you want new results
        print("Random Seed: ", manualSeed)
        random.seed(manualSeed)
        torch.manual_seed(manualSeed)

    def show_face(self):

        self.dataset = dset.ImageFolder(root=self.dataroot,
                                        transform=transforms.Compose([
                                       transforms.Resize(self.image_size),
                                       transforms.CenterCrop(self.image_size),
                                       transforms.ToTensor(),
                                       transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                                   ]))
        # Create the dataloader
        self.dataloader = torch.utils.data.DataLoader(self.dataset, batch_size=self.batch_size,
                                                 shuffle=True, num_workers=self.workers)

        # Decide which device we want to run on
        device = self.device

        # Plot some training images
        real_batch = next(iter(self.dataloader))
        plt.figure(figsize=(8, 8))
        plt.axis("off")
        plt.title("Training Images")
        plt.imshow(
            np.transpose(vutils.make_grid(real_batch[0].to(device)[:64], padding=2, normalize=True).cpu(), (1, 2, 0)))
        plt.show()

        # custom weights initialization called on netG and netD
    def weights_init(self, m):
        classname = m.__class__.__name__
        if classname.find('Conv') != -1:
            nn.init.normal_(m.weight.data, 0.0, 0.02)
        elif classname.find('BatchNorm') != -1:
            nn.init.normal_(m.weight.data, 1.0, 0.02)
            nn.init.constant_(m.bias.data, 0)

    def print_netG(self):
        ngpu = self.ngpu
        device = self.device
        netG = Generator(ngpu).to(device)
        # Handle multi-gpu if desired
        if (device.type == 'cuda') and (ngpu > 1):
            netG = nn.DataParallel(netG, list(range(ngpu)))

        # Apply the weights_init function to randomly initialize all weights
        #  to mean=0, stdev=0.02.
        netG.apply(self.weights_init)

        # Print the model
        print(netG)

    def print_netD(self):
        ngpu = self.ngpu
        device = self.device

        netD = Discriminator(ngpu).to(device)


        # Handle multi-gpu if desired
        if (device.type == 'cuda') and (ngpu > 1):
            netD = nn.DataParallel(netD, list(range(ngpu)))

        # Apply the weights_init function to randomly initialize all weights
        #  to mean=0, stdev=0.2.
        netD.apply(self.weights_init)
        # Print the model
        print(netD)

    def fake_faces(self):

        num_epochs = self.num_epochs
        nz = self.nz
        lr = self.lr
        beta1 =self.beta1

        ngpu = self.ngpu
        device = self.device

        dataset = dset.ImageFolder(root=self.dataroot,
                                        transform=transforms.Compose([
                                            transforms.Resize(self.image_size),
                                            transforms.CenterCrop(self.image_size),
                                            transforms.ToTensor(),
                                            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                                        ]))
        # Create the dataloader
        dataloader = torch.utils.data.DataLoader(dataset, batch_size=self.batch_size,
                                                      shuffle=True, num_workers=self.workers,
                                                 multiprocessing_context='spawn')



        netG = Generator(ngpu).to(device)
        # Handle multi-gpu if desired
        if (device.type == 'cuda') and (ngpu > 1):
            netG = nn.DataParallel(netG, list(range(ngpu)))

        # Apply the weights_init function to randomly initialize all weights
        #  to mean=0, stdev=0.02.
        netG.apply(self.weights_init)

        netD = Discriminator(ngpu).to(device)

        # Handle multi-gpu if desired
        if (device.type == 'cuda') and (ngpu > 1):
            netD = nn.DataParallel(netD, list(range(ngpu)))

        # Apply the weights_init function to randomly initialize all weights
        #  to mean=0, stdev=0.2.
        netD.apply(self.weights_init)


        # Initialize BCELoss function
        criterion = nn.BCELoss()

        # Create batch of latent vectors that we will use to visualize
        #  the progression of the generator
        fixed_noise = torch.randn(64, nz, 1, 1, device=device)

        # Establish convention for real and fake labels during training
        real_label = 1.
        fake_label = 0.

        # Setup Adam optimizers for both G and D
        optimizerD = optim.Adam(netD.parameters(), lr=lr, betas=(beta1, 0.999))
        optimizerG = optim.Adam(netG.parameters(), lr=lr, betas=(beta1, 0.999))
        # Training Loop



        # Lists to keep track of progress
        img_list = []
        G_losses = []
        D_losses = []
        iters = 0

        print("Starting Training Loop...")
        # For each epoch
        for epoch in range(num_epochs):
            # For each batch in the dataloader
            for i, data in enumerate(tqdm(dataloader)):

                ############################
                # (1) Update D network: maximize log(D(x)) + log(1 - D(G(z)))
                ###########################
                ## Train with all-real batch
                netD.zero_grad()
                # Format batch
                real_cpu = data[0].to(device)
                b_size = real_cpu.size(0)
                label = torch.full((b_size,), real_label, dtype=torch.float, device=device)
                # Forward pass real batch through D
                output = netD(real_cpu).view(-1)
                # Calculate loss on all-real batch
                errD_real = criterion(output, label)
                # Calculate gradients for D in backward pass
                errD_real.backward()
                D_x = output.mean().item()

                ## Train with all-fake batch
                # Generate batch of latent vectors
                noise = torch.randn(b_size, nz, 1, 1, device=device)
                # Generate fake image batch with G
                fake = netG(noise)
                label.fill_(fake_label)
                # Classify all fake batch with D
                output = netD(fake.detach()).view(-1)
                # Calculate D's loss on the all-fake batch
                errD_fake = criterion(output, label)
                # Calculate the gradients for this batch, accumulated (summed) with previous gradients
                errD_fake.backward()
                D_G_z1 = output.mean().item()
                # Compute error of D as sum over the fake and the real batches
                errD = errD_real + errD_fake
                # Update D
                optimizerD.step()

                ############################
                # (2) Update G network: maximize log(D(G(z)))
                ###########################
                netG.zero_grad()
                label.fill_(real_label)  # fake labels are real for generator cost
                # Since we just updated D, perform another forward pass of all-fake batch through D
                output = netD(fake).view(-1)
                # Calculate G's loss based on this output
                errG = criterion(output, label)
                # Calculate gradients for G
                errG.backward()
                D_G_z2 = output.mean().item()
                # Update G
                optimizerG.step()
                # Check how the generator is doing by saving G's output on fixed_noise
                if (iters % 500 == 0) or ((epoch == num_epochs - 1) and (i == len(dataloader) - 1)):
                    with torch.no_grad():
                        fake = netG(fixed_noise).detach().cpu()
                    img_list.append(vutils.make_grid(fake, padding=2, normalize=True))

                iters += 1
            # Output training stats
            print('[%d/%d]\tLoss_D: %.4f\tLoss_G: %.4f\tD(x): %.4f\tD(G(z)): %.4f / %.4f'
                  % (epoch, num_epochs, errD.item(), errG.item(), D_x, D_G_z1, D_G_z2))

            # Save Losses for plotting later
            G_losses.append(errG.item())
            D_losses.append(errD.item())
        # Grab a batch of real images from the dataloader
        real_batch = next(iter(dataloader))

        # Plot the real images
        plt.figure(figsize=(15, 15))
        plt.subplot(1, 2, 1)
        plt.axis("off")
        plt.title("Real Images")
        plt.imshow(
            np.transpose(vutils.make_grid(real_batch[0].to(device)[:64], padding=5, normalize=True).cpu(), (1, 2, 0)))

        # Plot the fake images from the last epoch
        plt.subplot(1, 2, 2)
        plt.axis("off")
        plt.title("Fake Images")
        plt.imshow(np.transpose(img_list[-1], (1, 2, 0)))
        plt.show()
    def MyDlib(self):
        t = MyDlib()
        t.hook()



class MyDlib(object):
    def __init__(self):
        pass

    def hook(self):

        predictor_model = "./files/shape_predictor_68_face_landmarks.dat"

        # HOG 이용한 얼굴 감지 클래스 생성 - dlib
        face_detector = dlib.get_frontal_face_detector()

        face_pose_predictor = dlib.shape_predictor(predictor_model)

        face_aligner = openface.AlignDlib(predictor_model)

        image = cv2.imread('./data/lenna.jpg')

        detected_faces = face_detector(image, 1)

        # 찾은 얼굴 개수 만큼 반복한다.
        for i, face_rect in enumerate(detected_faces):

            print(
                "- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(),
                                                                                   face_rect.top(),
                                                                                   face_rect.right(),
                                                                                   face_rect.bottom()))

            # 얼굴 위치에서 랜드마크 찾기
            pose_landmarks = face_pose_predictor(image, face_rect)

            alignedFace = face_aligner.align(532, image, face_rect,
                                             landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

            # aligned_face_x.jpg 로 저장
            cv2.imwrite("./data/aligned_face_{}.jpg".format(i), alignedFace)

    # Generator Code
class Generator(nn.Module):
    def __init__(self, ngpu):
        super(Generator, self).__init__()
        that = DcGan()
        nz = that.nz
        ngf = that.ngf
        nc = that.nc
        self.ngpu = ngpu
        self.main = nn.Sequential(
            # input is Z, going into a convolution
            nn.ConvTranspose2d(nz, ngf * 8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(ngf * 8),
            nn.ReLU(True),
            # state size. (ngf*8) x 4 x 4
            nn.ConvTranspose2d(ngf * 8, ngf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 4),
            nn.ReLU(True),
            # state size. (ngf*4) x 8 x 8
            nn.ConvTranspose2d(ngf * 4, ngf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 2),
            nn.ReLU(True),
            # state size. (ngf*2) x 16 x 16
            nn.ConvTranspose2d(ngf * 2, ngf, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(True),
            # state size. (ngf) x 32 x 32
            nn.ConvTranspose2d(ngf, nc, 4, 2, 1, bias=False),
            nn.Tanh()
            # state size. (nc) x 64 x 64
        )

    def forward(self, input):
        return self.main(input)


class Discriminator(nn.Module):
    def __init__(self, ngpu):
        that = DcGan()
        nc = that.nc
        ndf = that.ndf

        super(Discriminator, self).__init__()
        self.ngpu = ngpu
        self.main = nn.Sequential(
            # input is (nc) x 64 x 64
            nn.Conv2d(nc, ndf, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. (ndf) x 32 x 32
            nn.Conv2d(ndf, ndf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 2),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. (ndf*2) x 16 x 16
            nn.Conv2d(ndf * 2, ndf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 4),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. (ndf*4) x 8 x 8
            nn.Conv2d(ndf * 4, ndf * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 8),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. (ndf*8) x 4 x 4
            nn.Conv2d(ndf * 8, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()
        )

    def forward(self, input):
        return self.main(input)

GAN_MENUS = ["종료",  # 0
             '/movie/movies/fake-faces',  # 1
            '/movie/movies/faces-blow-up', #2


             ]

gan_menu = {
    "1": lambda t: t.hook(),
    "2": lambda t: t.MyDlib(),
    "3": lambda t: print(" ** No Function ** "),
    "4": lambda t: print(" ** No Function ** "),
    "5": lambda t: print(" ** No Function ** "),
    "6": lambda t: print(" ** No Function ** "),
    "7": lambda t: print(" ** No Function ** "),
    "8": lambda t: print(" ** No Function ** "),

}


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')


if __name__ == '__main__':
    while True:
        t = DcGan()
        menu = my_menu(GAN_MENUS)
        if menu == '0':
            print('종료')
            break
        else:
            gan_menu[menu](t)
