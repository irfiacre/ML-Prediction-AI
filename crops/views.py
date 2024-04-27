from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    latest_question_list = []
    context = {"latest_question_list": latest_question_list}

    return render(request, "crops/home.html", context)

def prediction(request):
    if request.method == 'POST':
        input1 = request.POST.get('input1')
        print("------=",input1)
    context = {"prediction_value": input1}
    return render(request, "crops/prediction.html", context)

