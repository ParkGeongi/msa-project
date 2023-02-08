import csv
import os
import time
from collections import defaultdict
from math import log, exp

from os import path

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
from sklearn.model_selection import train_test_split

from nlp.naver_movie.models import NaverMovieModel


class ReviewService(object):
    def __init__(self):
        pass

    def process(self):
        model = NaverMovieModel()
        model.model_fit()
        text = '"시간 아깝다. 정말 평범한 영화다"'
        score = model.classify(text)
        score = f'{int(round(score, 2) * 100)}%'
        return score
    def to_frontend(self,text):
        model = NaverMovieModel()
        model.model_fit()
        score = model.classify(text)
        positive = int(round(score,3) * 100)

        return positive



imdb_menu = ["Exit",  # 0
             "hook",  # 1
             ]
imdb_lambda = {
    "1": lambda x: x.process(),
}
if __name__ == '__main__':
    result = ReviewService().process()
    print(f'긍정률: {result}')
