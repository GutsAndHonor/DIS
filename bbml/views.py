from django.http import JsonResponse
from .models import Prediction
from .serializers import PredictionSerializer

def getPredictions(request):
    predictions = Prediction.objects.all()
    serializer = PredictionSerializer(predictions, many=True)
    return JsonResponse(serializer.data, safe=False)
