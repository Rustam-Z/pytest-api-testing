from flask import Flask, jsonify, request
from pydantic import ValidationError

from src.commands import CreateArticleCommand
from src.queries import GetArticleByIDQuery, ListArticlesQuery

app = Flask(__name__)


@app.errorhandler(ValidationError)
def handle_validation_exception(error):
    response = jsonify(error.errors())
    response.status_code = 400
    return response


@app.route('/create-article/', methods=['GET'])
def create_article():
    command = CreateArticleCommand(**request.json)
    article = command.execute()
    return jsonify(article.dict())


@app.route("/article/<article_id>/", methods=["GET"])
def get_article(article_id):
    query = GetArticleByIDQuery(
        id=article_id
    )
    article = query.execute()
    return jsonify(article.dict())


@app.route("/articles/", methods=["GET"])
def list_articles():
    query = ListArticlesQuery()
    articles = query.execute()
    return jsonify([article.dict() for article in articles])



