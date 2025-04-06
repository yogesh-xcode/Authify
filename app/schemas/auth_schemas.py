from tortoise.models import Model
from tortoise import fields
import uuid


class User(Model):
    id = fields.UUIDField(primary_key=True, default=lambda: uuid.uuid4(), unique=True)
    email = fields.CharField(
        max_length=60, unique=True, null=False, description="email of the user"
    )
    password = fields.CharField(
        max_length=100, min_length=20, null=False, description="password of the user"
    )
    username = fields.CharField(
        max_length=15, unique=True, null=False, description="username of the user"
    )

    def __str__(self):
        return self.name
