from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse, RedirectResponse

from sqlalchemy.orm import Session

from app.admin.utils import current_time
from app.cruds.article import ArticleCrud
from app.cruds.user import UserCrud
from app.schemas.article import ArticleDTO
from app.database import get_db
from app.schemas.user import UserDTO

router = APIRouter()


@router.post("/write",status_code=201)
async def wrtie(dto: ArticleDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200, content=dict(
    msg=ArticleCrud(db).add_article(request_article=dto)))


@router.put("/modify/id/{userid}",status_code=200)
async def modify_article(userid:str,dto:ArticleDTO ,db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    print(f" 업데이트에 진입한 시간: {current_time()} ")
    result = article_crud.update_article_by_userid(request_article=dto)
    if result == 'success':
        return {'data', f'update {userid} success'}
    return JSONResponse(status_code=404, content=dict(msg="해당 아이디가 없습니다."))

@router.delete("/remove/title/{title}")
async def remove_article(title:str,dto:ArticleDTO ,db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    print(f" 삭제에 진입한 시간: {current_time()} ")
    result = article_crud.delete_article_by_title(request_article=dto)
    if result =='success':
        return {'data':f'delete {title} success'}
    else:
        return JSONResponse(status_code=404, content=dict(msg="타이틀이 없습니다."))

## Q
@router.get("/page/{page}")
async def get_articles(page:int,db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    result = article_crud.find_all_articles(page)
    return result

@router.get("/search/id/{userid}/page/{page}")
async def search_article_by_userid(page:int,dto:ArticleDTO,db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    result = article_crud.find_articles_by_userid(page,request_article=dto)
    return result
@router.get("/seq/{seq}")
async def get_article_by_seq(seq: int,dto:ArticleDTO,db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    print(f' 글 번호 : {seq}')
    result = article_crud.find_article_by_seq(request_article=dto)
    return result