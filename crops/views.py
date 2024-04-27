from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    latest_question_list = []
    context = {"latest_question_list": latest_question_list}

    return render(request, "crops/home.html", context)

def prediction(request):
    latest_question_list = []
    context = {"latest_question_list": latest_question_list}

    return render(request, "crops/prediction.html", context)
