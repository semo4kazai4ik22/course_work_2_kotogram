import logging

from flask import Blueprint, jsonify

api_blueprint = Blueprint("api_blueprint", __name__, template_folder="templates")

from main_page.dao.main_page_dao import MainPageDao
from main_page.dao.comments_dao import CommentsDao
from config import POST_PATH, COMMENTS_PATH

main_page_dao = MainPageDao(POST_PATH)
comments_dao = CommentsDao(COMMENTS_PATH)

logger = logging.getLogger("basic")


@api_blueprint.route("/api/main_page")
def api_main_page():
    """Главная страница показывает все посты"""
    logger.debug("Запрошены все посты через API")
    posts = main_page_dao.get_all()
    return jsonify(posts)


@api_blueprint.route("/api/post/<int:post_id>")
def api_one_post_page(post_id):
    """Страница одного поста по его номеру"""
    logger.debug(f"Запрошена страница поста {post_id} через API")
    post = main_page_dao.get_post_by_pk(post_id)
    return jsonify(post)
