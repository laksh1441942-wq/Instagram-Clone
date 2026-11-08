# Instagram Clone

A work-in-progress FastAPI backend for an Instagram-style social media
application.

## Project status

**Current phase:** Core backend and authentication

### Completed

- [x] Set up a FastAPI application under `backend/`.
- [x] Added SQLite database support with SQLAlchemy.
- [x] Added database session management and SQLAlchemy models.
- [x] Added user and post relationships, including post likes.
- [x] Added Pydantic schemas for users and posts.
- [x] Implemented user registration and JWT login.
- [x] Implemented fetching, listing, and deleting users.
- [x] Implemented post creation, retrieval, and deletion.
- [x] Added post likes, unlikes, and liker retrieval.
- [x] Added password reset code generation and password updates.
- [x] Added Alembic migrations for the application schema.
- [x] Centralized the SQLite database path for FastAPI and Alembic.
- [x] Added Black formatting configuration for Python files.

### Next steps

- [ ] Add automated tests for authentication, users, and posts.
- [ ] Protect user and post operations with authenticated-user dependencies.
- [ ] Protect user, post, and like operations with authenticated-user dependencies.
- [ ] Add image upload and media storage.
- [ ] Add comments, follows, and a feed.
- [ ] Add automated deployment documentation.

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
| `POST` | `/auth/signup` | Register a new user |
| `POST` | `/auth/token` | Log in and receive a bearer token |
| `POST` | `/auth/sendcode` | Generate a password reset code |
| `POST` | `/auth/verifycode` | Verify a password reset code |
| `POST` | `/auth/reset` | Set a new password |
| `POST` | `/users/profile` | Retrieve the current user profile |
| `GET` | `/users/users` | List users with pagination |
| `GET` | `/users/{user_id}` | Retrieve a user by ID |
| `DELETE` | `/users/{user_id}` | Delete a user |
| `PUT` | `/users/{username}` | Update the authenticated user profile |
| `POST` | `/posts/` | Create a post |
| `GET` | `/posts/{author_id}/posts` | Retrieve all posts by an author |
| `GET` | `/posts/{post_id}` | Retrieve a post by ID |
| `DELETE` | `/posts/{post_id}` | Delete a post |
| `POST` | `/likes/like` | Like a post |
| `POST` | `/likes/unlike` | Unlike a post |
| `GET` | `/likes/likes/{post_id}` | List users who liked a post |

## Running locally

1. Create and activate a Python virtual environment from the repository root.
2. Install the backend dependencies:

   ```bash
   python -m pip install -r backend/requirements.txt
   ```

3. Copy `backend/.env.example` to `.env` and set a secure `SECRET_KEY`.
4. Apply the database migration from the repository root:

   ```bash
   alembic -c backend/alembic.ini upgrade head
   ```

5. Start the development server from the repository root:

   ```bash
   uvicorn backend.app.main:app --reload
   ```

6. Open the interactive API documentation at
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Authentication settings are loaded from `.env`. Use a long, random
`SECRET_KEY` outside local development. The SQLite database is always stored
at `backend/sql.db`, regardless of the directory used to start the server.

To check migration consistency:

```bash
alembic -c backend/alembic.ini check
```

Black is configured for the project virtual environment. Install it if needed:

```bash
python -m pip install black
```

## Project structure

| File | Responsibility |
| --- | --- |
| `backend/app/main.py` | FastAPI app entry point |
| `backend/app/core/config.py` | Shared database path and application configuration |
| `backend/app/database/db.py` | Database engine, session, and declarative base |
| `backend/app/models/` | SQLAlchemy models and relationships |
| `backend/app/schemas/` | Request and response schemas |
| `backend/app/services/` | Database queries and authentication logic |
| `backend/app/routers/` | FastAPI route definitions |
| `backend/migrations/` | Alembic configuration and migration history |
| `backend/requirements.txt` | Pinned Python dependencies |
