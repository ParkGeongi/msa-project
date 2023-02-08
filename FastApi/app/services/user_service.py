from app.models.user import User

class UserService:
    def login(self):
        user = User()
        print(f'리액트에서 보낸 email:{user.get_email()}')
        print(f'리액트에서 보낸 email:{user.get_password()}')
