from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path("crops/prediction/", views.prediction, name="prediction")
    path("", views.index, name="index"),
]
