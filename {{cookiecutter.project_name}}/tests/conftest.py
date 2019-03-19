import pytest
import os


def pytest_sessionstart(session):
    os.environ["FLASK_ENV"] = "testing"
    from coast.flask import create_app

    create_app()


@pytest.fixture(scope="session")
def app():
    from flask import current_app

    yield current_app


@pytest.fixture()
def client(app):
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield client
    ctx.pop()
