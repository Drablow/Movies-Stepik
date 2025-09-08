from fastapi import HTTPException, status

from schemas.movies import Movie
from .crud import MOVIES


def find_movie(movie_id: int) -> Movie | None:
    for movie in MOVIES:
        if movie.id == movie_id:
            return movie
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        f"Movie {movie_id!r} not found",
    )
