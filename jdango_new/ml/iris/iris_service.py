import numpy as np
from sklearn import datasets
from keras.models import load_model

from paths.path import dir_path


class IrisService(object):

    def __init__(self):
        global model , graph, target_names
        model = load_model(dir_path('iris')+r'\save\iris_model.h5')
        #model = load_model(os.path.join(os.path.abspath("save"), "iris_model.h5"))
        target_names = datasets.load_iris().target_names


    def service_model(self, features):

        features = np.reshape(features,(1,4))
        Y_prob = model.predict(features, verbose=0)
        predicted = Y_prob.argmax(axis=-1) # p-vla 가장 높은 것

        return predicted[0] # 타입 :  <class 'numpy.int64'>


'''
 --- 1.Shape ---
(150, 6)
 --- 2.Features ---
Index(['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm',
       'Species'],
'''
iris_menu = ["Exit", #0
                "hook",#1
             ]
iris_lambda = {
    "1" : lambda x: x.service_model([5.1,3.5,1.4,0.1])

}
if __name__ == '__main__':
    iris = IrisService()


    while True:
        [print(f"{i}. {j}") for i, j in enumerate(iris_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                iris_lambda[menu](iris)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")
