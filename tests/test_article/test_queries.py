import pytest

from src.models import Article, NotFound
from src.queries import ListArticlesQuery, GetArticleByIDQuery, GetArticleByTitleQuery


def test_list_articles():
    """
    GIVEN 2 articles stored in the database
    WHEN the execute method is called
    THEN it should return 2 articles
    """
    Article(
        author="rustam_zokirov@epam.com",
        title="New Article",
        content="Super extra awesome article"
    ).save()
    Article(
        author="rustam_zokirov@epam.com",
        title="Another Article",
        content="Super awesome article"
    ).save()

    query = ListArticlesQuery()

    assert len(query.execute()) == 2


def test_get_article_id():
    """
    GIVEN an article stored in the database
    WHEN the execute method is called
    THEN it should return the article id
    """
    article = Article(
        author="rustam_zokirov@epam.com",
        title="ML Article",
        content="ML is not as awesome as it seems")
    article.save()

    query = GetArticleByIDQuery(article.id)

    assert query.execute().id == article.id
    assert query.execute().title == article.title
    assert query.execute().content == article.content
    assert query.execute().author == article.author


@pytest.mark.parametrize("invalid_id", [
    "",
    "99999999",
    9999999999
])
def test_get_article_id_with_invalid_id(invalid_id):
    """
    GIVEN an article id that is not valid
    WHEN the execute method is called
    THEN it should raise NotFound
    """
    query = GetArticleByIDQuery(invalid_id)

    with pytest.raises(NotFound):
        query.execute()


def test_get_article_with_title():
    """
    GIVEN an article stored in the database
    WHEN the execute method is called
    THEN it should return the article id
    """
    article = Article(
        author="rustam_zokirov@epam.com",
        title="Silicon Valley",
        content="Silicon Valley is awesome")
    article.save()

    query = GetArticleByTitleQuery(article.title)

    assert query.execute().id == article.id
    assert query.execute().title == article.title
    assert query.execute().content == article.content
    assert query.execute().author == article.author


@pytest.mark.parametrize("invalid_title", [
    "Hello World! >''<",
    "",
    0,
    123456,
])
def test_get_article_id_with_invalid_id(invalid_title):
    """
    GIVEN an article id that is not valid
    WHEN the execute method is called
    THEN it should raise NotFound
    """
    query = GetArticleByIDQuery(invalid_title)

    with pytest.raises(NotFound):
        query.execute()
