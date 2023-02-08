from abc import ABCMeta, abstractmethod

from app.schemas.article import ArticleDTO


class ArticleBase(metaclass=ABCMeta):
    @abstractmethod
    def add_article(self, request_article: ArticleDTO) -> str:
        pass

    @abstractmethod
    def update_article_by_userid(self, request_article: ArticleDTO) -> str: pass

    @abstractmethod
    def delete_article_by_title(self, request_article: ArticleDTO) -> str: pass

    @abstractmethod
    def find_all_articles(self, page: int) -> str: pass

    @abstractmethod
    def find_articles_by_userid(self, page: int, request_article: ArticleDTO) -> ArticleDTO: pass


    @abstractmethod
    def find_article_by_seq(self, request_article: ArticleDTO) -> str: pass

