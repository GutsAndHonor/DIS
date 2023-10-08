from django.db import models

class Prediction(models.Model):
    cilt_probability = models.TextChoices("RiskProbability", "LOW, MEDIUM, HIGH")
    class Coordinates(models.Model):
        latitude = models.FloatField
        longitude = models.FloatField
    station_ID = models.CharField(max_length=20)
    value = models.FloatField