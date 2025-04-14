from tortoise import Tortoise
from app.config.load_env import db_url


async def db_init():
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["app.models.auth_model"]},
    )
    await Tortoise.generate_schemas()
