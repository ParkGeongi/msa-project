import csv
import time

from os import path

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
from sklearn.model_selection import train_test_split

from paths.path import dir_path


class ImdbService(object):

    def __init__(self):
        global train_input,train_target,test_input,test_target, val_input,val_target,lengths
        (train_input, train_target), (test_input, test_target) = tf.keras.datasets.imdb.load_data(num_words=500)
        train_input, val_input, train_target, val_target = train_test_split(train_input, train_target, test_size=0.2,
                                                                            random_state=42)
        lengths = np.array([len(x) for x in train_input])
    def hook(self):
        self.spec()
        self.plt_grapth()

    def spec(self):

        print(train_input.shape, test_input.shape)
        print(train_input)
        print(len(train_input[0]))
        print(len(train_input[1]))
        print(len(train_input[0]))
        print(train_target[:20])

        print(np.mean(lengths), np.median(lengths))
        return lengths
    def plt_grapth(self):
        plt.hist(lengths)
        plt.xlabel('length')
        plt.ylabel('freq')


        plt.show()

class NaverMovieService(object):
    def __init__(self):
        global url, savepath, encoding
        savepath = dir_path('imdb')+'\\save'
        encoding = "UTF-8"
        url ='https://movie.naver.com/movie/point/af/list.naver?&page='

    def crawling(self):
        if path.exists(f"{savepath}\\naver_movie_review.csv") == True:
            data = pd.read_csv(f"{savepath}\\naver_movie_review.csv", header=None)
            data.columns = ['review', 'score']
            result = [print(f"{i+1}. {data['score'][i]}\n{data['review'][i]}\n") for i in range(len(data))]
            return result

        else:

            driver = webdriver.Chrome(dir_path('webcrawler') + '\\chromedriver.exe')
            review_data = []

            for page in range(1, 3):
                driver.get(url+str(page))
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                # find_all : 지정한 태그의 내용을 모두 찾아 리스트로 반환
                all_tds = soup.find_all('td', attrs={'class', 'title'})
            # 한 페이지의 리뷰 리스트의 리뷰를 하나씩 보면서 데이터 추출
                for review in all_tds:
                    need_reviews_cnt = 1000
                    sentence = review.find("a", {"class": "report"}).get("onclick").split("', '")[2]
                    if sentence != "":  # 리뷰 내용이 비어있다면 데이터를 사용하지 않음
                        score = review.find("em").get_text()
                        review_data.append([sentence, int(score)])
                        need_reviews_cnt -= 1
            # 현재까지 수집된 리뷰가 목표 수집 리뷰보다 많아진 경우 크롤링 중지
                    if need_reviews_cnt < 0:break

            #
            #             # 다음 페이지를 조회하기 전 1초 시간 차를 두기
            time.sleep(1)

            with open(f'{savepath}\\naver_movie_review.csv', 'w', newline='', encoding=encoding) as f:
                wr = csv.writer(f)
                wr.writerows(review_data)
            driver.close()
            return "크롤링 완료"

imdb_menu = ["Exit",  # 0
             "hook",  # 1
             ]
imdb_lambda = {
    "1": lambda x: x.hook(),
}
if __name__ == '__main__':
    n =ImdbService()
    n.plt_grapth()


'''
if __name__ == '__main__':
    imdb =ImdbService()

    while True:
        [print(f"{i}. {j}") for i, j in enumerate(imdb_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                imdb_lambda[menu](imdb)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")

'''