from typing import Annotated
from pydantic import BaseModel


class Movie(BaseModel):
    slug: str
    title: str
    description: str
    genre: str
    year: int


class MovieCreate(BaseModel):
    """
    Модель для создания фильма.
    """

    slug: str
    title: str
    description: str
    genre: str
    year: int


class MovieUpdate(BaseModel):
    """
    Модель для обновления информации о фильме
    """

    title: str
    description: str
    genre: str
    year: int


class MoviePartialUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    genre: str | None = None
    year: int | None = None
