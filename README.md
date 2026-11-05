# Instagram Clone

A work-in-progress backend for an Instagram-style social media application.

## Project status

**Current phase:** Core backend and authentication

### Completed

- [x] Set up a FastAPI application.
- [x] Added SQLite database support with SQLAlchemy.
- [x] Added database session management in `db.py`.
- [x] Created user and post models with SQLAlchemy relationships.
- [x] Added a many-to-many relationship for post likes.
- [x] Added Pydantic schemas for users and posts.
- [x] Implemented user registration.
- [x] Implemented login with password hashing and JWT session tokens.
- [x] Implemented fetching the current user profile.
- [x] Implemented user listing, lookup, and deletion.
- [x] Implemented post creation and post retrieval by user or post ID.
- [x] Added an Alembic migration for the updated user model.

### Next steps

- [ ] Add automated tests for authentication, users, and posts.
- [ ] Protect user and post operations with authenticated-user dependencies.
- [ ] Add update and delete endpoints for posts.
- [ ] Add endpoints for liking and unliking posts.
- [ ] Add image upload and media storage.
- [ ] Add comments, follows, and a feed.
- [ ] Move secrets and database configuration into environment variables.
- [ ] Add dependency metadata and deployment documentation.

## Tech stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Alembic
- Pydantic
- JWT authentication
- bcrypt password hashing

## API endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `POST` | `/users` | Register a new user |
| `POST` | `/token` | Log in and receive a bearer token |
| `POST` | `/profile` | Retrieve the current user profile |
| `GET` | `/users/*` | List users with pagination |
| `GET` | `/users/{user_id}` | Retrieve a user by ID |
| `DELETE` | `/users/{user_id}` | Delete a user |
| `POST` | `/posts` | Create a post |
| `GET` | `/posts/{user_id}/posts` | Retrieve all posts for a user |
| `GET` | `/posts/{user_id}/{post_id}` | Retrieve one of a user’s posts |

## Running locally

1. Create and activate a Python virtual environment.
2. Install the project dependencies used by the application.
3. Start the development server:

   ```bash
   uvicorn main:app --reload
   ```

4. Open the interactive API documentation at
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Authentication settings are loaded from `.env`. Replace the placeholder
`SECRET_KEY` with a long, random value before using the application outside
local development.

The local SQLite database is stored in `sql.db`. Apply Alembic migrations when
working with an existing database:

```bash
alembic upgrade head
```

## Project structure

| File | Responsibility |
| --- | --- |
| `main.py` | FastAPI app and route definitions |
| `db.py` | Database engine, session, and declarative base |
| `models.py` | SQLAlchemy models and relationships |
| `schemas.py` | Request and response schemas |
| `services.py` | Database queries and authentication logic |
| `migrations/` | Alembic configuration and migration history |
