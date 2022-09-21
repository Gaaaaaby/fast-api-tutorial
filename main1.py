from fastapi import FastAPI
from enum import Enum
app = FastAPI()

#path parameters 
#the variable item_id type will be int 
#pydantic --for data validation 

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

#predefined values -- use Enum 
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

#the model_name will be referenced to the class ModelName, and
#will be chose depending on the type of model 

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

#path parameters containing paths 

#a path operation with a path /files/{files_path}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}