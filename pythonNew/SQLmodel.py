# # Objective: Understand how to define multiple models.
 
# # Task:
 
# # Define this Team model.
 
# # Modify create_db_and_tables() to include this.
 
# # Run the script and verify tables in DB Browser for SQLite.




# from sqlmodel import Field, SQLModel, Session, create_engine, select


# class Hero(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str
#     secret_name: str
#     age: int | None = None  # nullable column

# class Team(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str
#     member_count: int


# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# engine = create_engine(sqlite_url, echo=True)

# def create_heroes():
#     hero_1 = Hero(name = "Deadpool", secret_name = "Dave")
#     hero_2 = Hero(name = "SpiderMan", secret_name = "Peter Parker")
#     hero_3 = Hero(name = "IronMan", secret_name = "Tony", age = 33)
    
#     print("Before: ")
#     print("Hero 1: ", hero_1)
#     print("Hero 2: ", hero_2)
#     print("Hero 3: ", hero_3)
    
#     with Session(engine) as session:
#         session.add(hero_1)
#         session.add(hero_2)
#         session.add(hero_3)
        
#         print("After adding to the database:")
#         print("Hero 1:", hero_1)
#         print("Hero 2:", hero_2)
#         print("Hero 3:", hero_3)
    
#         session.commit()
        
#         print("After committing to the database: ")
#         print("Hero 1: ",hero_1)
#         print("Hero 2: ",hero_2.name)
#         print("Hero 3: ",hero_3.name)
        
#         session.refresh(hero_1)
#         session.refresh(hero_2)
#         session.refresh(hero_3)
        
#         print("After Refresh: ")
#         print("Hero 1: ", hero_1)
#         print("Hero 2: ", hero_2.name)
#         print("Hero 3: ", hero_3.name)
        
# def select_heroes():
#     with Session(engine) as session:
#         statement = select(Hero)
#         results = session.exec(statement)
#         # for hero in results:
#         #     print(hero)
        
#         heroes = session.exec(select(Hero)).all()

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

# def main():
#     create_db_and_tables()
#     create_heroes()

# if __name__ == "__main__":
#     main()

# from sqlmodel import Field, SQLModel, create_engine, Session, select, or_


# class Hero(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str
#     secret_name: str
#     age: int | None = None  # nullable column



# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# engine = create_engine(sqlite_url, echo=True) #echo=True will log all SQL statements to the console


# def create_heroes():
#     hero_1 = Hero(name="Batman", secret_name="Bruce Wayne")
#     hero_2 = Hero(name="Ironman", secret_name="Tony Stark", age=45)


#     with Session(engine) as session:
#         # Session is a temporary workspace for interacting with the database
#         # It allows you to add, update, delete, and query data
#         session.add(hero_1)
#         session.add(hero_2)

#         session.commit()
#         #with Session(engine) as session: # This is a context manager that automatically closes the session when done

#         session.refresh(hero_1)
#         session.refresh(hero_2)
#         print(hero_1)
#         print(hero_2)
#         #refresh() is used to update the instance with the latest data from the database


# def select_heroes():
#     with Session(engine) as session:
#             # --------- READ -----------
#             # statement = select(Hero)
#             # results = session.exec(statement)
#             # for hero in results:
#             #      print(hero)
#             # heroes = results.all()#returns a list of all rows
#             # print(heroes)

#             # ---------- FILTER -----------
#             # statement = select(Hero).where(Hero.name == "Ironman", Hero.age == "45") #AND condition
#             statement = select(Hero).where(or_(Hero.name == "Ironman", Hero.name == "Batman")) #AND condition
#             results = session.exec(statement)
#             for hero in results:
#                  print(hero)

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

# def main():
#     create_db_and_tables()
#     select_heroes()

# if __name__ == "__main__":
#     main()

from sqlmodel import Field, SQLModel, create_engine, Session, select, or_


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True) #ix_hero_name   [ix_tablename_columnname]
    secret_name: str
    age: int | None = Field(default=None, index=True)  # nullable column



sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True) #echo=True will log all SQL statements to the console


def create_heroes():
    hero_1 = Hero(name="Batman", secret_name="Bruce Wayne")
    hero_2 = Hero(name="Ironman", secret_name="Tony Stark", age=45)
    hero_3 = Hero(name="Superman", secret_name="Clark Kent", age=35)
    hero_4 = Hero(name="Spiderman", secret_name="Peter Parker", age=18)
    hero_5 = Hero(name="Wonder Woman", secret_name="Diana Prince")
    hero_6 = Hero(name="Black Panther", secret_name="T'Challa", age=40)
    hero_7 = Hero(name="Doctor Strange", secret_name="Stephen Strange", age=42)
    hero_8 = Hero(name="Captain Marvel", secret_name="Carol Danvers")


    with Session(engine) as session:
        #with Session(engine) as session: # This is a context manager that automatically closes the session when done
        # Session is a temporary workspace for interacting with the database
        # It allows you to add, update, delete, and query data
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.add(hero_4)
        session.add(hero_5)
        session.add(hero_6)
        session.add(hero_7)
        session.add(hero_8)

        session.commit() # commit() will save the changes to the database

        session.refresh(hero_1) #refresh() is used to update the instance with the latest data from the database
        session.refresh(hero_2)
        print(hero_1)
        print(hero_2)
        
def select_heroes():
    with Session(engine) as session:
            # --------- READ -----------
            # statement = select(Hero)
            # results = session.exec(statement)
            # for hero in results:
            #      print(hero)
            # heroes = results.all()#returns a list of all rows
            # print(heroes)

            # ---------- FILTER -----------
            # statement = select(Hero).where(Hero.name == "Ironman", Hero.age == "45") #AND condition
            # statement = select(Hero).where(or_(Hero.name == "Ironman", Hero.name == "Batman")) #OR condition
            # results = session.exec(statement)
            # for hero in results:
            #      print(hero)

            # ------------------ FIRST AND ONE ------------------                                
            # one() will return the first row of the result set, and raise an error if there are no rows or more than one row
            # first() will return the first row of the result set, and return None if there are no rows
            statement = select(Hero).where(Hero.name == "Superman") 
            result = session.exec(statement)
            hero = result.first() #result.one()
            print('Hero : ', hero)

            # ------------------- OFFSET AND LIMIT ------------------
            # offset() will skip the first n rows of the result set
            # limit() will limit the result set to n rows
            # statement = select(Hero).offset(3).limit(3)
            # results = session.exec(statement)
            # heroes = results.all()
            # print('Heroes : ', heroes)



#---------- UPDATE --------------
def update_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Superman")
        results  = session.exec(statement)
        hero_1 = results.one()
     

        statement = select(Hero).where(Hero.name == "Captain Marvel")
        results  = session.exec(statement)
        hero_2 = results.one()

        #before updation
        print("Hero : ", hero_1)
        print("Hero : ", hero_2)

        #updation
        hero_1.name = "Superman-Teenager"
        hero_2.name = "Captain Canada"
        session.add(hero_1)
        session.add(hero_2)
        session.commit()
        session.refresh(hero_1)
        session.refresh(hero_2)

        #after updation
        print(" Updated Hero : ", hero_1)
        print(" Updated Hero : ", hero_2)

def delete_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Superman - Teenager")
        results  = session.exec(statement)
        hero_1 = results.one()
        
        #before deletion
        print("Hero : ", hero_1)


        #deletion
        session.delete(hero_1)
        session.commit()   #session.refresh(hero_1) #refresh() will raise an error since the object is deleted

        #after deletion
        print("Deleted Hero : ", hero_1)

       
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def addDataWithParams(name:str,age:int|None,secret:str):
    hero_temp=Hero(name=name,secret_name=secret,age=age)

    with Session(engine) as session:
        session.add(hero_temp)
        session.commit()
        session.refresh(hero_temp)
        print("New item added:",hero_temp)


def main():
    # create_db_and_tables()
    # create_heroes() 
    update_heroes() 
    delete_heroes()
    select_heroes()
    addDataWithParams("Nan",-12,"none")

if __name__ == "__main__":
    main()