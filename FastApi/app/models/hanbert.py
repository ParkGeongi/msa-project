from Korpora import Korpora
from tokenizers.implementations import BertWordPieceTokenizer
import os

class Hanbert():
    def __init__(self):
        self.nsmc = Korpora.load("nsmc", force_download=True)

    import os
    def write_lines(self,path, lines):
        with open(path, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(f'{line}\n')
    def exec(self):
        self.write_lines("./data/hanbert/train.txt", self.nsmc.train.get_all_texts())
        self.write_lines("./data/hanbert/test.txt", self.nsmc.test.get_all_texts())
        wordpiece_tokenizer = BertWordPieceTokenizer(lowercase=False)
        wordpiece_tokenizer.train(
            files=["./data/hanbert/train.txt", "./data/hanbert/test.txt"],
            vocab_size=10000,
        )
        # wordpiece_tokenizer.save_model("/gdrive/My Drive/nlpbook/wordpiece")
        wordpiece_tokenizer.save_model("./save/wordpiece")

if __name__ == '__main__':
    Hanbert().exec()