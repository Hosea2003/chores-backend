from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class AppUserManger(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs) -> AbstractUser:
        email = self.normalize_email(email=email)

        user: AbstractUser = self.model(username=username, email=email, **kwargs)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(
        self, username, email, password=None, **kwargs
    ) -> AbstractUser:
        super_user = self.create_user(username, email, password=password, **kwargs)
        super_user.is_staff = True
        super_user.is_superuser = True
        super_user.save()

        return super_user


# Create your models here.
class AppUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(null=True, blank=True)

    objects = AppUserManger()

    REQUIRED_FIELDS = ["email"]
