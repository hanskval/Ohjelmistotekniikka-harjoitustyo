import os
from pathlib import Path
from dotenv import load_dotenv

# Projektin juuri (budjetti-app/)
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# Tietokantapolku
DATABASE_FILENAME = os.getenv("DATABASE_FILENAME", "database.sqlite")
DATABASE_PATH = BASE_DIR / "data" / DATABASE_FILENAME

# Varmistetaan, että data-kansio on olemassa
DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)