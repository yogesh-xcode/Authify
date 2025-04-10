from tortoise import Tortoise
import ssl

db_url = "sqlite://app/utils/user.sqlite"


async def db_init():
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["app.schemas.auth_schemas"]},
    )
    await Tortoise.generate_schemas()
