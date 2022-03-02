from typing import List
from pydantic import BaseModel
from src.models import Article


class ListArticlesQuery(BaseModel):
    def execute(self) -> List[Article]:
        articles = Article.list()

        return articles


class GetArticleByIDQuery:
    def __init__(self, id):
        self.id = id

    def execute(self) -> Article:
        article = Article.get_by_id(self.id)
        return article


class GetArticleByTitleQuery:
    def __init__(self, title):
        self.title = title

    def execute(self) -> Article:
        article = Article.get_by_title(self.title)
        return article
