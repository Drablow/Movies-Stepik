from fastapi import  APIRouter, status

from schemas.movies import Movie, MovieCreate, MovieRead

from api.api_v1.movies.crud import storage

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get("/", response_model=list[MovieRead])
def get_all_movies() -> list[Movie]:
    return storage.get()


@router.post(
    "/",
    response_model=MovieRead,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(movie: MovieCreate):
    return storage.create(movie)



