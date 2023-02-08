from abc import ABC
from typing import List, Tuple

from fastapi import HTTPException
from fastapi_pagination import Params
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.admin.security import verify_password, generate_token, get_hashed_password, myuuid
from app.bases.user import UserBase
from app.models.user import User
from app.schemas.user import UserDTO, UserUpdate, UserFaker, ChatbotDTO
from starlette.responses import JSONResponse


class UserCrud(UserBase, ABC):
    def __init__(self, db:Session):
        self.db : Session = db


    def add_user(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        userid = self.find_userid_by_email(request_user)
        print(userid)
        if userid == "":
            user.userid = myuuid()
            print(f'해시전 비번 : {user.password}')
            user.password = get_hashed_password(user.password)
            print(f"해시후 비번 : {user.password}")
            is_success = self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            message = "SUCCESS: 회원가입이 완료되었습니다" if is_success != 0 else "FAILURE: 회원가입이 실패하였습니다"
        else:
            message = "FAILURE: 이메일이 이미 존재합니다"
        return message
    def add_user_for_faker(self,request_user: UserFaker)->str:
        user = User(**request_user.dict())
        userid = self.find_userid_by_email_for_faker(request_user)
        print(userid)
        if userid == "":
            user.userid = myuuid()
            print(f'해시전 비번 : {user.password}')
            user.password = get_hashed_password(user.password)
            print(f"해시후 비번 : {user.password}")
            is_success = self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            message = "SUCCESS: 회원가입이 완료되었습니다" if is_success != 0 else "FAILURE: 회원가입이 실패하였습니다"
        else:
            message = "FAILURE: 이메일이 이미 존재합니다"
        return message

    def login_user(self, request_user: UserDTO) -> str:
        userid = self.find_userid_by_email(request_user)
        if userid != '':
            request_user.userid = userid
            db_user = self.find_user_by_id(request_user)
            print(request_user.password)
            print(db_user.password)
            verified = verify_password(plain_password=request_user.password,
                                   hashed_password=db_user.password)
            print(verified)
            if verified:
                new_token = generate_token(request_user.email)
                request_user.token = new_token
                self.update_token(db_user,new_token)
                return new_token
            else:
                return "FAILURE: 비밀번호가 일치하지 않습니다."
        else:
            return "FAILURE: 이메일 주소가 일치하지 않습니다."

    def logout_user(self, request_user:UserDTO)->str:
        user = self.find_user_by_token(request_user)
        is_success = self.db.query(User).filter(User.userid==user.userid)\
            .update({User.token: ""}, synchronize_session=False)
        self.db.commit()
        return '로그아웃 성공' if is_success !=0 else "로그아웃 실패"


    def update_token(self, db_user: User, new_token: str)->UserDTO:
        print('토큰 수정 메소드 진입')
        is_success = self.db.query(User).filter(User.userid == db_user.userid) \
            .update({User.token: new_token}, synchronize_session=False)
        print(f"수정 완료 후 성공이면 : {is_success}:")
        self.db.commit()
        self.db.refresh(db_user)
        return is_success

    def update_user(self, request_user: UserUpdate)->str:
        db_user = self.find_user_by_id_for_update(request_user)
        for var, value in vars(request_user).items():
            setattr(db_user, var, value) if value else None
        is_success = self.db.add(db_user)
        db_user.password = get_hashed_password(db_user.password)
        self.db.commit()
        self.db.refresh(db_user)
        return "업데이트 성공" if is_success != 0 else "업데이트 실패"

    def find_user_by_id_for_update(self, request_user: UserUpdate) -> User:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.userid == user.userid).one_or_none()

    def update_password(self, request_user: UserDTO)->str:
        user = User(**request_user.dict())
        print(user.password)
        user.password = get_hashed_password(user.password)
        is_success = self.db.query(User).filter(User.userid == user.userid) \
            .update({User.password: user.password}, synchronize_session=False)
        self.db.commit()

        return "비번 바꾸기 성공" if is_success != 0 else "비번 바꾸기 실패"

    def delete_user(self,  request_user: UserDTO) -> str:
        user = self.find_user_by_id(request_user)
        is_success = self.db.query(User).filter(User.userid==user.userid).\
            delete(synchronize_session=False)
        self.db.commit()
        return '탈퇴 성공' if is_success !=0 else "탈퇴 실패"

    def find_all_users(self)-> list[User]:

        return self.db.query(User).order_by(User.created).all()
    def find_userid_by_email_for_faker(self, request_user: UserFaker) -> str:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.email == user.email).first()
        if db_user is not None:
            return db_user.userid
        else:
            return ""

    def find_userid_by_email(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.email == user.email).first()
        if db_user is not None:
            return db_user.userid
        else:
            return ""

    def find_users_by_job(self, request_user: UserDTO) -> list:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.job == user.job).all()

    def find_user_by_id(self, request_user: UserDTO) -> User:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.userid == user.userid).one_or_none()

    def find_user_by_token(self, request_user: UserDTO) -> UserDTO:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.token == user.token).one_or_none()
    def match_token(self, request_user:UserDTO)-> bool:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.token == user.token).one_or_none()
        return True if db_user is not None else False

    def match_token_for_update(self, request_user:UserUpdate)-> bool:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.token == user.token).one_or_none()
        return True if db_user is not None else False

    def count_all_users(self)->int:
        return self.db.query(User.userid).count()


'''
def find_users_legacy():
    conn = pymysql.connect(host=DB_HOST, port=PORT, user=DB_USER, password=DB_PASSWORD, db=DB_NAME, charset='utf8')
    cursor = conn.cursor()  # MySQL에 접속
    sql = "select * from users"  # 적용할 MySQL 명령어를 만들어서 sql 객체에 할당하면 됨
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
    
def login():
    user = User(**request_user.dict())
        db_user = self.db.scalars(select(User).where(User.user_email == user.user_email)).first()
        print(f" dbUser {db_user}")
        if db_user is not None:
            if db_user.password == user.password:
                return db_user
            else:
                return 'password fail'
        else:
            print("해당 이메일이 없습니다.")
            return "email failure"    
'''