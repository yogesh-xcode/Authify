from tortoise import Tortoise

db_url = "sqlite://app/storage/user.sqlite"


async def db_init():
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["app.models.auth_model"]},
    )
    await Tortoise.generate_schemas()
