from enum import Enum

import numpy as np
import pandas as pd
from keras import Input
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from paths.path import dir_path
from keras.layers import Dense, LSTM, concatenate
from keras.models import Sequential, Model
from abc import abstractmethod, ABCMeta

class H5FileNames(Enum):
    dnn_model = "DNN.h5"
    dnn_ensemble = "DNN_ensemble.h5"
    lstm_model = "LSTM.h5"
    lstm_ensemble = "LSTM_ensemble.h5"


#날짜                종가      오픈      고가      저가      거래량    변동 %


class Samsung_Stock_Base(metaclass=ABCMeta):
    def __init__(self):
        global path
        path = dir_path('aitrader')

    def normalization(self,df, npy_file_name):

        del df['변동 %']
        df.replace(np.nan, '0', regex=True, inplace=True)
        df = df.astype('str')
        df = df[df['거래량'] != '0']

        for i in range(len(df.index)):
            for j in range(len(df.iloc[i])):
                if df.iloc[i, j][-1] == "M":
                    df.iloc[i, j] = df.iloc[i, j].replace(',', '')
                    df.iloc[i, j] = df.iloc[i, j].replace('M', '')
                    df.iloc[i, j] = float(df.iloc[i, j])
                    df.iloc[i, j] = df.iloc[i, j] * 1000000

                elif df.iloc[i, j][-1] == "K":
                    df.iloc[i, j] = df.iloc[i, j].replace(',', '')
                    df.iloc[i, j] = df.iloc[i, j].replace('K', '')
                    df.iloc[i, j] = float(df.iloc[i, j])
                    df.iloc[i, j] = df.iloc[i, j] * 1000
                else:
                    df.iloc[i, j] = df.iloc[i, j].replace(',', '')
                    df.iloc[i, j] = float(df.iloc[i, j])

        df.sort_values(['날짜'], ascending=[True], inplace=True)
        print(df)
        df = df.values
        np.save(f'{path}\\save\\{npy_file_name}.npy', arr = df)
        npy = np.load(f'{path}\\save\\{npy_file_name}.npy', allow_pickle=True)
        return npy


    def split_xy5(self, dataset, time_step, y_column):
        x,y = list(), list()
        for i in range(len(dataset)):
            x_end_number = i + time_step
            y_end_number = x_end_number + y_column
            if y_end_number > len(dataset): break

            tmp_x = dataset[i:x_end_number,:]
            tmp_y = dataset[x_end_number:y_end_number, 0] # 종가
            x.append(tmp_x)
            y.append(tmp_y)
        return np.array(x), np.array(y)

    @abstractmethod
    def scaled(self, csv_file_name):
        pass

    @abstractmethod
    def create(self):
        pass

class Dnn_Model(Samsung_Stock_Base):

    def scaled(self, csv_file_name):
        df = pd.read_csv(f'{path}\\data\\{csv_file_name}.csv', index_col=0, header=0, encoding='utf-8', sep=',')
        npy = super().normalization(df,'samsung')
        x, y = super().split_xy5(npy, 5, 1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1] * x_train.shape[2])).astype(float)
        x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1] * x_test.shape[2])).astype(float)
        y_train = y_train.astype(float)
        y_test= y_test.astype(float)
        scalar = StandardScaler()
        scalar.fit(x_train)
        x_train_scaled = scalar.transform(x_train)
        x_test_scaled = scalar.transform(x_test)
        return x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled

    def create(self):
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = self.scaled('삼성전자')
        print(x_train_scaled[0, :])
        print(x_train_scaled.shape)

        model = Sequential()
        model.add(Dense(64, input_shape=(25,)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience=20)
        print('#####################DNN Model learning#####################')
        model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])
        loss, mse = model.evaluate(x_test_scaled, y_test, batch_size=1)
        print('loss : ', loss)
        print('mse: ', mse)

        model.save(f'{path}\\save\\{H5FileNames.dnn_model.value}')

        y_pred = model.predict(x_test_scaled)

        for i in range(5):
            print(f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}')

class Lstm_Model(Samsung_Stock_Base):

    def scaled(self,csv_file_name):
        df = pd.read_csv(f'{path}\\data\\{csv_file_name}.csv', index_col=0, header=0, encoding='utf-8', sep=',')
        npy = super().normalization(df, 'samsung')
        x, y = super().split_xy5(npy, 5, 1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        print(x_train)
        print(x_train.shape)
        x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1] * x_train.shape[2])).astype(float)
        x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1] * x_test.shape[2])).astype(float)
        y_train = y_train.astype(float)
        y_test= y_test.astype(float)
        print(x_train)
        print(type(x_train[0][0]))
        scalar = StandardScaler()
        scalar.fit(x_train)

        x_train_scaled = scalar.transform(x_train)
        print(x_train_scaled)
        x_test_scaled = scalar.transform(x_test)
        x_train_scaled = np.reshape(x_train_scaled, (x_train_scaled.shape[0], 5, 5))
        x_test_scaled = np.reshape(x_test_scaled, (x_test_scaled.shape[0], 5, 5))
        return x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled

    def create(self):
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = self.scaled('삼성전자')
        model = Sequential()
        model.add(LSTM(64,input_shape=(5,5)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss= 'mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience = 20)
        print('#####################LSTM Model learning#####################')
        model.fit(x_train_scaled, y_train, validation_split=0.2,verbose=1,batch_size=1,epochs=100,callbacks=[early_stopping])

        loss, mse = model.evaluate(x_test_scaled,y_test,batch_size=1)
        print('loss : ', loss)
        print('mse: ', mse)
        model.save(f'{path}\\save\\{H5FileNames.lstm_model.value}')

        y_pred = model.predict(x_test_scaled)

        for i in range(5):
            print(f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}')

class Dnn_Ensemble_Model(Samsung_Stock_Base):


    def scaled(self, csv_file_name):
        df = pd.read_csv(f'{path}\\data\\{csv_file_name}.csv', index_col=0, header=0, encoding='utf-8', sep=',')
        npy = super().normalization(df, 'samsung')
        x, y = super().split_xy5(npy, 5, 1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2])).astype(float)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2])).astype(float)
        y_train = y_train.astype(float)
        y_test = y_test.astype(float)
        scalar = StandardScaler()
        scalar.fit(x_train)
        x_train_scaled = scalar.transform(x_train)
        x_test_scaled = scalar.transform(x_test)
        print(x_train_scaled)
        return x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled

    def create(self):
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = self.scaled('삼성전자')
        x2_train, x2_test, y2_train, y2_test, x2_train_scaled, x2_test_scaled = self.scaled('코스피200내역1')

        input1 = Input(shape=(25,))
        dense1 = Dense(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)

        input2 = Input(shape=(25,))
        dense2 = Dense(64)(input2)
        dense2 = Dense(32)(dense2)
        dense2 = Dense(32)(dense2)
        output2 = Dense(32)(dense2)

        merge = concatenate([output1, output2])
        output3 = Dense(1)(merge)
        model = Model(inputs=[input1, input2], outputs=output3)

        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience=20)
        print('#####################DNN_Ensemble Model learning#####################')
        model.fit([x_train_scaled, x2_train_scaled], y_train, validation_split=0.2, verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])
        loss, mse = model.evaluate([x_test_scaled, x2_test_scaled], y_test, batch_size=1)
        print('loss : ', loss)
        print('mse: ', mse)

        model.save(f'{path}\\save\\{H5FileNames.dnn_ensemble.value}')

        y_pred = model.predict([x_test_scaled, x2_test_scaled])

        for i in range(5):
            print(f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}')


class Lstm_Ensemble_Model(Samsung_Stock_Base):

    def scaled(self,csv_file_name):
        df = pd.read_csv(f'{path}\\data\\{csv_file_name}.csv', index_col=0, header=0, encoding='utf-8', sep=',')
        npy = super().normalization(df, 'samsung')
        x, y = super().split_xy5(npy, 5, 1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1] * x_train.shape[2])).astype(float)
        x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1] * x_test.shape[2])).astype(float)
        y_train = y_train.astype(float)
        y_test= y_test.astype(float)
        scalar = StandardScaler()
        scalar.fit(x_train)
        x_train_scaled = scalar.transform(x_train)
        x_test_scaled = scalar.transform(x_test)
        x_train_scaled = np.reshape(x_train_scaled, (x_train_scaled.shape[0], 5, 5))
        x_test_scaled = np.reshape(x_test_scaled, (x_test_scaled.shape[0], 5, 5))
        return x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled

    def create(self):
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = self.scaled('삼성전자')
        x2_train, x2_test, y2_train, y2_test, x2_train_scaled, x2_test_scaled = self.scaled('코스피200내역1')

        input1 = Input(shape=(5, 5))
        dense1 = LSTM(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)

        input2 = Input(shape=(5, 5))
        dense2 = LSTM(64)(input2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        output2 = Dense(32)(dense2)

        merge = concatenate([output1, output2])
        output3 = Dense(1)(merge)
        model = Model(inputs=[input1, input2], outputs=output3)

        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience=20)
        print('#####################LSTM_Ensemble Model learning#####################')
        model.fit([x_train_scaled, x2_train_scaled], y_train, validation_split=0.2, verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])
        loss, mse = model.evaluate([x_test_scaled, x2_test_scaled], y_test, batch_size=1)
        print('loss : ', loss)
        print('mse: ', mse)
        model.save(f'{path}\\save\\{H5FileNames.lstm_ensemble.value}')


        y_pred = model.predict([x_test_scaled, x2_test_scaled])

        for i in range(5):
            print(f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}')


if __name__ == '__main__':
    s = Lstm_Model()
    s.create()
