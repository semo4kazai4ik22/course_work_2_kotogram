import pytest

from config import *

from main_page.dao.main_page_dao import MainPageDao


class TestMainPageDao:

    @pytest.fixture
    def main_page_dao(self):
        return MainPageDao(POST_PATH)

    @pytest.fixture
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    # тестируем получение всех постов
    def test_get_all_check_type(self, main_page_dao):
        posts = main_page_dao.get_all()
        assert type(posts) == list, "Список постов должен быть list"
        assert type(posts[0]) == dict, "Один пост должен быть dict"

    def test_get_all_has_keys(self, main_page_dao, keys_expected):
        posts = main_page_dao.get_all()
        for post in posts:
            keys = post.keys()
            assert set(keys) == keys_expected, "Потерялся ключ поста"

    # тестируем получение одного поста
    def test_get_one_check_type(self, main_page_dao):
        post = main_page_dao.get_post_by_pk(3)
        assert type(post) == dict, "Один пост должен быть dict"

    def test_one_has_keys(self, main_page_dao, keys_expected):
        post = main_page_dao.get_post_by_pk(3)
        keys = post.keys()
        assert set(keys) == keys_expected, "Потерялся ключ"

    params_for_test_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]

    @pytest.mark.parametrize("post_pk", params_for_test_by_pk)
    def test_get_one_check_pk(self, main_page_dao, post_pk):
        post = main_page_dao.get_post_by_pk(post_pk)
        assert post["pk"] == post_pk, "Полученный пост не соответствует запрошенному"

    # тестируем получение поста по пользователю

    params_for_test_by_user = [("leo", {1, 5}), ("johnny", {2, 6}), ("larry", {4, 8})]

    @pytest.mark.parametrize("poster_name, pk_correct", params_for_test_by_user)
    def test_get_by_user(self, main_page_dao, poster_name, pk_correct):
        posts = main_page_dao.get_posts_by_user(poster_name)
        post_pks = set()
        for post in posts:
            post_pks.add(post["pk"])

        assert post_pks == pk_correct, "Поиск поста пользователя неверный"

    # тестируем поиск поста по вхождению слова

    params_for_test_search = [("заметят", {1}), ("штуки", {2}), ("лампочка", {6})]

    @pytest.mark.parametrize("query, pk_correct", params_for_test_search)
    def test_get_by_user(self, main_page_dao, query, pk_correct):
        posts = main_page_dao.search_for_posts(query)
        post_pks = set()
        for post in posts:
            post_pks.add(post["pk"])

        assert post_pks == pk_correct, "Поиск поста по вхождению строки неверный"