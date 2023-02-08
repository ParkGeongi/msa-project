import numpy as np
from keras.models import load_model
import tensorflow as tf

from paths.path import dir_path


class NumberService(object):

    def __init__(self):
        pass


    def service_model(self,i):

        model = load_model(dir_path('number')+'\\save\\number_model.h5')
        (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

        predictions = model.predict(test_images)
        predictions_array, true_label, img = predictions[i], test_labels[i], test_images[i]
        predicted_label = np.argmax(predictions_array)
        print(f'#############//True label {true_label}//################')

        if predicted_label == 0:
            resp = '영'
        elif predicted_label == 1:
            resp = '일'
        elif predicted_label == 2:
            resp = '이'
        elif predicted_label == 3:
            resp = '삼'
        elif predicted_label == 4:
            resp = '사'
        elif predicted_label == 5:
            resp = '오'
        elif predicted_label == 6:
            resp = '육'
        elif predicted_label == 7:
            resp = '칠'
        elif predicted_label == 8:
            resp = '팔'
        elif predicted_label == 9:
            resp = '구'
        elif predicted_label == 10:
            resp = '십'
        return resp
number_menu = ["Exit", #0
                "hook",#1
             ]
number_lambda = {
    "1" : lambda x: x.service_model(),
}

if __name__ == '__main__':
    number= NumberService()


    while True:
        [print(f"{i}. {j}") for i, j in enumerate(number_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                number_lambda[menu](number)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")