import os
from collections.abc import Callable, Generator

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

os.environ.setdefault("SECRET_KEY", "test-secret-key")

from backend.app.database.db import Base, get_db
from backend.app.main import app
from backend.app.models import PostModel, UserModel
from backend.app.services.auth_service import bcrypt_context
from backend.app.services.posts_service import create_post
from backend.app.schemas import CreatePost


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
def test_engine():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture
def db_session(test_engine) -> Generator[Session, None, None]:
    session = sessionmaker(bind=test_engine)()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def test_app(db_session: Session) -> Generator[FastAPI, None, None]:
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    yield app
    app.dependency_overrides.clear()


@pytest.fixture
async def client(test_app: FastAPI):
    transport = ASGITransport(app=test_app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as http:
        yield http


@pytest.fixture
def user_factory(db_session: Session) -> Callable[..., UserModel]:
    def create_user(
        username: str = "alice",
        email: str | None = None,
        password: str = "password123",
    ) -> UserModel:
        user = UserModel(
            username=username,
            email=email or f"{username}@example.com",
            hashed_password=bcrypt_context.hash(password),
            name=username.title(),
            profile_pic="",
            bio="",
            location="",
        )
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)
        return user

    return create_user


@pytest.fixture
def post_factory(db_session: Session) -> Callable[..., PostModel]:
    def create_user_post(
        author_id: int,
        title: str = "Test post",
        content: str = "A test post #testing",
    ) -> PostModel:
        return create_post(
            db_session,
            CreatePost(title=title, content=content, image="", location=""),
            author_id,
        )

    return create_user_post


async def get_token(
    client: AsyncClient, username: str, password: str = "password123"
) -> str:
    response = await client.post(
        "/auth/token",
        data={"username": username, "password": password},
    )
    assert response.status_code == 200
    return response.json()["access_token"]
