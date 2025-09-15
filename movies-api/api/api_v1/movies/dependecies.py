from fastapi import HTTPException, status

from schemas.movies import Movie
from .crud import storage


def find_movie(slug: str) -> Movie | None:
    movie: Movie | None = storage.get_by_slug(slug=slug)
    if movie:
        return movie
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        f"Movie {slug!r} not found",
    )
