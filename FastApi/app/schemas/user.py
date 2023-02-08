from datetime import datetime
from typing import List, Optional, Any
from uuid import UUID
from pydantic import BaseModel
from app.schemas.article import ArticleDTO


class UserDTO_C(BaseModel):
    class Config:
        orm_mode = True


class UserDTO(UserDTO_C):
    userid: Optional[str]
    email: Optional[str]
    password: Optional[str]
    username: Optional[str]
    phone: Optional[str]
    birth: Optional[str]
    address: Optional[str]
    job: Optional[str]
    interests: Optional[str]
    token: Optional[str]
    created: Optional[str]
    modified: Optional[str]


class ChatbotDTO(UserDTO_C):
    userid: Optional[str]
    email: Optional[str]


class UserUpdate(UserDTO_C):
    userid: Optional[str]
    phone: Optional[str]
    job: Optional[str]
    interests: Optional[str]
    token: Optional[str]


class UserGet(UserDTO_C):
    userid: Optional[str]
    email: Optional[str]
    password: Optional[str]
    username: Optional[str]
    phone: Optional[str]
    birth: Optional[str]
    address: Optional[str]
    job: Optional[str]
    interests: Optional[str]


class UserFaker(UserDTO_C):
    userid: Optional[str]
    email: Optional[str]
    password: Optional[str]
    username: Optional[str]
    phone: Optional[str]
    birth: Optional[str]
    address: Optional[str]


class UserDetail(UserDTO):
    articles: List[ArticleDTO] = []
