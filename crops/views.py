from django.http import HttpResponse
from django.shortcuts import render
import joblib

def index(request):
    latest_question_list = []
    context = {"latest_question_list": latest_question_list}

    return render(request, "crops/home.html", context)

def prediction(request):
    prediction = [0]
    user_inputs=[]
    if request.method == 'POST':
        area = int(request.POST.get('area'))
        item = int(request.POST.get('item'))
        year = int(request.POST.get('year'))
        rain_avg = float(request.POST.get('rain_avg'))
        pesticides = float(request.POST.get('pesticides'))
        avg_temp = float(request.POST.get('avg_temp'))

        user_inputs = [area,item,year,rain_avg,pesticides,avg_temp]
        scaled_inputs = [user_inputs]

        model=joblib.load('controller/crop-yield-predictor2.joblib')

        prediction = model.predict(scaled_inputs)
        
        
    context = {
        "prediction_value": round((prediction[0] * 0.0001),3), 
        "user_inputs": [str(i) for i in user_inputs],
        }
    return render(request, "crops/prediction.html", context)

