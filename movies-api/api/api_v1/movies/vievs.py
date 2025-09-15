from typing import Annotated
from fastapi import Depends, APIRouter, status


from schemas.movies import Movie, MovieCreate

from .crud import storage
from .dependecies import find_movie

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get("/", response_model=list[Movie])
def get_all_movies() -> list[Movie]:
    return storage.get()


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(movie: MovieCreate):
    return storage.create(movie)


@router.get("/{movie_id}", response_model=Movie)
def get_movies_by_id(movie: Annotated[Movie, Depends(find_movie)]):
    return movie


@router.delete(
    "/{slug}/",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Movie not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Movie 'name movie' not found",
                    },
                },
            },
        },
    },
)
def delete_movie(movie_slug: Annotated[Movie, Depends(find_movie)]) -> None:
    storage.delete(movie=movie_slug)
