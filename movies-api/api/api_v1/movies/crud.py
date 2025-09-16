from schemas.movies import Movie, MovieCreate, MovieUpdate, MoviePartialUpdate
from pydantic import BaseModel, ValidationError

from core.config import MOVIE_STORAGE_FILEPATH


class MovieStorage(BaseModel):
    slug_to_movie: dict[str, Movie] = {}

    def save_state(self) -> None:
        MOVIE_STORAGE_FILEPATH.write_text(self.model_dump_json(indent=2))

    @classmethod
    def from_state(cls) -> "MovieStorage":
        if not MOVIE_STORAGE_FILEPATH.exists():
            return MovieStorage()
        return cls.model_validate_json(MOVIE_STORAGE_FILEPATH.read_text())

    def get(self) -> list[Movie]:
        return list(self.slug_to_movie.values())

    def get_by_slug(self, slug: str) -> Movie | None:
        return self.slug_to_movie.get(slug)

    def create(self, movie_in: MovieCreate) -> Movie:
        movie = Movie(
            **movie_in.model_dump(),
        )
        self.slug_to_movie[movie.slug] = movie
        self.save_state()
        return movie

    def update(self, movie: Movie, movie_in: MovieUpdate) -> Movie:
        for fiend_name, value in movie_in:
            setattr(movie, fiend_name, value)
        self.save_state()
        return movie

    def update_partial(self, movie: Movie, movie_in: MoviePartialUpdate):
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)
        self.save_state()
        return movie


try:
    storage = MovieStorage.from_state()
except ValidationError:
    storage = MovieStorage()
    storage.save_state()
