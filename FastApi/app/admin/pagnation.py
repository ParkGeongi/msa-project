
from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from app.admin.security import myuuid
from app.admin.utils import between_random_date
from app.cruds.user import UserCrud
from app.database import get_db, SessionLocal
from app.models.user import User
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from faker import Faker

from app.schemas.user import UserFaker

router = APIRouter()


@router.get("/page/{request_page}")
def pagination(request_page: int ,db: Session = Depends(get_db)):
    row_cnt = UserCrud(db).count_all_users()
    page_size = 10
    response_page = request_page - 1  # 넘겨받은 page번호를 인덱스 값으로 전환
    t = row_cnt // page_size
    t2 = row_cnt % page_size
    page_cnt = t if (t2 == 0) else t + 1
    t3 = page_cnt // page_size
    block_size = 10
    t4 = page_cnt % block_size
    block_cnt = t3 if (t4 == 0) else t3 + 1
    start_row_per_page = page_size * (response_page)
    response_block = (response_page) // block_size
    end_row_per_page = start_row_per_page + (page_size - 1) if request_page != page_cnt else row_cnt - 1
    start_page_per_block = response_block * block_size
    end_page_per_block = start_page_per_block + (block_size - 1) if response_block != (block_cnt - 1) else page_cnt - 1

    print("### 테스트 ### ")
    print(row_cnt)
    print(f"start_row_per_page ={start_row_per_page}")
    print(f"end_row_per_page ={end_row_per_page}")
    print(f"start_page_per_block ={start_page_per_block}")
    print(f"end_page_per_block ={end_page_per_block}")

    return {
        "start_row_per_page": start_row_per_page,
        "end_row_per_page": end_row_per_page,
        "start_page_per_block": start_page_per_block,
        "end_page_per_block": end_page_per_block,
        "response_block": response_block
    }



@router.get("/many")
def insert_many(db: Session = Depends(get_db)):
    faker = Faker('ko_KR')

    [UserCrud(db).add_user_for_faker(UserFaker(
        email=faker.email(),
        password="11aa",
        username=faker.name(),
        birth=between_random_date(),
        address=faker.city())) for i in range(10)]

'''
    [print(UserFaker(
        email=faker.email(),
        password="123a",
        username=faker.name(),
        birth=between_random_date(),
        address=faker.city())) for i in range(5)]
'''




'''
총 count -> 13
| 현재 페이지 1
api       |   row start 0
api       |   row end 4
api       |   page start 0
api       |   page end 2
api       |  count is 13

  | 현재 페이지 2
api       |   row start 5
api       |   row end 9
api       |   page start 0
api       |   page end 2
api       |  count is 13

  | 현재 페이지 3
api       |   row start 10
api       |   row end 12
api       |   page start 0
api       |   page end 2
api       |  count is 13

'''
