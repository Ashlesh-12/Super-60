from fastapi import FastAPI 

app = FastAPI()

@app.get("/") # here we can write anything but in web also we have to change the name.
async def root():
    return {"message": "Hello World"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello Students!"}

@app.get("/Introduce")
def say_introduce(name: str):
    return {"message": f"Hello I am {name}!"}

@app.get("/users/{user_id}/items")
def get_user_items(user_id:int):
    pass

@app.post("/user/{id}")
def Post(id: int, username: str, email: str):
    return {
        "id": id,
        "username": username,
        "email": email
    }

 