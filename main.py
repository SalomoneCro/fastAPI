from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title = "Primer Backend"

class Movie(BaseModel):
    id: Optional[int] = None
    name : str
    category: str
    description: str

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
def add_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put("/movies/{id}", tags=['movies'])
def modify_movie(id: int, movie:Movie):
    for item in movies:
        if item['id'] == id:
            item['name'] = movie.name,
            item['category'] = movie.category,
            item['description'] = movie.description
            return movies
    return "No se encontró pelicula con el id dado"

@app.delete("/movies/{id}", tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return movies
    return "No se encontró pelicula con el id dado"

    