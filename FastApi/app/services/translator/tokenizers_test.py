import pandas as pd
import urllib.request
from tokenizers.implementations import BertWordPieceTokenizer

"""
구글이 공개한 딥 러닝 모델 BERT에는 WordPiece Tokenizer가 사용되었습니다. 
허깅페이스는 해당 토크나이저를 직접 구현하여 tokenizers라는 패키지를 통해 
버트워드피스토크나이저(BertWordPieceTokenizer)를 제공합니다.
여기서는 네이버 영화 리뷰 데이터를 해당 토크나이저에 학습시키고, 
이로부터 서브워드의 단어 집합(Vocabulary)을 얻습니다. 
그리고 임의의 문장에 대해서 학습된 토크나이저를 사용하여 토큰화를 진행합니다. 
우선 네이버 영화 리뷰 데이터를 로드합니다.
"""


class TokenizersTest:
    def __init__(self):
        pass

    def exec(self):
        urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings.txt",
                                   filename="ratings.txt")
        naver_df = pd.read_table('ratings.txt')
        naver_df = naver_df.dropna(how='any')
        with open('naver_review.txt', 'w', encoding='utf8') as f:
            f.write('\n'.join(naver_df['document']))
        tokenizer = BertWordPieceTokenizer(lowercase=False)
        """
        lowercase : 대소문자를 구분 여부. True일 경우 구분하지 않음.
        strip_accents : True일 경우 악센트 제거.
        ex) é → e, ô → o
        """

        data_file = 'naver_review.txt'
        vocab_size = 30000
        limit_alphabet = 6000
        min_frequency = 5
        # 버트워드피스토크나이저를 설정합니다.
        tokenizer.train(files=data_file,
                        vocab_size=vocab_size,
                        limit_alphabet=limit_alphabet,
                        min_frequency=min_frequency)
        """
        files : 단어 집합을 얻기 위해 학습할 데이터
        vocab_size : 단어 집합의 크기
        limit_alphabet : 병합 전의 초기 토큰의 허용 개수.
        min_frequency : 최소 해당 횟수만큼 등장한 쌍(pair)의 경우에만 병합 대상이 된다.
        """
        # 네이버 영화 리뷰 데이터를 학습하여 단어 집합을 얻어봅시다.
        data_file = 'naver_review.txt'
        vocab_size = 30000
        limit_alphabet = 6000
        min_frequency = 5

        tokenizer.train(files=data_file,
                        vocab_size=vocab_size,
                        limit_alphabet=limit_alphabet,
                        min_frequency=min_frequency)

        # vocab 저장
        tokenizer.save_model('./save')
        encoded = tokenizer.encode('아 배고픈데 짜장면먹고싶다')
        print('토큰화 결과 :', encoded.tokens)
        print('정수 인코딩 :', encoded.ids)
        print('디코딩 :', tokenizer.decode(encoded.ids))

if __name__ == '__main__':
    TokenizersTest().exec()
