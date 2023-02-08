from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
from keras.layers import Dense
from keras import Sequential

from paths.path import dir_path


class IrisModel(object):

    def __init__(self):
        self.iris = datasets.load_iris() # <'sklearn.utils.Bunch'>

        self._X = self.iris.data # _ getter / setter 내장된 값이라는 의미 프라이빗
        self._Y = self.iris.target


    def hook(self):
        self.spec()
        #self.create_model()


    def spec(self):

        print(" --- 1.Features ---")
        print(self.iris['feature_names'])
        print(" --- 2.target ---")
        print(self.iris['target'])
        print(" --- 3.print ---")
        print(self.iris)



    def create_model(self):
        X = self._X
        Y = self._Y
        enc = OneHotEncoder()
        Y_1hot = enc.fit_transform(Y.reshape(-1,1)).toarray()

        model = Sequential()

        model.add(Dense(4, input_dim = 4 ,activation = 'relu'))
        model.add(Dense(3, activation = 'softmax'))
        model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics=['accuracy'])
        model.fit(X,Y_1hot,epochs=300, batch_size=10)
        print('Model Training is completed')

        file_name = dir_path('iris')+'/save/iris_model.h5'
        model.save(file_name)
        print(f'Model Save in {file_name}')


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
    "1" : lambda x: x.hook(),
}

if __name__ == '__main__':
    iris = IrisModel()


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
