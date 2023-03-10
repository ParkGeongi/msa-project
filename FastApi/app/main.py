import os
import sys
from fastapi import FastAPI, APIRouter, Depends, HTTPException, WebSocket
from fastapi_pagination import add_pagination
from fastapi_sqlalchemy import DBSessionMiddleware

from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from app.admin.utils import current_time, current_time1
from app.models.user import User
from app.routers.user import router as user_router
from app.routers.article import router as post_router
from app.admin.pagnation import router as page_router
from app.database import init_db
from app.env import DB_URL
import logging
from fastapi.security import APIKeyHeader
from .test.user import router as test_router
from mangum import Mangum
from .routers.chatbot import router as chatbot_router
API_TOKEN = 'SECRET_API_TOKEN'
api_key_header = APIKeyHeader(name="Token")

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
print(f" ################ app.main Started At {current_time()} ################# ")

router = APIRouter()
router.include_router(user_router, prefix="/users",tags=["users"])
router.include_router(post_router, prefix="/articles",tags=["articles"])
router.include_router(test_router,prefix='/test',tags=['test'])
router.include_router(page_router,prefix='/pagination',tags=['pagnation'])

router.include_router(chatbot_router,prefix='/chatbot',tags=['chatbot'])


app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
#Base.query = db_session.query_property()
# Dependency
add_pagination(app)
@app.on_event('startup')
async def on_startup():
    await init_db()

@app.get("/progected-router")
async def protected_route(token: str = Depends(api_key_header)):
    if token !=API_TOKEN:
        raise HTTPException(status_code=403)
    return{"?????????":  "???????????????."}

@app.get("/")
async def home():
    return HTMLResponse(content=f"""
    <body>
    <div style="width: 400px; margin: 50 auto;">
         <h3> {current_time1()} </h3>
        <h1>?????? ?????? ?????? ??? ?????????.</h1>
        <h3>10:10:10</h3>
    </div>
</body>
      
    """
)

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
@app.get("/no-match-token")
async def no_match_token():
    return {"message": f"?????? ??????????????? ???????????????."}

'''
app.add_middleware(DBSessionMiddleware, db_url=DATABASE)
@app.get("/")
async def root():
    print(" -- 1 -- ")
    # tp = pymysql_method()
    tp = sqlalchemy_method()
    print(" -- 2 -- ")
    return {"message": tp}


def pymysql_method():
    import pymysql

    HOSTNAME = 'host.docker.internal'
    PORT = 3306
    USERNAME = 'root'
    PASSWORD = 'root'
    DATABASE = 'mydb'
    CHARSET = 'utf8'

    conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)
    cursor = conn.cursor()  # MySQL??? ??????
    sql = "select * from users"  # ????????? MySQL ???????????? ???????????? sql ????????? ???????????? ???
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(f"data: {data}")
    print(f"type is {type(result)}")
    # conn.close()  # ?????? ????????? ?????? ????????? ??????
    return result

def sqlalchemy_method():
    import pymysql
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    pymysql.install_as_MySQLdb()
    engine = create_engine("mysql+pymysql://root:root@host.docker.internal:3306/mydb", encoding="utf-8", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(User).all()
    print(f"type is {type(result)}")
    for row in result:
        print(f"data : {row}")
    return result
'''
##handler = Mangum(app)