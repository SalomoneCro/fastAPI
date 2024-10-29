from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse

app = FastAPI()
app.title = "Primer Backend"

movies = [
    {
        "id": 1,
        "name": "The Big Short",
        "category" : "Documentary",
        "description": "Some random guys predict one of the biggest economic crashes of all time"
    },
    {
        "id": 2,
        "name": "American Pie",
        "category": "Comedy",
        "description": "Frat parties, alcohol, sex, all a man can ask"
    }
]

@app.get('/', tags=["home"])
def message():
    return HTMLResponse('<h1>Que pasa durooo</h1>')

@app.get('/movies', tags=["movies"])
def get_movies():
    return JSONResponse(content=movies)

@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return "No se encontro la pelicula"

@app.get("/movies/", tags=["movies"])
def get_movies_category(category: str):
    return [i for i in movies if i["category"] == category]

@app.post("/movies/add", tags=['movies'])
def add_movie(id: int = Body(),
              name: str = Body(),
              category: str = Body(),
              description: str = Body()
):
    movies.append({
        "id": id,
        "name": name,
        "category": category,
        "description": description,
    })
    return movies

app.
    