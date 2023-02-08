from fastapi import APIRouter
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from app.services.chatbot.kakao_chatbot import KakaoChatbot
from app.services.chatbot.kogpt2 import Kogpt2

router = APIRouter()
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>챗봇</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>보내기</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>

            var ws = new WebSocket("ws://localhost:8000/chatbot/sk-kogpt2");
            
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

@router.websocket("/sk-kogpt2")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        output = Kogpt2().test2(data)
        await websocket.send_text(f"보낸 메세지: {data}")
        await websocket.send_text(f"KoGPT2 챗봇의 답변: {output}")

@router.websocket("/kakao-chatbot")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        output = KakaoChatbot().chatbot(msg = data)
        await websocket.send_text(f"보낸 메세지: {data}")
        await websocket.send_text(f"카카오 챗봇의 답변: {output}")