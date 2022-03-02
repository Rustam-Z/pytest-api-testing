import pytest

from src.models import Article
from src.commands import CreateArticleCommand, AlreadyExists


def test_create_article():
    """
    GIVEN CreateArticleCommand with valid author, title, and content properties
    WHEN the execute method is called
    THEN a new Article must exist in the database with the same attributes
    """
    cmd = CreateArticleCommand(
        author="rustam_zokirov@epam.com",
        title="New Article",
        content="Super awesome article"
    )

    article = cmd.execute()

    db_article = Article.get_by_id(article.id)

    assert db_article.id == article.id
    assert db_article.author == article.author
    assert db_article.title == article.title
    assert db_article.content == article.content


@pytest.mark.xfail()
def test_create_article_with_wrong_email_format():
    """
    GIVEN CreateArticleCommand with a wrong email format
    WHEN the execute method is called
    THEN the AlreadyExists exception must be raised
    """

    cmd = CreateArticleCommand(
        author="rustam_zokirov",
        title="New Article",
        content="Super awesome article"
    )

    cmd.execute()


@pytest.mark.xfail()
def test_create_article_with_wrong_title_as_integer():
    """
    GIVEN CreateArticleCommand with a wrong email format
    WHEN the execute method is called
    THEN the AlreadyExists exception must be raised
    """

    cmd = CreateArticleCommand(
        author="rustam_zokirov",
        title=1234,
        content="Super awesome article"
    )

    cmd.execute()


def test_create_article_already_exists():
    """
    GIVEN CreateArticleCommand with a title of some article in database
    WHEN the execute method is called
    THEN the AlreadyExists exception must be raised
    """

    Article(
        author="rustam_zokirov@epam.com",
        title="New Article",
        content="Super extra awesome article"
    ).save()

    cmd = CreateArticleCommand(
        author="rustam_zokirov@epam.com",
        title="New Article",
        content="Super awesome article"
    )

    with pytest.raises(AlreadyExists):
        cmd.execute()
