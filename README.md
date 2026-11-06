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
- [x] Implemented post creation and post retrieval by user or post ID.
- [x] Added password reset code generation and password updates.
- [x] Added an Alembic migration for the updated user model.

### Next steps

- [ ] Add automated tests for authentication, users, and posts.
- [ ] Protect user and post operations with authenticated-user dependencies.
- [ ] Add update and delete endpoints for posts.
- [ ] Add endpoints for liking and unliking posts.
- [ ] Add image upload and media storage.
- [ ] Add comments, follows, and a feed.
- [ ] Move database configuration into environment variables.
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
| `POST` | `/users` | Register a new user |
| `POST` | `/token` | Log in and receive a bearer token |
| `POST` | `/profile` | Retrieve the current user profile |
| `GET` | `/users/*` | List users with pagination |
| `GET` | `/users/{user_id}` | Retrieve a user by ID |
| `DELETE` | `/users/{user_id}` | Delete a user |
| `POST` | `/posts` | Create a post |
| `GET` | `/posts/{user_id}/posts` | Retrieve all posts for a user |
| `GET` | `/posts/{user_id}/{post_id}` | Retrieve one of a user’s posts |
| `PUT` | `/users/{username}` | Update the authenticated user’s username |
| `POST` | `/resetpassword/sendcode` | Generate a password reset code |
| `POST` | `/resetpassword/vefifycode` | Verify a password reset code |
| `POST` | `/resetpassword/reset` | Set a new password |

## Running locally

1. Create and activate a Python virtual environment from the repository root.
2. Install the backend dependencies:

   ```bash
   python -m pip install -r backend/requirements.txt
   ```

3. Copy `backend/.env.example` to `.env` and set a secure `SECRET_KEY`.
4. Start the development server from the repository root:

   ```bash
   uvicorn backend.main:app --reload
   ```

5. Open the interactive API documentation at
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Authentication settings are loaded from `.env`. Use a long, random
`SECRET_KEY` outside local development. The SQLite database is stored in
`sql.db` in the directory where the server is started.

Apply Alembic migrations from the repository root when working with an
existing database:

```bash
alembic -c backend/alembic.ini upgrade head
```

## Project structure

| File | Responsibility |
| --- | --- |
| `backend/main.py` | FastAPI app entry point |
| `backend/app/database/db.py` | Database engine, session, and declarative base |
| `backend/app/models/models.py` | SQLAlchemy models and relationships |
| `backend/app/schemas/schemas.py` | Request and response schemas |
| `backend/app/services/services.py` | Database queries and authentication logic |
| `backend/migrations/` | Alembic configuration and migration history |
| `backend/requirements.txt` | Pinned Python dependencies |
