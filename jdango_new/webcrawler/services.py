import csv
import os

from selenium import webdriver

from webcrawler.models import ScrapVO
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from dataclasses import dataclass
import pandas as pd

class ScrapService(ScrapVO):
    def __init__(self):
        global driverpath, naver_url, save_path, file_path
        driverpath = r'C:\Users\AIA\project\jdango_new\webcrawler\chromedriver'
        naver_url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
        save_path = r'C:\Users\AIA\project\jdango_new\webcrawler\save\naver.csv'
        file_path = r'C:\Users\AIA\project\jdango_new\webcrawler\save\naver.csv'
    def bugsmusic(self,arg):# BeautifulSoup 기본 크롤링

        soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), 'lxml')
        title = {"class": arg.class_names[0]}
        artist = {"class": arg.class_names[1]}
        titles = soup.find_all(name=arg.tag_name, attrs=title)
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name=arg.tag_name, attrs=artist)
        artists = [i.find('a').text for i in artists]
        [print(f"{i}위 {j} : {k}")  # 디버깅
         for i, j, k in zip(range(1, len(titles)), titles, artists)]
        diction = {}  # dict 로 변환
        for i, j in enumerate(titles):
            diction[j] = artists[i]
        arg.diction = diction
        arg.dict_to_dataframe()
        arg.dataframe_to_csv()  # csv파일로 저장

    def melonmusic(self,arg):# BeautifulSoup 기본 크롤링
        soup = BeautifulSoup(
            urlopen(urllib.request.Request(arg.domain + arg.query_string, headers={'User-Agent': "Mozilla/5.0"})),
            "lxml")
        title = {"class": arg.class_names[0]}
        artist = {"class": arg.class_names[1]}
        titles = soup.find_all(name=arg.tag_name, attrs=title)
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name=arg.tag_name, attrs=artist)
        artists = [i.find('a').text for i in artists]
        [print(f"{i}위 {j} : {k}")  # 디버깅
         for i, j, k in zip(range(1, len(titles)), titles, artists)]
        diction = {}  # dict 로 변환
        for i, j in enumerate(titles):
            diction[j] = artists[i]
        arg.diction = diction
        arg.dict_to_dataframe()
        arg.dataframe_to_csv()  # csv파일로 저장

    def naver_movie_review(self):

        if os.path.isfile(file_path) == True:
            df = pd.read_csv(file_path)

            result = [{'rank' : i+1 , 'title' : df.columns[i]} for i in range(50)]
            print(result)
            #result = [{'rank' : f'{i+1}', 'title' : f'{j}'} for i ,j in enumerate(df)]




            return result


        else:
            driver = webdriver.Chrome(driverpath)
            driver.get(naver_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_divs = soup.find_all('div', attrs={'class', 'tit3'})
            products = [[div.a.string for div in all_divs]]
            with open(save_path, 'w', newline='', encoding='UTF-8') as f:
                wr = csv.writer(f)
                wr.writerows(products)
            driver.close()
            df = pd.read_csv(file_path)
            return df.columns[0]

if __name__ == '__main__':
    s = ScrapService()
    s.naver_movie_review()

