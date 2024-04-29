from django.http import HttpResponse
from django.shortcuts import render
from joblib import load
import numpy as np


def index(request):
    latest_question_list = []
    context = {"latest_question_list": latest_question_list}

    return render(request, "crops/home.html", context)

def prediction(request):
    prediction = [0]
    user_inputs=[]
    if request.method == 'POST':
        # Load your machine learning model
        model = load('controller/model/crop-predictor.joblib')

        # Get the input values from the form and convert them to float
        rainfall = int(request.POST.get('rainfall'))
        fertilizer = int(request.POST.get('fertilizer'))
        temperature = int(request.POST.get('temperature'))
        nitrogen = int(request.POST.get('nitrogen'))
        phosphorus = int(request.POST.get('phosphorus'))
        potassium = int(request.POST.get('potassium'))

        user_inputs = [rainfall,temperature,fertilizer,nitrogen,phosphorus,potassium]
        print("Received input data:")
        print(f"Rainfall: {rainfall}")
        print(f"Fertilizer: {fertilizer}")
        print(f"Temperature: {temperature}")
        print(f"Nitrogen: {nitrogen}")
        print(f"Phosphorus: {phosphorus}")
        print(f"Potassium: {potassium}")

        input_data = np.array([user_inputs])

        prediction = model.predict(input_data)
        print(f"==== Predicted crop yield: {prediction.tolist()}")
        
    context = {
        "prediction_value": round((prediction[0]),3), 
        "user_inputs": [str(i) for i in user_inputs],
        }
    return render(request, "crops/prediction.html", context)

