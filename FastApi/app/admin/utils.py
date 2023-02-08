from datetime import datetime
import pytz

from app.database import get_db
from fastapi import  Depends
from sqlalchemy.orm import Session

def current_time():
    tz = pytz.timezone('Asia/Seoul')
    cur_time = datetime.now(tz)
    current_time = cur_time.strftime("%H:%M:%S")
    return f"{current_time}"
def current_time1():
    return f"{datetime.now(pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')}"
def utc_seoul():
    return datetime.now(pytz.timezone('Asia/Seoul'))

from random import randrange
from datetime import timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def between_random_date():
    d1 = datetime.strptime('1988-1-1', '%Y-%m-%d')
    d2 = datetime.strptime('2005-12-31', '%Y-%m-%d')
    target = str(random_date(d1, d2))
    return target.split()[0]

def paging(request_page: int, row_cnt:int):

    page_size = 10
    response_page = request_page - 1  # 넘겨받은 page번호를 인덱스 값으로 전환
    page_cnt = row_cnt // page_size if (row_cnt % page_size == 0) else row_cnt // page_size + 1
    block_size = 10
    block_cnt = page_cnt // page_size if (page_cnt % block_size == 0) else page_cnt // page_size + 1
    start_row_per_page = page_size * (response_page)
    response_block = (response_page) // block_size
    end_row_per_page = start_row_per_page + (page_size - 1) if request_page != page_cnt else row_cnt - 1
    start_page_per_block = response_block * block_size
    end_page_per_block = start_page_per_block + (block_size - 1) if response_block != (block_cnt - 1) else page_cnt - 1

    prev_arrow = 0 if request_page == 1 else 1

    next_arrow = 0 if request_page == page_cnt else 1

    print("### 테스트 ### ")
    print(row_cnt)
    print(page_cnt)
    print(f"start_row_per_page ={start_row_per_page}")
    print(f"end_row_per_page ={end_row_per_page}")
    print(f"start_page_per_block ={start_page_per_block}")
    print(f"end_page_per_block ={end_page_per_block}")

    return {
        "row_cnt" : row_cnt,
        "start_row_per_page": start_row_per_page,
        "end_row_per_page": end_row_per_page,
        "start_page_per_block": start_page_per_block,
        "end_page_per_block": end_page_per_block,
        "request_page":request_page,
        "prev_arrow" : prev_arrow,
        "next_arrow" : next_arrow
    }
