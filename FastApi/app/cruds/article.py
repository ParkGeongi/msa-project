from abc import ABC

from app.bases.article import ArticleBase
from app.models.article import Article

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.article import ArticleDTO


class ArticleCrud(ArticleBase, ABC):
    def __init__(self, db: Session):
        self.db: Session = db

    def add_article(self, request_article: ArticleDTO) -> str:
        article = Article(**request_article.dict())

        self.db.add(article)
        self.db.commit()
        return "success"

    def update_article_by_userid(self, request_article: ArticleDTO) -> str:
        article = Article(**request_article.dict())
        userid = article.userid
        update_query = self.db.query(Article).filter(Article.userid == userid)
        update = update_query.first()
        if not update:
            return 'fail'
        update_data = request_article.dict(exclude_unset=True)
        del (update_data['userid'])
        update_query.filter(Article.userid == userid).update(update_data, synchronize_session=False)
        self.db.commit()
        return 'success'

    def delete_article_by_title(self, request_article: ArticleDTO) -> str:
        article = Article(**request_article.dict())
        title = article.title
        delete_title_query = self.db.query(Article).filter(Article.title == title)
        delete_title = delete_title_query.first()
        if not delete_title:
            return 'fail'
        delete_title_query.delete(synchronize_session=False)
        self.db.commit()
        return 'success'

    def find_all_articles(self, page: int) -> list:
        print(f"page number is {page}")
        return self.db.query(Article).all()

    def find_articles_by_userid(self, page: int, request_article: ArticleDTO) -> list:
        article = Article(**request_article.dict())
        print(f"page number is {page}")
        return self.db.query(Article).filter(Article.userid == article.userid).all()

    def find_article_by_seq(self, request_article: ArticleDTO) -> ArticleDTO:
        article = Article(**request_article.dict())
        return self.db.query(Article).filter(Article.artseq == article.artseq).first()


