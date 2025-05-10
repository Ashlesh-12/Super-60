from sqlmodel import SQLModel, Field, Session, select, create_engine
from fastapi import FastAPI, HTTPException

class Hero(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

sql_file_name = "database.db"
sqlite_url = f"sqlite:///{sql_file_name}"
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    print("Database and tables created.")

@app.post("/heroes/")
def create_hero(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
    return hero

@app.get("/heroes/")
def read_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes

@app.put("/heroes/{hero_id}/")
def update_hero(hero_id: int, hero: Hero):
    with Session(engine) as session:
        db_hero = session.get(Hero, hero_id)
        if not db_hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        db_hero.name = hero.name
        db_hero.secret_name = hero.secret_name
        db_hero.age = hero.age
        session.commit()
        session.refresh(db_hero)
    return db_hero