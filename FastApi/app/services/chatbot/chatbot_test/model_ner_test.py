from app.models.ner import NERModel
from app.services.chatbot.utils.Preprocess import Preprocess

p = Preprocess(word2index_dic=r'C:\Users\AIA\project\FastApi\app\services\chatbot\intent\data\chatbot_dict.bin',
               userdic=r'C:\Users\AIA\project\FastApi\app\services\chatbot\intent\data\chatbot_dict.bin')



ner = NERModel(model_name=r'C:\Users\AIA\project\FastApi\app\services\chatbot\ner\save\ner_model.h5', proprocess=p)
query = '오늘 오전 13시 2분에 탕수육 주문 하고 싶어요'
predicts = ner.predict(query)
tags = ner.predict_tags(query)
print(predicts)
print(tags)

