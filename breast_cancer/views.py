from django.http import HttpResponse
from django.shortcuts import render
from joblib import load
import numpy as np


def index(request):
    latest_question_list = []
    context = {"latest_question_list": latest_question_list}

    return render(request, "breast_cancer/home.html", context)

def prediction(request):
    prediction = [0]
    user_inputs=[]
    if request.method == 'POST':
        # Load your machine learning model
        model = load('controller/model/breast_cancer_prediction_model.joblib')

        # Get the input values from the form and convert them to float
        radius_mean = float(request.POST.get('radius_mean'))
        texture_mean = float(request.POST.get('texture_mean'))
        perimeter_mean = float(request.POST.get('perimeter_mean'))
        area_mean = float(request.POST.get('area_mean'))
        smoothness_mean = float(request.POST.get('smoothness_mean'))
        compactness_mean = float(request.POST.get('compactness_mean'))
        concavity_mean = float(request.POST.get('concavity_mean'))
        concave_points_mean = float(request.POST.get('concave_points_mean'))
        symmetry_mean = float(request.POST.get('symmetry_mean'))
        fractal_dimension_mean = float(request.POST.get('fractal_dimension_mean'))

        radius_se = float(request.POST.get('radius_se'))
        texture_se = float(request.POST.get('texture_se'))
        perimeter_se = float(request.POST.get('perimeter_se'))
        area_se = float(request.POST.get('area_se'))
        smoothness_se = float(request.POST.get('smoothness_se'))
        compactness_se = float(request.POST.get('compactness_se'))
        concavity_se = float(request.POST.get('concavity_se'))
        concave_points_se = float(request.POST.get('concave_points_se'))
        symmetry_se = float(request.POST.get('symmetry_se'))
        fractal_dimension_se = float(request.POST.get('fractal_dimension_se'))

        radius_worst = float(request.POST.get('radius_worst'))
        texture_worst = float(request.POST.get('texture_worst'))
        perimeter_worst = float(request.POST.get('perimeter_worst'))
        area_worst = float(request.POST.get('area_worst'))
        smoothness_worst = float(request.POST.get('smoothness_worst'))
        compactness_worst = float(request.POST.get('compactness_worst'))
        concavity_worst = float(request.POST.get('concavity_worst'))
        concave_points_worst = float(request.POST.get('concave_points_worst'))
        symmetry_worst = float(request.POST.get('symmetry_worst'))
        fractal_dimension_worst = float(request.POST.get('fractal_dimension_worst'))

        user_inputs = [
            radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,
            radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,
            radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst
            ]

        input_data = np.array([user_inputs])
        
        prediction = model.predict(input_data)
        print(f"==== Predicted value: {prediction[0]}")
        
    
    if prediction[0] == 'M':
        prediction = "Malignant"
    elif prediction[0] == 'B':
        prediction = "Benign"
    else:
        prediction = "Unknown"
        
    context = {
        "prediction_value": (prediction), 
        "user_inputs": [str(i) for i in user_inputs],
        }
    return render(request, "breast_cancer/prediction.html", context)

