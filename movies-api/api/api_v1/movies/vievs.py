from typing import Annotated
from fastapi import Depends, APIRouter

from schemas.movies import Movie

from .crud import MOVIES
from .dependecies import find_movie

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get("/", response_model=list[Movie])
def get_all_movies():
    return MOVIES


@router.get("/{movie_id}", response_model=Movie)
def get_movies_by_id(movie: Annotated[Movie, Depends(find_movie)]):
    return movie
