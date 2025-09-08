from typing import Annotated
from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str
    year: int


class MovieCreate(BaseModel):
    """
    Модель для создания фильма.
    """

    title: str
    description: str
    genre: str
    year: int
