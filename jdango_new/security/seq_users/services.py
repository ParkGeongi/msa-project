import random

import pandas as pd
from sqlalchemy import create_engine

from basic.lambdas import cre_lambdas


class SeqUserService(object):
    def __init__(self):
        pass
    def df_to_sql(self):
        df = self.dataframe_create()
        engine = create_engine(
            "mysql+pymysql://root:root@localhost:3306/mydb",
            encoding='utf-8')
        df.to_sql(name='seq_users',
                  if_exists='append',
                  con = engine,
                  index=False)

    def dataframe_create(self):
        '''
        susers_id = models.AutoField(primary_key=True)
        user_email = models.CharField(max_length=20)
        password = models.CharField(max_length=20)
        user_name = models.CharField(max_length=20)
        phone = models.CharField(max_length=20)
        birth = models.CharField(max_length=20)
        address = models.CharField(max_length=20)
        job = models.CharField(max_length=20)
        user_interests = models.CharField(max_length=20)
        token = models.CharField(max_length=20)
            '''



        data =[{'user_email':cre_lambdas.lambda_string(3) + '@naver.com','password':'1',
                'user_name':cre_lambdas.lambda_k(2), 'phone':cre_lambdas.lambda_phone(4),'birth':cre_lambdas.lambda_birth(1985, 2011),
                'address':  random.choice(cre_lambdas.address_list),'job':random.choice(cre_lambdas.job_list),
                'user_interests':random.choice(cre_lambdas.interests_list),'token':'JWT fefege..'}
               for i in range(100)]

        print(data)
        df = pd.DataFrame(data)
        print(df)
        return data
    def get_users(self)->[]:
        print('포스트벤 요청이 도달하였음 !')

    def to_react(self):
        engine = create_engine(
            "mysql+pymysql://root:root@localhost:3306/mydb",
            encoding='utf-8')
        df = pd.read_sql_query('select * from seq_users', engine)
        print(df)
        data = df.to_dict('records')
        print(data)
        return data

if __name__ == '__main__':
    SeqUserService().to_react()
