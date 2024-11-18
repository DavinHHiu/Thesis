import uuid
from datetime import datetime

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework_jwt.settings import api_settings

from api.utils.jwt import get_username, get_username_field

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class JSONWebTokenAuthentication(BaseAuthentication):
    def jwt_get_secret_key(payload=None):
        """
        For enhanced security you may want to use a secret key based on user.

        This way you have an option to logout only this user if:
            - token is compromised
            - password is changed
            - etc.
        """
        if api_settings.JWT_GET_USER_SECRET_KEY:
            User = get_user_model()  # noqa: N806
            user = User.objects.get(pk=payload.get("user_id"))
            key = str(api_settings.JWT_GET_USER_SECRET_KEY(user))
            return key
        return api_settings.JWT_SECRET_KEY

    def jwt_create_payload(user):
        username_field = get_username_field()
        username = get_username(user)

        payload = {
            "user_id": user.pk,
            username_field: username,
            "exp": int(
                (timezone.now() + settings.JWT_AUTH["JWT_EXPIRATION_DELTA"]).timestamp()
            ),
        }
        if hasattr(user, "email"):
            payload["email"] = user.email
        if isinstance(user.pk, uuid.UUID):
            payload["user_id"] = str(user.pk)

        # Include original issued at time for a brand new token,
        # to allow token refresh
        if api_settings.JWT_ALLOW_REFRESH:
            payload["orig_iat"] = int(timezone.now().timestamp())

        return payload

    @classmethod
    def jwt_encode_payload(self, payload):
        return jwt.encode(
            payload,
            key=api_settings.JWT_PRIVATE_KEY or self.jwt_get_secret_key(payload),
            algorithm=api_settings.JWT_ALGORITHM,
        ).decode("utf-8")

    @classmethod
    def jwt_decode_payload(self, token):
        options = {
            "verify_exp": api_settings.JWT_VERIFY_EXPIRATION,
        }
        # get user from token, BEFORE verification, to get user secret key
        unverified_payload = jwt.decode(token, None, False)
        secret_key = self.jwt_get_secret_key(unverified_payload)
        return jwt.decode(
            token,
            api_settings.JWT_PRIVATE_KEY or secret_key,
            api_settings.JWT_VERIFY,
            algorithms=[api_settings.JWT_ALGORITHM],
            options=options,
        )

    @classmethod
    def jwt_get_username_from_payload(self, payload):
        return payload.get(get_username_field())

    @classmethod
    def get_token_from_request(self, request):
        auth = get_authorization_header(request).split()
        auth_header_prefix = api_settings.JWT_AUTH_HEADER_PREFIX.lower()

        if not auth:
            if api_settings.JWT_AUTH_COOKIE:
                return request.COOKIES.get(api_settings.JWT_AUTH_COOKIE)
            return None

        if len(auth) == 1:
            msg = _("Invalid Authorization header. No credentials provided.")
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _(
                "Invalid Authorization header. Credentials string "
                "should not contain spaces."
            )
            raise exceptions.AuthenticationFailed(msg)

        return auth[1]

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        return '{0} realm="{1}"'.format(
            api_settings.JWT_AUTH_HEADER_PREFIX, self.www_authenticate_realm
        )


class BaseJSONWebTokenAuthentication(JSONWebTokenAuthentication):
    """
    Token based authentication using the JSON Web Token standard.
    """

    def authenticate(self, request):
        """
        Returns a two-tuple of `User` and token if a valid signature has been
        supplied using JWT-based authentication.  Otherwise returns `None`.
        """
        jwt_value = self.get_token_from_request(request)
        if jwt_value is None:
            return None

        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            msg = _("Signature has expired.")
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _("Error decoding signature.")
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()

        user = self.authenticate_credentials(payload)

        return (user, payload)

    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        User = get_user_model()
        username = self.jwt_get_username_from_payload(payload)

        if not username:
            msg = _("Invalid payload.")
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            msg = _("Invalid signature.")
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = _("User account is disabled.")
            raise exceptions.AuthenticationFailed(msg)

        return user
