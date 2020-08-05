from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from database import database, notes, Note, NoteIn, notes
from uvicorn import run
from typing import List
import requests
import os

# PATH :
base_path = os.path.abspath(os.path.curdir)
current_wd = 'Popsmoke'
# TEMPLATES :
templates = Jinja2Templates(directory=f"{current_wd}/resources/templates")

# API :
api = FastAPI(debug=True)
api.mount("/static", StaticFiles(directory="Popsmoke/resources/static"), name="static")

# ROUTES :
@api.get('/')
async def root(request:Request):    
    tem = templates.get_template('index.html')
    return templates.TemplateResponse(tem, {'request':request})
    # return {"code":"hello world"}

@api.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@api.get('/items_bis/{id}')
async def load_item(request: Request, id: str):
    test_list = {'print_hello':print_hello}
    for i in test_list.keys():
        num = id
        return test_list[i](num)


@api.on_event("startup")
async def startup():
    await database.connect()


@api.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@api.get("/notes/{id}", response_model=List[Note])
async def read_notes(request:Request, id:str):
    query = notes.select()
    note = await database.fetch_all(query)
    return templates.TemplateResponse("notes.html", {"request": request, "id": id, "text":note})

@api.post('/notes-post/')
async def bridge(request:Request, text:str = Form(...), completed:bool = Form(default=False)):
    # SQL INSERTION => INSERT DATA
    note = {"text":text, "completed":completed}
    query = notes.insert().values(text=note['text'], completed=note['completed'])
    last_record_id = await database.execute(query)
    return templates.TemplateResponse("index.html", {"request":request, "text": text})


# FUNCTIONS :
list_des = {'1':'lot numero 1 very good','2':'lot numero 2 very bad'}

def print_hello(num:str):
    print('hello')
    return list_des[num]

if __name__ == "__main__":
    run(api)