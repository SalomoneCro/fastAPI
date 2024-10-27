from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse

app = FastAPI()
app.title = "Primer Backend"

movies = [
    {
        "id": 1,
        "name": "The Big Short",
        "description": "Some random guys predict one of the biggest economic crashes of all time"
    },
    {
        "id": 2,
        "name": "American Pie",
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