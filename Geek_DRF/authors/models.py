from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

from django.db.models.fields import UUIDField


class Author(AbstractUser):
    uuid = UUIDField(primary_key=True, default=uuid4)
    email = models.EmailField(unique=True)

# from uuid import uuid4
#
# from django.db import models
#
#
# class Author(models.Model):
#     uid = models.UUIDField(primary_key=True, default=uuid4)
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     birthday_year = models.PositiveIntegerField()