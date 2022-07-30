import pytest

from app import app

class TestApiMainPage:

    @pytest.fixture()
    def keys(self):
        return ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]

    def test_api_main_page(self, keys):
        """ Проверяем, возвращает ли страница всех постов нужный статус-код и нужный формат данных """
        response = app.test_client().get('/api/main_page', follow_redirects=True)
        assert response.status_code == 200, "Статус код неверный"
        assert response.mimetype == "application/json", "Получен не JSON"
        data = response.get_json()
        assert type(data) == list, "Данные должны быть списком"
        assert len(data) > 0
        for key in keys:
            assert key in data[0], "В данных JSON отсуствуют нужные ключи"

    def test_api_post_page(self, keys):
        """ Проверяем, возвращает ли страница одного поста нужный статус-код и нужный формат данных """
        response = app.test_client().get('/api/post/1', follow_redirects=True)
        assert response.status_code == 200, "Статус код неверный"
        assert response.mimetype == "application/json", "Получен не JSON"
        data = response.get_json()
        assert type(data) == dict, "Данные должны быть словарем"
        for key in keys:
            assert key in data, "В данных JSON отсуствуют нужные ключи"
