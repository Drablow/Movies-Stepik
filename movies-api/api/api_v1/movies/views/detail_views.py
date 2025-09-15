from fastapi import APIRouter

from typing import Annotated
from fastapi import Depends, APIRouter, status


from schemas.movies import Movie, MovieUpdate, MoviePartialUpdate

from api.api_v1.movies.crud import storage
from api.api_v1.movies.dependecies import find_movie

router = APIRouter(prefix="/{slug}")

MovieBySlug = Annotated[
    Movie,
    Depends(find_movie),
]


@router.get("/", response_model=Movie)
def get_movies_by_id(movie: MovieBySlug):
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
def delete_movie(movie: MovieBySlug) -> None:
    storage.delete(movie=movie)


@router.put("/", response_model=Movie)
def update_movie_details(movie: MovieBySlug, movie_in: MovieUpdate):
    return storage.update(movie=movie, movie_in=movie_in)


@router.patch("/", response_model=Movie)
def update_movie_detail_partial(
    movie: MovieBySlug,
    movie_in: MoviePartialUpdate,
) -> Movie:
    return storage.update_partial(
        movie=movie,
        movie_in=movie_in,
    )
