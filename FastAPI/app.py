from typing import Annotated
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_user_db = {
    "user1":{
        "username": "user2",
        "email": "e@email.com",
        "password": "Fakesecret",
        "disabled": "False"
    },
    "user2": {
        "username": "user2",
        "email": "e1@email.com",
        "password": "Fakesecret1",
        "disabled": "True"
    }
}

app = FastAPI()

def fake_hash(password: str):
    return "Fake" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

class User(BaseModel):
    username: str
    email: str | None = None
    disabled: bool | None = None
    
class UserInDB(User):
    password: str
    
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    
def fake_decode(token):
    user = get_user(fake_user_db, token)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode(token = token)
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "InValid Auth")
    
    return user

async def get_currentActiveUser(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code = 400, detail = "Disabled")
    return current_user

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_user_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400)
    user = UserInDB(**user_dict)
    hashedPassword = fake_hash(form_data.password)
    if not hashedPassword == user.password:
        raise HTTPException(status_code=400, detail="User password not found")
    return {"access_token": user.username, "token_type": "bearer"} 

@app.get("/user/me")
async def read(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user