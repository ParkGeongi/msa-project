import warnings
from datetime import datetime

import pandas as pd
from prophet import Prophet

from paths.path import dir_path

warnings.filterwarnings('ignore')
import pandas_datareader.data as web
from pandas_datareader import data
import yfinance as yf
path = "c:/Windows/Fonts/malgun.ttf"
import platform
from matplotlib import font_manager, rc, pyplot as plt

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
plt.rcParams['axes.unicode_minus'] = False
yf.pdr_override()
'''
Date    Open     High      Low    Close     Adj Close   Volume  
퀀트
'''

class AiTraderService(object):
    def __init__(self):
        global start_date, end_date, item_code
        start_date = '2000-1-1'
        end_date = '2022-12-31'
        item_code = '005930.KS'
        #000270

    def hook(self):
        KIA = data.get_data_yahoo(item_code, start_date, end_date)
        print(KIA.head(3))
        print(KIA.tail(3))
        KIA['Close'].plot(figsize = (12,6), grid=True)
        item_trunc = KIA[:'2021-12-31']
        df = pd.DataFrame({'ds': item_trunc.index, 'y': item_trunc['Close']})
        df.reset_index(inplace=True)
        del df['Date']
        prophet = Prophet(daily_seasonality=True)
        prophet.fit(df)
        future = prophet.make_future_dataframe(periods=365*5)
        forecast = prophet.predict(future)
        prophet.plot(forecast)
        plt.figure(figsize=(12,6))
        plt.plot(KIA.index, KIA['Close'], label = 'real')
        plt.plot(forecast['ds'], forecast['yhat'], label = 'forecast')
        plt.grid()
        plt.legend()
        path = dir_path('aitrader')
        print(f'path : {path}')
        plt.savefig(f'{path}\\samsung_close.png')

if __name__ == '__main__':
    ai =AiTraderService()
    ai.hook()



















