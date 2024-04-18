from django.db import models

class Prediction(models.Model):

    hours_studied = models.IntegerField()
    predicted_gpa = models.FloatField(max_length=5)

