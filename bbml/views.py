from django.http import JsonResponse
from .models import Prediction
from .serializers import PredictionSerializer

import requests;

def data():
    url = "https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations.json?type=tidepredictions&units=english"
    response = requests.get(url);
    data = response.json()["stations"]
    print(data)

def getPredictions(request):
    predictions = Prediction.objects.all()
    serializer = PredictionSerializer(predictions, many=True)
    return JsonResponse(serializer.data, safe=False)
