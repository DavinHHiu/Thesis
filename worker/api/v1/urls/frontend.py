from django.urls import path

from api.v1 import views

urlpatterns = [
    path("register/", views.RegisterApiView.as_view(), name="register"),
    path("token/", views.BaseObtainJSONWebTokenView.as_view(), name="eu-token"),
    path(
        "token/refresh/",
        views.EURefreshJSONWebTokenView.as_view(),
        name="eu-token-refresh",
    ),
]
