from django.urls import include, path

from api.v1 import views

urlpatterns = [
    path("bo/", include("api.v1.urls.backoffice"), name="backoffice"),
    path("eu/", include("api.v1.urls.frontend"), name="frontend"),
]
