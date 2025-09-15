from fastapi import APIRouter

from typing import Annotated
from fastapi import Depends, APIRouter, status


from schemas.movies import Movie

from api.api_v1.movies.crud import storage
from api.api_v1.movies.dependecies import find_movie

router = APIRouter(
    prefix="/{slug}"
)

@router.get("/", response_model=Movie)
def get_movies_by_id(movie: Annotated[Movie, Depends(find_movie)]):
    return movie


@router.delete(
    "/",
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
