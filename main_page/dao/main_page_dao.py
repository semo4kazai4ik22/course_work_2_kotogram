import json


class MainPageDao:
    """Работа со всеми постами"""

    def __init__(self, path):
        self.path = path

    def get_all(self):
        """возвращает все посты списком словарей"""
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def get_posts_by_user(self, user_name):
        """возвращает посты определенного пользователя"""
        if type(user_name) != str:
            raise TypeError

        data = self.get_all()
        posts_by_user = []

        for post in data:
            if post["poster_name"].lower() == user_name.lower():
                posts_by_user.append(post)
        return posts_by_user



    def search_for_posts(self, query):
        """возвращает список постов по ключевому слову"""
        if type(query) != str:
            raise TypeError

        data = self.get_all()
        posts_by_query = []

        for post in data:
            if query.lower() in post["content"].lower():
                posts_by_query.append(post)
        return posts_by_query

    def get_post_by_pk(self, pk):
        """возвращает один пост по его номеру"""
        if type(pk) != int:
            raise TypeError

        data = self.get_all()

        for post in data:
            if post["pk"] == pk:
                return post
