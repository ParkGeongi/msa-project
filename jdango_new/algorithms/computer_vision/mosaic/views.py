import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt


from PIL import Image

from algorithms.common import Common
from algorithms.computer_vision.mosaic.models import Canny, HoughLines, Haar, Mosaic, Mosaic_People, Gray, Origin
from algorithms.dataclass import Dataset
from algorithms.lambas import Mosaic_Lambdas


class MenuController(object):

    def __init__(self):
        pass

    def __str__(self):
        return f""

    @staticmethod
    def Menu_1_Origin(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(Mosaic_Lambdas('Memory_Img_Read', params[1]))
        plt.imshow(Mosaic_Lambdas('Image_From_Array', img))
        plt.show()
        print(f' cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
        print(f' Shape is {img.shape}')


    @staticmethod
    def Menu_2_Gray(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(Mosaic_Lambdas('Memory_Img_Read', params[1]))
        img = Mosaic_Lambdas('Gray',img)
        plt.imshow(Mosaic_Lambdas('Image_From_Array',img))
        plt.show()

    @staticmethod
    def Menu_3_CannyDisk(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(Mosaic_Lambdas('Disk_Img_Read',params[1]))
        (lambda x: plt.imshow(x))(Canny(img))
        plt.show()

    @staticmethod
    def Menu_4_CannyMemory(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(Mosaic_Lambdas('Memory_Img_Read', params[1]))
        (lambda x : plt.imshow(Image.fromarray(x)))(Canny(img))
        plt.show()

    @staticmethod
    def Menu_5_Hough(*params):
        print(f" ### {params[0]} ### ")
        img = np.array(Mosaic_Lambdas('Memory_Img_Read', params[1]))
        edges =  cv.Canny(img, 100, 200) # img, threshold 1, 2 \
        dst = HoughLines(edges)
        plt.subplot(121), plt.imshow(edges, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_6_Haar(*params):
        print(f" ### {params[0]} ### ")
        haar = cv.CascadeClassifier(params[1])
        girl = params[2]
        # bgr -> rgb
        img1 = Mosaic_Lambdas('Disk_Img_Read',girl)
        girl,rect = Haar(img1, haar)
        plt.subplot(111), plt.imshow(girl)
        plt.title('Haar Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_7_Mosaic_Cat(*params):
        print(f" ### {params[0]} ### ")
        cat = cv.imread(f'{Dataset().context}{params[1]}')
        mos = Mosaic(cat,(150,150,450,450), 10)
        cv.imwrite(f'{Dataset().context}cat-mosaic.png',mos)
        plt.subplot(111), plt.imshow(mos)
        plt.title('Mosaic Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_8_Mosaic_Girl(*params):
        print(f" ### {params[0]} ### ")
        haar = cv.CascadeClassifier(params[1])
        girl = params[2]
        img = cv.cvtColor(Mosaic_Lambdas('Disk_Img_Read', girl), cv.COLOR_BGR2RGB)
        img1 = img.copy()
        girl,rect = Haar(img, haar)
        mos = Mosaic(img1,rect, 10)
        cv.imwrite(f'{Dataset().context}girl-mosaic.png', mos)
        plt.subplot(111), plt.imshow(mos)
        plt.title('Mosaic Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_9_Mosaic_Two(*params):
        print(f" ### {params[0]} ### ")
        haar = params[1]
        girl = params[2]

        img = cv.cvtColor(Mosaic_Lambdas('Disk_Img_Read', girl), cv.COLOR_BGR2RGB)

        mos =Mosaic_People(img,10, haar)
        plt.subplot(111), plt.imshow(mos)
        plt.title('Mosaic Image'), plt.xticks([]), plt.yticks([])
        plt.show()


    @staticmethod
    def Menu_10_All_View(*params):

        print(f" ### {params[0]} ### ")
        haar = params[1]
        img = params[2]
        img_people = params[3]


        img1 = cv.cvtColor(Origin(Mosaic_Lambdas('Disk_Img_Read',img)), cv.COLOR_BGR2RGB) # bgr -> rgb

        img_copy = img1.copy()
        img2 = Gray(np.array(Mosaic_Lambdas('Disk_Img_Read',img)))

        img3 =Canny(np.array(Mosaic_Lambdas('Disk_Img_Read',img)))

        img4 = HoughLines(img3)

        img5,rect = Haar(img1, cv.CascadeClassifier(haar))

        mos = Mosaic_People(img_copy,10,haar) #img, size, haar경로

        #mos_two = Mosaic_People(Mosaic_People(cv.cvtColor(Mosaic_Lambdas('Disk_Img_Read', img_people), cv.COLOR_BGR2RGB), 10, haar),10,haar)# harr경로를 받아서 servise에서 처리함

        img_people = cv.cvtColor(Mosaic_Lambdas('Disk_Img_Read', img_people), cv.COLOR_BGR2RGB)
        mos_img = Mosaic_People(Mosaic_People(img_people, 10, haar),10,haar)




        plt.subplot(331), plt.imshow(img_copy)
        plt.title('Original '), plt.xticks([]), plt.yticks([])
        plt.subplot(332), plt.imshow(img2, cmap='gray')
        plt.title('Gray '), plt.xticks([]), plt.yticks([])
        plt.subplot(333), plt.imshow(img3, cmap='gray')
        plt.title('Canny '), plt.xticks([]), plt.yticks([])
        plt.subplot(334), plt.imshow(img4)
        plt.title('Hough '), plt.xticks([]), plt.yticks([])
        plt.subplot(335), plt.imshow(img5)
        plt.title('Haar '), plt.xticks([]), plt.yticks([])
        plt.subplot(336), plt.imshow(mos)
        plt.title('Mosaic '), plt.xticks([]), plt.yticks([])
        plt.subplot(337), plt.imshow(mos_img)
        plt.title('Mosaic '), plt.xticks([]), plt.yticks([])
        plt.show()
        #girl = cv.cvtColor(img1, cv.COLOR_RGB2BGR)
        #girl = cv.resize(girl, (300, 300))
        #cv.imwrite('girl_facing.png',girl)
        #cv.imshow('GIRL FACE',girl)
        #cv.waitKey(0)
        #cv.destroyWindow()


if __name__ == '__main__':

    '''
    이미지 읽기의 flag는 3가지가 있습니다.
    cv2.IMREAD_COLOR : 이미지 파일을 Color로 읽어들입니다.
                        투명한 부분은 무시되며, Default값입니다.
    cv2.IMREAD_GRAYSCALE : 이미지를 Grayscale로 읽어 들입니다.
                            실제 이미지 처리시 중간단계로 많이 사용합니다.
    cv2.IMREAD_UNCHANGED : 이미지파일을 alpha channel까지 포함하여 읽어 들입니다
    3개의 flag대신에 1, 0, -1을 사용해도 됩니다
    Shape is (512, 512, 3)
    Y축: 512 (앞)
    X축: 512 (뒤)
    3은 RGB 로 되어 있다.
    cv2.waitKey(0) : keyboard입력을 대기하는 함수로
                    0이면 key입력까지 무한대기이며, 특정 시간동안 대기하려면
                    milisecond값을 넣어주면 됩니다.
    cv2.destroyAllWindows() 화면에 나타난 윈도우를 종료합니다.
                            일반적으로 위 3개는 같이 사용됩니다.
    '''

    ds = Dataset()
    api = MenuController()
    URL = "https://docs.opencv.org/4.x/roi.jpg"
    IMG = "Lenna.png"
    BUILDING = 'https://www.charlezz.com/wordpress/wp-content/uploads/2021/06/www.charlezz.com-opencv-building.jpg'
    HAAR = "./data/haarcascade_frontalface_alt.xml"
    GIRL = "girl.jpg"
    GIRL_INCLINED = "girl_inclined.png"
    GIRL_WITH_MOM = "girl_with_mom.jpg"
    PEOPLE = "1.jpg"
    GIRL_SIDE_FACE = "girl_side_face.jpg"
    FACE_TARGET = ""
    FACE_OBJECT = ""
    CAT = "cat.jpg"

    if __name__ == '__main__':
        menus = ["종료", "원본보기", "그레이 스케일", "엣지 검출 disk", "엣지 검출 memory", "직선 검출", "얼굴 인식", "고양이 모자이크", "소녀 모자이크",
                 "모녀 모자이크", "전체보기"]

        while True:

            menu = Common.menu(menus)
            if menu == "0":
                print(f" ### {menus[0]} ### ")
                break
            elif menu == "1":
                api.Menu_1_Origin(menus[1], URL)
            elif menu == "2":
                api.Menu_2_Gray(menus[2], URL)
            elif menu == "3":
                api.Menu_3_CannyDisk(menus[3], IMG)
            elif menu == '4':
                api.Menu_4_CannyMemory(menus[4], URL)
            elif menu == '5':
                api.Menu_5_Hough(menus[5], BUILDING)
            elif menu == '6':
                api.Menu_6_Haar(menus[6], HAAR, PEOPLE)
            elif menu == '7':
                api.Menu_7_Mosaic_Cat(menus[7], CAT)
            elif menu == '8':
                api.Menu_8_Mosaic_Girl(menus[8], HAAR, GIRL)
            elif menu == '9':
                api.Menu_9_Mosaic_Two(menus[9], HAAR, PEOPLE)
            elif menu == '10':
                api.Menu_10_All_View(menus[10], HAAR, GIRL, GIRL_WITH_MOM)

            else:
                print(" ### 해당 메뉴 없음 ### ")

