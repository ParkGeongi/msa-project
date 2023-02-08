
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, orm
from sqlalchemy.orm import sessionmaker, scoped_session
from app.env import DB_URL

engine = create_engine(DB_URL, echo=True, pool_pre_ping=True)
SessionLocal = scoped_session(
    sessionmaker(autocommit = False, autoflush=False, bind=engine)
)
Base = declarative_base()
engine = create_engine(DB_URL, echo=True, pool_pre_ping=True)
Base.query = SessionLocal.query_property()


async def get_db():
    global db
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

async def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise e
'''
pymysql.install_as_MySQLdb()
conn = pymysql.connect(host=DB_HOST, port=PORT, user=DB_USER, password=DB_PASSWORD, db=DB_NAME, charset=CHARSET)
'''
'''
class engineconn(object):

    def __init__(self):
        self.engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{PORT}/{DB_NAME}?charset=utf8mb4",future=True)
#172.17.0.1 -> docker host host.docker.internal
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.close()
        return session

    def connection(self):
        conn = self.engine.connect()
        conn.close()
        return conn
'''


