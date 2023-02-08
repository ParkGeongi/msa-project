from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from keras import Input
from keras.callbacks import EarlyStopping
from numpy.ma import indices
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from paths.path import dir_path
from keras.layers import Dense, LSTM, concatenate
from keras.models import Sequential, Model, load_model
from abc import abstractmethod, ABCMeta
import tensorflow as tf
#날짜                종가      오픈      고가      저가      거래량    변동 %

class Samsung_Stock_Service(object):


    def __init__(self):
        global path, DNN, LSTM, samsung, kospi, DNN_E, LSTM_E
        path = dir_path('aitrader')
        DNN = load_model(f'{path}\\save\\DNN.h5')
        LSTM = load_model(f'{path}\\save\\LSTM.h5')
        DNN_E = load_model(f'{path}\\save\\DNN_Ensemble.h5')
        LSTM_E = load_model(f'{path}\\save\\LSTM_Ensemble.h5')
        samsung = 'samsung_test'
        kospi = 'kospi_test'
    def hook(self):
        return 'a'




    def normalization(self, df):
        df2 = df
        for i in range(len(df2.index)):
            for j in range(len(df2.iloc[i])):
                if j ==0:
                    df2.iloc[i, j] = df2.iloc[i, j].replace(' ', '')
                else:
                    if df2.iloc[i, j][-1] == "M":
                        df2.iloc[i, j] = df2.iloc[i, j].replace(',', '')
                        df2.iloc[i, j] = df2.iloc[i, j].replace(',', '')
                        df2.iloc[i, j] = df2.iloc[i, j].replace('M', '')
                        df2.iloc[i, j] = float(df2.iloc[i, j])
                        df2.iloc[i, j] = df2.iloc[i, j] * 1000000

                    elif df2.iloc[i, j][-1] == "K":
                        df2.iloc[i, j] = df2.iloc[i, j].replace(',', '')
                        df2.iloc[i, j] = df2.iloc[i, j].replace('K', '')
                        df2.iloc[i, j] = float(df2.iloc[i, j])
                        df2.iloc[i, j] = df2.iloc[i, j] * 1000
                    else:
                        df2.iloc[i,j] = df2.iloc[i, j].replace(',', '')
                        df2.iloc[i, j] = float(df2.iloc[i, j])



    def df_to_npy(self,df):
        ls = list(df['날짜'])
        idx = pd.to_datetime(ls)
        df = df.set_index(idx)
        del df['날짜']
        df = df.values
        print(df)
        npy_file_name = 'test2.npy'
        np.save(f'{path}\\save\\{npy_file_name}.npy', arr=df)
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

    def DNN_scaled(self):
        df = self.preprocessing()
        npy = self.df_to_npy(df)
        print(npy.shape)
        x = np.array(npy)
        x = np.reshape(x, (1, x.shape[0] * x.shape[1])).astype(float)
        print(x)
        x = tf.constant(x)
        scalar = StandardScaler()
        scalar.fit(x)
        x_scaled = scalar.transform(x)
        print(x_scaled)
        return x_scaled


    def LSTM_scaled(self,x):
        x = np.reshape(x, (1, x.shape[0] * x.shape[1]))
        x = tf.constant(x)
        x = np.array(x)
        scaler = StandardScaler()
        scaler.fit(x)  # 표준화를 수행 함수 생성
        x_scaled = scaler.transform(x)  # 표준화 수행
        x_scaled = np.array(x_scaled)
        x_scaled = np.reshape(x_scaled, (x_scaled.shape[0], 5, 5))

        return x_scaled
    def extract_5_days(self,start_day):

        df = self.preprocessing()
        ls = list(df['날짜'])
        idx = pd.to_datetime(ls)

        x_scaled = self.DNN_scaled()
        df2 = pd.DataFrame(x_scaled,index = idx,columns = ['종가','오픈','고가','저가','거래량'])
        df2 = df2[start_day:]
        df2 = df2.head(5)

        return df2
    def preprocessing(self,file_name):

        df1 = pd.read_csv(f'{path}\\data\\{file_name}.csv',header=0, encoding='utf-8', sep=',')
        del df1['변동 %']
        df1 = df1.dropna(axis=0)
        df1 = df1.astype(str)
        df1 = df1.replace(np.nan, '0')

        df1['날짜'] = df1['날짜'].replace(" ", '')
        df1['거래량'] = df1['거래량'].replace("", '0')
        df1 = df1[df1['거래량'] != '0']
        self.normalization(df1)
        df1.sort_values(['날짜'], ascending=[True], inplace=True)
        return df1




    def scaling(self,start_day):
        df = self.preprocessing(samsung)
        ls = list(df['날짜'])
        idx = pd.to_datetime(ls)

        df1 = self.preprocessing(samsung)
        npy = self.df_to_npy(df1)
        npy = np.array(npy).astype(float)
        std_data = (npy - np.mean(npy, axis=0)) / np.std(npy, axis=0)

        df2 = pd.DataFrame(std_data, index=idx, columns=['종가', '오픈', '고가', '저가', '거래량'])
        df2 = df2[start_day:]
        df2 = df2.head(5)

        ls = df2.index

        date = ls[-1].date()
        #start = ls[0].date().weekday()
        if date.weekday() == 4:
            future_day = date + timedelta(days=3)
        else:
            future_day = date + timedelta(days=1)

        return df2, str(future_day)

    def kospi_scaling(self,start_day):
        df = self.preprocessing(kospi)
        ls = list(df['날짜'])
        idx = pd.to_datetime(ls)

        df1 = self.preprocessing(kospi)
        npy = self.df_to_npy(df1)
        npy = np.array(npy).astype(float)
        std_data = (npy - np.mean(npy, axis=0)) / np.std(npy, axis=0)

        df2 = pd.DataFrame(std_data, index=idx, columns=['종가', '오픈', '고가', '저가', '거래량'])
        df2 = df2[start_day:]
        df2 = df2.head(5)

        return df2

    def pre2(self, start_day):
        df, future_day = self.scaling(start_day)
        print(df)
        x_scaled = np.array(df.values).astype(float)
        x_scaled = np.concatenate(x_scaled)
        x_scaled = np.expand_dims(x_scaled, axis=0)
        print(x_scaled)
        return future_day, x_scaled

    def pre3(self, start_day):
        df = self.kospi_scaling(start_day)
        print(df)
        x_scaled = np.array(df.values).astype(float)
        x_scaled = np.concatenate(x_scaled)
        x_scaled = np.expand_dims(x_scaled, axis=0)
        print(x_scaled)
        return x_scaled

    def DNN_predict(self,start_day):

        #start_day_date = datetime.strptime(start_day, '%Y-%m-%d').date()
        #pred_day = start_day_date + timedelta(days=5)
        #pred_day = str(pred_day)

        future_day, x_scaled = self.pre2(start_day)
        y_pred = DNN.predict(x_scaled)
        print(y_pred[0][0])
        print(future_day)
        return str(y_pred[0][0]), future_day


    def LSTM_predict(self,start_day):
        future_day, x_scaled = self.pre2(start_day)
        x_scaled = np.reshape(x_scaled, (x_scaled.shape[0], 5, 5))
        print(x_scaled)
        y_pred = LSTM.predict(x_scaled)
        print(y_pred[0][0])
        print(future_day)
        return str(y_pred[0][0]), future_day
    def DNN_Ensemble_pred(self,start_day):
        future_day, x_scaled = self.pre2(start_day)
        kospi_scaled = self.pre3(start_day)

        y_pred = DNN_E.predict([x_scaled,kospi_scaled])

        print(y_pred[0][0])
        print(future_day)
        return str(y_pred[0][0]), future_day
    def LSTM_Ensemble_pred(self,start_day):
        future_day, x_scaled = self.pre2(start_day)
        x_scaled = np.reshape(x_scaled, (x_scaled.shape[0], 5, 5))
        kospi_scaled = self.pre3(start_day)
        kospi_scaled = np.reshape(kospi_scaled, (x_scaled.shape[0], 5, 5))


        y_pred = LSTM_E.predict([x_scaled,kospi_scaled])
        print(y_pred[0][0])
        print(future_day)
        return str(y_pred[0][0]), future_day

# 5일 동안의   종가      오픈      고가      저가      거래량을 토대로 6일 째 종가를 예측하는 모델
   # x = [[70200.0, 71600.0, 71600.0, 70200.0, 12610000.0],
    #     [70600.0, 70300.0, 70600.0, 69800.0, 590.0],
     #    [70500.0, 70400.0, 70900.0, 70100.0, 4890.0],
     #    [70200.0, 70300.0, 70900.0, 70200.0, 980.0],
      #   [69900.0, 69900.0, 70000.0, 69600.0, 11440000.0]]


if __name__ == '__main__':
    start_day='2022-9-16'
    s = Samsung_Stock_Service()
    s.LSTM_Ensemble_pred(start_day)
