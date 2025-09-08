from typing import Annotated
from fastapi import Depends, APIRouter, status, Form

from random import randint


from schemas.movies import Movie, MovieCreate

from .crud import MOVIES
from .dependecies import find_movie

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get("/", response_model=list[Movie])
def get_all_movies():
    return MOVIES


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(movie: MovieCreate):
    return Movie(
        id=randint(4, 10),
        **movie.model_dump(),
    )


@router.get("/{movie_id}", response_model=Movie)
def get_movies_by_id(movie: Annotated[Movie, Depends(find_movie)]):
    return movie
