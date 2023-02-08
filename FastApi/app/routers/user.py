from fastapi import APIRouter, Depends, WebSocket
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse
from fastapi_pagination import Page, paginate, add_pagination, LimitOffsetPage, Params


from app.admin.security import get_hashed_password, generate_token

from app.admin.utils import current_time, paging
from app.cruds.user import UserCrud
from app.models.user import User
from app.schemas.user import UserDTO, UserUpdate, UserGet, ChatbotDTO
from app.database import get_db
from app.services import chatbot
from app.services.chatbot.kakao_chatbot import KakaoChatbot, Chatbot
from app.services.chatbot.kogpt2 import Kogpt2
from fastapi.responses import HTMLResponse
router = APIRouter()


## C
@router.post("/register",status_code=201)
async def register_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200, content=dict(
        msg=UserCrud(db).add_user(request_user=dto)))

@router.post("/login", status_code=200)
async def login_user(dto:UserDTO ,db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(msg=UserCrud(db).login_user(request_user =dto)))


@router.post("/logout", status_code=200)
async def logout_user(dto:UserDTO ,db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(msg=UserCrud(db).logout_user(request_user =dto)))


@router.get("/load")
async def load_user(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=jsonable_encoder(
                                UserCrud(db).find_user_by_token(request_user=dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.put("/modify")
async def modify_user(dto:UserUpdate ,db: Session = Depends(get_db)):
    if UserCrud(db).match_token_for_update(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=UserCrud(db).update_user(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.put("/modify/password")
async def modify_password_by_id(dto:UserDTO ,db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(msg=UserCrud(db).update_password(request_user=dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)

@router.delete("/remove")
async def remove_user(dto:UserDTO ,db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,content=dict(msg=UserCrud(db).delete_user(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


## Q
@router.get("/page/{page}",response_model=Page[UserGet])
async def get_users_per_page(page:int,db: Session = Depends(get_db)):
    default_size = 10
    page_result = paginate(UserCrud(db).find_all_users(), Params(page=page, size=default_size))
    print(f'page_result{type(page_result)}')
    count =UserCrud(db).count_all_users()
    page_info = paging(request_page=page,row_cnt=count)

    dc = {'page_info':page_info,"users":page_result}
    print(f"############################################{dc}")
    return JSONResponse(status_code=200,content=jsonable_encoder(dc))

@router.get("/page/{page}/size/{size}",response_model=Page[UserGet])
async def get_users_chaged_size(page:int,size:int ,db: Session = Depends(get_db)):
    page_result = paginate(UserCrud(db).find_all_users(), Params(page=page, size=size))
    print(f'page_result{page_result}')
    return JSONResponse(status_code=200,content=jsonable_encoder(page_result))


@router.get("/job")
async def search_users_by_job(dto:UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(
                            UserCrud(db).find_users_by_job(dto)))

@router.get("/id/{userid}")
async def get_user_by_userid(userid:str,dto: UserDTO ,db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    result = user_crud.find_user_by_id(request_user=dto)
    return result

@router.get("/chatbot")
async def get_user_by_userid(dto: Chatbot ,db: Session = Depends(get_db)):
    msg = Kogpt2().test(request_user=dto)
    #msg = Kogpt2().path()

    return JSONResponse(status_code=200,content=dict(msg=msg))

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/users/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""
@router.get("/")
async def get():
    return HTMLResponse(html)
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        output = Kogpt2().test2(data)
        await websocket.send_text(f"보낸 메세지: {data}")
        await websocket.send_text(f"챗봇의 답변: {output}")


'''
@router.get("/2")
async def get_users_legacy():
    return dao.find_users_legacy()
    
@router.get("/")
async def get_users():
    return dao.find_users()

'''