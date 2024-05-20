from django.urls import path

from breast_cancer import views

urlpatterns = [
    path("", views.index, name="index"),
    path("prediction/", views.prediction, name="br_prediction")
]
