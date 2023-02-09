from app.models.intent import INTENTModel
from utils.Preprocess import Preprocess


p = Preprocess(word2index_dic=r'C:\Users\AIA\project\FastApi\app\services\chatbot\intent\data\chatbot_dict.bin',
               userdic=r'C:\Users\AIA\project\FastApi\app\services\chatbot\intent\data\user_dic.tsv')

intent = INTENTModel(model_name=r'C:\Users\AIA\project\FastApi\app\services\chatbot\intent\save\intent_model.h5', proprocess=p)
query = "오늘 탕수육 주문 가능한가요?"
c = intent.predict_class(query)
print(intent.labels[c])