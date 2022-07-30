import logging

from json import JSONDecodeError

from flask import Blueprint, render_template, request, abort

from config import POST_PATH, COMMENTS_PATH

from .dao.main_page_dao import MainPageDao
from .dao.comments_dao import CommentsDao

main_page_dao = MainPageDao(POST_PATH)
comments_dao = CommentsDao(COMMENTS_PATH)

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


logger = logging.getLogger("basic.txt")


@main_blueprint.route("/")
def main_page():
    """Главная страница показывает все посты"""
    logger.debug("Открытие главной страницы")
    try:
        all_posts = main_page_dao.get_all()
        return render_template("index.html", all_posts=all_posts)
    except FileNotFoundError:
        print("Файл не найден")
    except JSONDecodeError:
        print("JSON файл не удается преобразовать")


@main_blueprint.route("/post/<int:post_id>")
def search_by_post_id_page(post_id):
    """Страница одного поста по его номеру"""
    logger.debug(f"Открытие страницы поста {post_id}")
    try:
        post = main_page_dao.get_post_by_pk(post_id)
        comments = comments_dao.get_comments_by_post_id(post_id)
    except:
        return "Ошибка при загрузке поста/комментариев"
    else:
        if post is None:
            abort(404)

        content_with_tags = ""
        content = post["content"].split(" ")
        for word in content:
            if word.startswith("#"):
                word = word[1:]
                content_with_tags += f'<a href="/tag/{word}">#{word}</a>'
            else:
                content_with_tags += word
            content_with_tags += " "

        comments_count = len(comments)
        return render_template("post.html", post=post, comments=comments, comments_count=comments_count, content_with_tags=content_with_tags)


@main_blueprint.errorhandler(404)
def post_page_error(e):
    return "Пост не найден", 404

@main_blueprint.route("/search")
def search_by_substring_page():
    """Страница поиска постов по слову"""
    logger.debug("Открытие страницы поиска постов по слову")
    s = request.args.get("s", "")
    posts = main_page_dao.search_for_posts(s)
    posts_count = len(posts)
    return render_template("search.html", posts=posts, s=s, posts_count=posts_count)


@main_blueprint.route("/search/<username>")
def search_by_username_page(username):
    """Страница поиска постов по юзеру"""
    logger.debug(f"Открытие страницы постов юзера {username}")
    user_name = request.args.get("item__username")
    posts = main_page_dao.get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts, user_name=user_name)
