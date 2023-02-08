import numpy as np
import pandas as pd
from keras.models import load_model
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder

from paths.path import dir_path


class SquartService(object):
    def __init__(self):
        pass

    def service_model(self,i):
        model = load_model(dir_path('squart')+r'\save\squart_model_4.h5.h5')
        df = pd.read_csv(dir_path('squart')+r'\data\tt.csv')
        train, test = train_test_split(df, test_size=0.99)
        print(test.shape)
        x_test = test[
            ['x[0]', 'x[1]', 'x[2]', 'x[3]', 'x[4]', 'x[5]', 'x[6]', 'x[7]', 'x[8]', 'x[9]', 'x[10]', 'x[11]', 'x[12]',
             'x[13]', 'x[14]', 'x[15]', 'x[16]', 'x[17]', 'x[18]', 'x[19]', 'x[20]', 'x[21]', 'x[22]', 'x[23]', 'x[24]',
             'y[0]', 'y[1]', 'y[2]', 'y[3]', 'y[4]', 'y[5]', 'y[6]', 'y[7]', 'y[8]', 'y[9]', 'y[10]', 'y[11]', 'y[12]',
             'y[13]', 'y[14]', 'y[15]', 'y[16]', 'y[17]', 'y[18]', 'y[19]', 'y[20]', 'y[21]', 'y[22]', 'y[23]',
             'y[24]']]
        y_test = test.label
        x1_test = x_test.loc[[i],:]


        print(x1_test)
        print(x1_test.shape)
        predictions = model.predict(x1_test, verbose=0)
        pred = np.argmax(predictions)
        print(f'###################### 예측 값 : {pred}')
        print(f'###################### 실제 값 : {y_test.loc[i]}')
    def confusoin_matrix(self):
        model = load_model(dir_path('squart')+r'\save\squart_model3.h5')
        df = pd.read_csv(dir_path('squart')+r'\data\tt.csv')

        X = df[
            ['x[0]', 'x[1]', 'x[2]', 'x[3]', 'x[4]', 'x[5]', 'x[6]', 'x[7]', 'x[8]', 'x[9]', 'x[10]', 'x[11]', 'x[12]',
             'x[13]', 'x[14]', 'x[15]', 'x[16]', 'x[17]', 'x[18]', 'x[19]', 'x[20]', 'x[21]', 'x[22]', 'x[23]', 'x[24]',
             'y[0]', 'y[1]', 'y[2]', 'y[3]', 'y[4]', 'y[5]', 'y[6]', 'y[7]', 'y[8]', 'y[9]', 'y[10]', 'y[11]', 'y[12]',
             'y[13]', 'y[14]', 'y[15]', 'y[16]', 'y[17]', 'y[18]', 'y[19]', 'y[20]', 'y[21]', 'y[22]', 'y[23]',
             'y[24]']]
        Y = df[['label']]



        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.99, stratify = Y)

        Y_train = Y_train.to_numpy()
        Y_test = Y_test.to_numpy()
        enc = OneHotEncoder()
        Y_train_hot = enc.fit_transform(Y_train.reshape(-1, 1)).toarray()
        Y_test_hot = enc.fit_transform(Y_test.reshape(-1, 1)).toarray()
        print(Y_train_hot)

        Y_pred = model.predict(np.array(X_test))
        Y_pred = np.array(Y_pred)


        matrix = confusion_matrix(Y_pred.argmax(axis=1), Y_test_hot.argmax(axis=1))
        sns.heatmap(matrix, annot=True, cmap='Blues')
        plt.show()


squart_menu = ["Exit",  # 0
               "hook",  # 1
               ]
squart_lambda = {
    "1": lambda x: x.service_model(),
    "2": lambda x: x.confusoin_matrix()

}

if __name__ == '__main__':
    s = SquartService()
    while True :
        menu = int(input('메뉴'))
        if menu == 0:
            break
        elif menu == 1:

            i= int(input('인덱스 번호(~1545)'))
            s.service_model((i))
        elif menu ==2:
            s.confusoin_matrix()
        else: print('다시')
