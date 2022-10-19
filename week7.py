"""
1
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    html_content="<h2>Hello, my name is Zhalgas!</h2>"
    return HTMLResponse(content=html_content)
"""
"""
2
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello my name is Zhalgas"}
    
2.2
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
defroot():
    return {"message": "Hello!"}
    
@app.get("/about")
def about():
    return {"message": "About"}
"""
"""
3.1
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/")
defroot():
    data = {"message": "Hello World"}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data)
3.2
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app= FastAPI()

@app.get("/")

def root():
    return JSONResponse(content={"message": "Hello World"})
3.3
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse, HTMLResponse

app= FastAPI()

@app.get("/text", response_class = plain text response)
def root_text():
    return "Hello World!"

@app.get("/html", response_class = HTMLResponse)
def root_html():
    return "<h2>Hello World!</h2>"
"""
"""
4
import mimetypes
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index.html",
                        filename="mainpage.html",
                        media_type="application/octet-stream")
"""
"""
5
from fastapi import FastAPI, Path

app= FastAPI()

@app.get("/users/{name}/{age}")

def users(name:str = Path(min_length=3, max_length=twenty),
age:int = Path(ge=eighteen,lt=111)):
    return {"name": name, "age": age}
"""

"""
6
from fastapi import FastAPI, Path, Query

app= FastAPI()

@app.get("/users/{name}")
def users(name:str = Path(min_length=3, max_length=twenty),
age:int = Query(ge=eighteen,lt=111)):
    return {"name": name, "age": age}
"""
"""
7
from fastapi import FastAPI, Response, Path

app= FastAPI()

@app.get("/users/{id}", status_code=200)
def users(response: Response, id: int = path()):
    if id < 1:
        response.status_code = 400
    return {"message": "Incorrect Data"}
    return {"message": f"Id = {id}"}
"""
"""
8
importmimetypes

fromfastapi import FastAPI
fromfastapi.responses import RedirectResponse, PlainTextResponse

app=FastAPI()

@app.get("/old")
defold():
    returnRedirectResponse("/new", status_code=302)

@app.get("/new")
defnew():
    returnPlainTextResponse("New Page")
"""
"""
9
fromfastapi import FastAPI
fromfastapi.staticfiles import StaticFiles

app=FastAPI()

app.mount("/", StaticFiles(directory="public", html=True))
"""
"""
10
from fastapi import FastAPI, Body
from fastapi.responses import FileResponse

app= FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index.html")

@app.post("/hello")
def hello(name:str = Body(embed=True, min_length=3, max_length=twenty),
age:int = Body(embed=True,ge=eighteen,lt=111)):
    return {"message": f"{name}, your age is {age}"}
"""
"""
11
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import basemodel

class Company(BaseModel):
    name:str
    
class Person(BaseModel):
    name:str
    company: Company
    
app= FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index.html")
    
@app.post("/hello")
def hello(person: Person):
    return {"message": f"{person.name} ({person.company.name})"}
    
    
const response = await fetch("/hello", {
method: "POST",
headers: { "Accept": "application/json", "Content-Type": "application/json" },
body: JSON.stringify({
name: "Tom",
company: {name: "Google"}
})
"""

"""