from django.urls import path

from breast_cancer import views

urlpatterns = [
    path("", views.prediction, name="br_prediction"),
]
