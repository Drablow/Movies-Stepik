from typing import Annotated
from pydantic import BaseModel


class MovieBase(BaseModel):
    slug: str
    title: str
    description: str
    genre: str
    year: int


class Movie(MovieBase):
    slug: str
    title: str
    description: str
    genre: str
    year: int
    notes: str = ""


class MovieCreate(MovieBase):
    """
    Модель для создания фильма.
    """

    slug: str
    title: str
    description: str
    genre: str
    year: int


class MovieUpdate(MovieBase):
    """
    Модель для обновления информации о фильме
    """

    title: str
    description: str
    genre: str
    year: int


class MoviePartialUpdate(MovieBase):
    title: str | None = None
    description: str | None = None
    genre: str | None = None
    year: int | None = None


class MovieRead(MovieBase):
    slug: str
    title: str
    description: str
    genre: str
    year: int
