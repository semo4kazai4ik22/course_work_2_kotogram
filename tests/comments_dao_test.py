import pytest

from config import *

from main_page.dao.comments_dao import CommentsDao


class TestCommentsDao:

    @pytest.fixture
    def comments_dao(self):
        return CommentsDao(COMMENTS_PATH)

    @pytest.fixture
    def keys_expected(self):
        return {"post_id", "commenter_name", "comment", "pk"}

    # тестируем получение всех комментариев
    def test_get_all_check_type(self, comments_dao):
        comments = comments_dao.get_all()
        assert type(comments) == list, "Список комментариев должен быть list"
        assert type(comments[1]) == dict, "Один комментарий должен быть dict"

    def test_get_all_has_keys(self, comments_dao, keys_expected):
        comments = comments_dao.get_all()
        for comment in comments:
            keys = comment.keys()
            assert set(keys) == keys_expected, "Потерялся ключ комментария"

    # тестируем получение комментариев к определенному посту
    def test_get_comments_for_post_check_type(self, comments_dao):
        comments = comments_dao.get_comments_by_post_id(1)
        assert type(comments[0]) == dict, "Один комментарий должен быть dict"

    def test_one_has_keys(self, comments_dao, keys_expected):
        comments = comments_dao.get_comments_by_post_id(1)
        keys = comments[0].keys()
        assert set(keys) == keys_expected, "Потерялся ключ комментария"