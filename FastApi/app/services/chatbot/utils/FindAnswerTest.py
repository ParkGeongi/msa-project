import os

from app.admin.path import dir_path
from app.services.chatbot.config.DatabaseConfig import *
from app.services.chatbot.tts_bot import Tts
from app.services.chatbot.utils.Database import Database
from app.services.chatbot.utils.Preprocess import Preprocess
from app.models.intent import INTENTModel
from app.models.ner import NERModel
from app.services.chatbot.utils.FindAnswer import FindAnswer
class FindAngserTest:
    def __init__(self):
        pass

    def exec(self,msg):
        # 전처리 객체 생성
        prepath1 = '/usr/src/app/app/services/chatbot/intent/data/chatbot_dict.bin'
        prepath2 = '/usr/src/app/app/services/chatbot/intent/data/user_dic.tsv'
        #p = Preprocess(word2index_dic=r'C:\Users\AIA\project\FastApi\app\services\chatbot\intent\data\chatbot_dict.bin',userdic=r'C:\Users\AIA\project\FastApi\app\services\chatbot\intent\data\user_dic.tsv')

        p = Preprocess(word2index_dic=prepath1,
                       userdic=prepath2)

        # 질문/답변 학습 디비 연결 객체 생성
        db = Database(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME
        )
        db.connect()    # 디비 연결

        # 원문
        #msg = '오전에 탕수육 10개 주문합니다'
        query = msg

        # 의도 파악
        #intent_h5_path = '/usr/src/app/app/services/chatbot/intent/save/intent_model.h5'
        intent_h5_path = dir_path(param="chatbot")+'/intent/save/intent_model.h5'

        #intent_local = INTENTModel(model_name=r'C:\Users\AIA\project\FastApi\app\services\chatbot\intent\save\intent_model.h5', proprocess=p)
        intent = INTENTModel(model_name=intent_h5_path, proprocess=p)
        predict = intent.predict_class(query)
        intent_name = intent.labels[predict]

        # 개체명 인식
        ner_h5_path = dir_path(param="chatbot")+'/ner/save/ner_model.h5'
        #ner = NERModel(model_name=r'C:\Users\AIA\project\FastApi\app\services\chatbot\ner\save\ner_model.h5', proprocess=p)
        ner = NERModel(model_name=ner_h5_path,
                       proprocess=p)
        predicts = ner.predict(query)
        ner_tags = ner.predict_tags(query)

        print("질문 : ", query)
        print("=" * 40)
        print("의도 파악 : ", intent_name)
        print("답변 검색에 필요한 NER 태그 : ", ner_tags)
        print("=" * 40)

        # 답변 검색


        try:
            f = FindAnswer(db)
            answer_text, answer_image = f.search(intent_name, ner_tags)
            answer = f.tag_to_word(predicts, answer_text)
        except:
            answer = "죄송해요, 무슨 말인지 모르겠어요."

        print("답변 : ", answer)

        if msg == '종료':
            answer = '채팅이 끝났습니다.'
            db.close()  #  디비 연결 끊음

        return answer
