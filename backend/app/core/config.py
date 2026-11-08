from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parents[2]
DATABASE_PATH = BACKEND_DIR / "sql.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
