from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
def add_number(a: int,b: int):
    sum=a+b
    difference=a-b
    product=a*b     
    division=a/b
    return {
        f"sum of {a}+{b}":f"{sum}",
        f"difference of {a}-{b}": f"{difference}",
        f"Product of {a}*{b}": f"{product}",
        f"Division of {a}/{b}": f"{ division}"      
    }