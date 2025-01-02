import os


class Config:

    if os.environ.get("TESTING") in ["true", "True"]:
        DB_USER = "postgres"
        DB_PASSWORD = "postgres"
        DB_NAME = "url_shortening"
        DB_HOST = "localhost"
        DB_PORT = "5432"
    else:
        DB_USER = os.getenv("POSTGRES_USER", "postgres")
        DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
        DB_NAME = os.getenv("POSTGRES_NAME", "postgres")
        DB_HOST = os.getenv("POSTGRES_HOST", "db_postgres")
        DB_PORT = os.getenv("POSTGRES_PORT", "5432")

    if os.environ.get("GITHUB_WORKFLOW"):
        DB_USER = "postgres"
        DB_PASSWORD = "admin"
        DB_NAME = "github_actions"
        DB_HOST = "localhost"
        DB_PORT = "5432"

    DB_CONFIG = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    print(DB_CONFIG)
    DB_ASYNC_CONFIG = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        f"?prepared_statement_cache_size=0"
    )