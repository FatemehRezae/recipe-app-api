from django.contrib.auth.models import(
    PermissionsMixin,
    BaseUserManager,
    AbstractBaseUser,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=320, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
