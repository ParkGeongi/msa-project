import csv
import time
from collections import defaultdict
from math import log, exp

from os import path

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

from paths.path import dir_path



class NaverMovieModel(object):
    def __init__(self):
        global url, savepath, encoding, filename, k, word_probs, driver_path
        self.word_probs = []
        encoding = "UTF-8"
        #filename = os.path.join(os.getcwd(),'nlp\\naver_review\\data\\review_train.csv')

        filename = dir_path('naver_movie') +'\\data\\review_train.csv'
        url = 'https://movie.naver.com/movie/point/af/list.naver?&page='
        driver_path =dir_path('webcrawler')+ '\\chromedriver.exe'
        savepath = dir_path('naver_movie')+ 'save\\review_train.csv'
        k = 0.5

    def crawling(self):
        if path.exists(savepath) == True:
            data = pd.read_csv(savepath, header=None)
            data.columns = ['review', 'score']
            result = [print(f"{i+1}. {data['score'][i]}\n{data['review'][i]}\n") for i in range(len(data))]
            return result

        else:
            driver = webdriver.Chrome(driver_path)
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

            with open(savepath, 'w', newline='', encoding=encoding) as f:
                wr = csv.writer(f)
                wr.writerows(review_data)
            driver.close()
            return "크롤링 완료"

    def load_corpus(self):
        corpus = pd.read_table(filename, sep=',', encoding=encoding)
        #print(corpus)
        corpus = np.array(corpus)
        return corpus

    def count_words(self, train_X):
        counts = defaultdict(lambda: [0, 0])
        for doc, point in train_X:

            if self.isNumber(doc) is False:
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 3.5 else 1] += 1  # 점수 3.5 이상이면 긍정

        return counts

    def isNumber(self, param):
        try:
            float(param)
            return True
        except ValueError:
            return False

    def probability(self, word_probs, doc):
        docwords = doc.split()
        log_prob_if_class0 = log_prob_if_class1 = 0.0
        for word, prob_if_class0, prob_if_class1 in word_probs:
            if word in docwords:
                log_prob_if_class0 += log(prob_if_class0)
                log_prob_if_class1 += log(prob_if_class1)
            else:
                log_prob_if_class0 += log(1 - prob_if_class0)
                log_prob_if_class1 += log(1 - prob_if_class1)
        prob_if_class0 = exp(log_prob_if_class0)
        prob_if_class1 = exp(log_prob_if_class1)
        return prob_if_class0 / (prob_if_class0 + prob_if_class1)

    def word_probablities(self, counts, n_class0, n_class1, k):
        return [(w,
                 (class0 + k) / (n_class0 + 2 * k),
                 (class1 + k) / (n_class1 + 2 * k))
                for w, (class0, class1) in counts.items()]

    def classify(self, doc):
        return self.probability(word_probs=self.word_probs, doc=doc)

    def model_fit(self):
        train_X = self.load_corpus()
        '''
        '재밌네요' : [1,0]
        '별로 재미없어요' [0,1]
        '''
        num_class0 = len([1 for _, point in train_X if point > 3.5])

        num_class1 = len(train_X) - num_class0
        word_counts = self.count_words(train_X)
        #print(word_counts)
        self.word_probs = self.word_probablities(word_counts, num_class0, num_class1, k)

