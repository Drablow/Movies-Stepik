from fastapi import HTTPException, status

from schemas.movies import Movie
from .crud import MOVIES


def find_movie(slug: str) -> Movie | None:
    for movie in MOVIES:
        if movie.slug == slug:
            return movie
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        f"Movie {slug!r} not found",
    )
