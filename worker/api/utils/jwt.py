import uuid
from datetime import datetime

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model


def get_username_field():
    try:
        username_field = get_user_model().USERNAME_FIELD
    except AttributeError:
        username_field = "username"

    return username_field


def get_username(user):
    try:
        username = user.get_username()
    except AttributeError:
        username = user.username

    return username
