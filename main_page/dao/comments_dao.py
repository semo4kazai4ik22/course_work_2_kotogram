import json


class CommentsDao:
    """Работа со всеми комментариями"""

    def __init__(self, path):
        self.path = path

    def get_all(self):
        """возвращает все комментарии списком словарей"""
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def get_comments_by_post_id(self, post_id):
        """возвращает комментарии определенного поста"""
        if type(post_id) != int:
            raise TypeError

        data = self.get_all()
        comments = []

        for comment in data:
            if comment["post_id"] == post_id:
                comments.append(comment)
        return comments
