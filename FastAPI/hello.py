from fastapi import FastAPI 
from Models import Book, BookResponse

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

@app.post("/book")
async def create_book(book: Book):
    return {
        "Message": "Book Created",
        "book": book
    }

@app.get("/allbooks", response_model=list[BookResponse])
async def read_all_books():
    return [
        {"id":1,"title": "Book1", "author": "Author1"},
        {"id":2,"title": "Book2", "author": "Author2"}
    ]