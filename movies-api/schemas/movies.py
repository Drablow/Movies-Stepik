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
