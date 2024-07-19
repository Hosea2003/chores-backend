from typing import Any
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest
from django.db.models import Q

from identity.models import AppUser


class AppAuthBackend(BaseBackend):
    def authenticate(
        self, request: HttpRequest, username: str = None, password: str = None, **kwargs
    ) -> AbstractBaseUser | None:
        try:
            user = AppUser.objects.get(Q(email=username) | Q(username=username))
        except:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id: int) -> AbstractBaseUser | None:
        try:
            return AppUser.objects.get(id=user_id)
        except AppUser.DoesNotExist:
            return None
