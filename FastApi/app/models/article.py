from pydantic import BaseConfig
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from app.models.mixins import TimstampMixin
from app.database import Base


class Article(Base, TimstampMixin):
    __tablename__ = 'articles'
    artseq = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(String(1000))
    userid = Column(String(30), ForeignKey('users.userid'), nullable=True)

    user = relationship('User', back_populates='articles')

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'글쓴이: {self.userid}, \n ' \
               f'글번호: {self.artseq}, \n ' \
               f'제목: {self.title} \n ' \
               f'내용: {self.content} \n' \
               f'작성일: {self.created} \n' \
               f'수정일: {self.modified} \n'
