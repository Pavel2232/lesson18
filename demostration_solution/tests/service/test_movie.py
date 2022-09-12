from unittest.mock import MagicMock
import pytest

from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    tor = Movie(id=1, title="tor", description="marvel", trailer="whatch youtube", year=2016, rating="16+")
    spider_man = Movie(id=2, title="spider_man", description="film", trailer="whatch youtube2", year=2017,rating="16+")
    venom = Movie(id=3, title="venom", description="sony", trailer="whatch youtube3", year=2018, rating="18+")

    movie_dao.get_one = MagicMock(return_value=tor)
    movie_dao.get_all = MagicMock(return_value=[tor, spider_man, venom])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movies = self.movie_service.get_one(1)
        assert movies != None
        assert movies.id != None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        user_d = {
            "title": "tor",
            "year": 2016,
        }
        movie = self.movie_service.create(user_d)
        assert movie.id != None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            "title": "Venom",
            "year": 2018,
        }
        self.movie_service.update(movie_d)
