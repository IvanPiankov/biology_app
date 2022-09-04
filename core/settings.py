from starlette.config import Config


config = Config(".env")

DATABASE_URL = config("BG_DATABASE_URL", cast=str, default="")
