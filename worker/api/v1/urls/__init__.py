from django.urls import include, path

urlpatterns = [
    path("bo/", include("api.v1.urls.backoffice"), name="backoffice")
]