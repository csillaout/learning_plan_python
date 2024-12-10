import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Fruit(BaseModel):
    name: str

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory_db ={"fruits":{}}

@app.get("/fruits")
def get_fruits():
    # Convert the dictionary into a list of objects
    return [{"name": name, "count": count} for name, count in memory_db["fruits"].items()]

@app.post("/fruits")
def add_fruit(fruit: Fruit):
    # Increment the count for the fruit
    if fruit.name in memory_db["fruits"]:
        memory_db["fruits"][fruit.name] += 1
    else:
        memory_db["fruits"][fruit.name] = 1
    return {"name": fruit.name, "count": memory_db["fruits"][fruit.name]}

@app.delete("/fruits/{fruit_name}")
def delete_fruit(fruit_name: str):
    # Decrement the count for the fruit
    if fruit_name in memory_db["fruits"]:
        if memory_db["fruits"][fruit_name] > 1:
            memory_db["fruits"][fruit_name] -= 1
        else:
            del memory_db["fruits"][fruit_name]
        return {"name": fruit_name, "count": memory_db["fruits"].get(fruit_name, 0)}
    return {"error": f"{fruit_name} not found"}, 404

#this runs the app for us
if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)