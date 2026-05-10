import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME", "database.sqlite")
DATABASE_PATH = BASE_DIR / "data" / DATABASE_FILENAME


DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
