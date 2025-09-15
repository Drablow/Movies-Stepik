from schemas.movies import Movie, MovieCreate, MovieUpdate, MoviePartialUpdate
from pydantic import BaseModel


class MovieStorage(BaseModel):
    slug_to_movie: dict[str, Movie] = {}

    def get(self) -> list[Movie]:
        return list(self.slug_to_movie.values())

    def get_by_slug(self, slug: str) -> Movie | None:
        return self.slug_to_movie.get(slug)

    def create(self, movie_in: MovieCreate) -> Movie:
        movie = Movie(
            **movie_in.model_dump(),
        )
        self.slug_to_movie[movie.slug] = movie
        return movie

    def update(self, movie: Movie, movie_in: MovieUpdate) -> Movie:
        for fiend_name, value in movie_in:
            setattr(movie, fiend_name, value)
        return movie

    def update_partial(self, movie: Movie, movie_in: MoviePartialUpdate):
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)
        return movie


storage = MovieStorage()

storage.create(
    MovieCreate(
        slug="Один дома",
        title="Один дома",
        description="Парень остается один дома",
        genre="Комедия",
        year=1990,
    )
)

storage.create(
    MovieCreate(
        slug="Маска",
        title="Маска",
        description="Парень находит маску",
        genre="Комедия",
        year=1994,
    )
)


storage.create(
    MovieCreate(
        slug="Остров сокровищ",
        title="Остров сокровищ",
        description="У них есть пушка, но зачем?",
        genre="Приключения",
        year=1988,
    )
)
