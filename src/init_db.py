"""
E2E (end-to-end) tests need the live server to be running.
"""
from src.models import Article


if __name__ == "__main__":
    Article.create_table()
