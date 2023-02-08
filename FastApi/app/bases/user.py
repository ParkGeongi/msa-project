from abc import abstractmethod,ABCMeta
from typing import List
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserDTO, UserUpdate, UserFaker, ChatbotDTO


class UserBase(metaclass=ABCMeta):

    @abstractmethod
    def add_user(self, request_user: UserDTO) -> str: pass
    @abstractmethod
    def logout_user(self, request_user:UserDTO)->str: pass

    @abstractmethod
    def login_user(self, request_user: UserDTO) -> User: pass

    @abstractmethod
    def update_user(self, request_user: UserDTO) -> str: pass
    @abstractmethod
    def find_user_by_id_for_update(self, request_user: UserUpdate) -> User: pass
    @abstractmethod
    def update_token(self, db_user: User, new_token: str): pass
    @abstractmethod
    def update_password(self, request_user: UserDTO):pass
    @abstractmethod
    def delete_user(self, request_user: UserDTO) -> str: pass
    @abstractmethod
    def find_user_by_token(self, request_user: UserDTO) -> User:pass

    @abstractmethod
    def find_all_users(self) -> List[User]: pass

    @abstractmethod
    def find_user_by_id(self, request_user: UserDTO) -> UserDTO: pass

    @abstractmethod
    def find_userid_by_email(self, request_user: UserDTO) -> UserDTO: pass

    @abstractmethod
    def find_users_by_job(self, request_user: UserDTO) -> UserDTO:pass
    @abstractmethod
    def match_token(self, request_user: UserDTO) -> bool: pass
    @abstractmethod
    def match_token_for_update(self, request_user: UserUpdate) -> bool:pass

    @abstractmethod
    def count_all_users(self)->int:
        pass
    @abstractmethod
    def add_user_for_faker(self,request_user: UserFaker)->str: pass
    @abstractmethod
    def find_userid_by_email_for_faker(self, request_user: UserFaker) -> str:pass

