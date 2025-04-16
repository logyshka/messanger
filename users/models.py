from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.validators import UsernameValidator


class User(AbstractBaseUser):
    username_validator = UsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=32,
        unique=True,
        help_text=_(
            "Required. 32 characters or fewer. Letters, digits only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    USERNAME_FIELD = "username"

    objects = UserManager()
