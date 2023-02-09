from app.models.intent import INTENTModel
from app.services.chatbot.utils.Preprocess import Preprocess

p = Preprocess(word2index_dic=r'C:\Users\AIA\project\FastApi\app\services\chatbot\intent\data\chatbot_dict.bin',
               userdic=r'C:\Users\AIA\project\FastApi\app\services\chatbot\intent\data\chatbot_dict.bin')

intent = INTENTModel(model_name=r'C:\Users\AIA\project\FastApi\app\services\chatbot\intent\save\intent_model.h5', proprocess=p)
query = "오늘 짬뽕 주문 가능한가요?"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(query)
print("의도 예측 클래스 : ", predict)
print("의도 예측 레이블 : ", predict_label)

