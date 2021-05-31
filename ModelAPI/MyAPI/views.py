from django.db import models
from django.shortcuts import render
from .forms import PredictionForm

from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.parsers import JSONParser
from .models import predictions
from .serializers import predictionsSerializers
import pickle as pkl
import json
import numpy as np
import pandas as pd
import sklearn
from sklearn import preprocessing
import joblib
from sklearn.preprocessing import MinMaxScaler
# Create your views here.


class PredictionView(viewsets.ModelViewSet):
    queryset = predictions.objects.all()
    serializers_class = predictionsSerializers



# @api_view(["POST"])
def predictionsResults(mydata):
    try:
        scal=MinMaxScaler()
        model = pkl.load(open("E:/Office/Heart Disease/API/ModelAPI/MyAPI/model/model.p","rb"))
        # model = joblib.load("E:/Office/Heart Disease/API/ModelAPI/MyAPI/model/model.p")
        feat=['age','sex','cp', 'trestbps', 'chol','fbs','restecg','thalach' ,'exang','oldpeak' ,'slope','ca', 'thal']
        df_new=mydata[feat]
        print(df_new)
        unit = np.array(df_new.values)
        print(type(unit))
        unit = unit.reshape(1,-1)
        pred = model.predict(unit)
        print(pred)
        if pred == 0:
            result = 'Low Risk of Heart Disease!'
            
        else:
            result = 'High Risk of Heart Attack!'
        return result
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

def apiView(request):
    if request.method=='POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            age = int(form.cleaned_data['age'])
            # print(type(age))
            sex = int(form.cleaned_data['sex'])
            cp = int(form.cleaned_data['cp'])
            trestbps = int(form.cleaned_data['trestbps'])
            restecg = int(form.cleaned_data['restecg'])
            chol = int(form.cleaned_data['chol'])
            fbs = int(form.cleaned_data['fbs'])
            thalach = int(form.cleaned_data['thalach'])
            exang = int(form.cleaned_data['exang'])
            oldpeak = float(form.cleaned_data['oldpeak'])
            slope = int(form.cleaned_data['slope'])
            ca = int(form.cleaned_data['ca'])
            thal = int(form.cleaned_data['thal'])
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index=[0])
            # print(type(df.values))
            print(df)
            results = predictionsResults(df)
            messages.success(request,'Result: {}'.format(results))

    
    form=PredictionForm()

    return render(request, 'MyForm/forms.html',{'form':form})
