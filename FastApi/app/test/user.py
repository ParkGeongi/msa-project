from fastapi import APIRouter
from starlette.responses import HTMLResponse

router = APIRouter()

@router.get("/users/login")
async def login():
    return HTMLResponse(content="""
    <form action="http://localhost:8000/users/login" method="post" style="width: 30px">
    <div>
      <label for="email"><b>email</b></label>
      <input type="text" placeholder="Enter Username" name="email" required>
  
      <label for="password"><b>Password</b></label>
      <input type="text" placeholder="Enter Password" name="password" required>
  
      <button type="submit">Login</button>
      
    </div>
  
    <div class="container" style="background-color:#f1f1f1">
      <button type="button" class="cancelbtn">Cancel</button>
    </div>
  </form>
    """)