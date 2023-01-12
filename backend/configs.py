import os

POSTGRES_USER = os.environ.get("POSTGRES_USER", "pguser")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "pgkalmatmlgh3032810")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "webcard")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")

SQL_ALCHEMY_DB_URL = f"postgresql+asyncpg://" \
                     f"{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                     f"@{POSTGRES_HOST}:{POSTGRES_PORT}" \
                     f"/{POSTGRES_DB}"
