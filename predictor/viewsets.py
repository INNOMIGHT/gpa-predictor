from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import pickle
from .models import Prediction
from .serializers import PredictionSerializer
import os
import joblib



class PredictionsViewSet(ModelViewSet):

    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer

    @action(detail=False, methods=["POST"])
    def predict_gpa(self, request):
        # Get the directory of the current module
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # Construct the path to your pickle file relative to the current directory
        pickle_file_path = os.path.join(current_dir, 'gpa_prediction_model.pkl')
        hours_studied = float(request.data.get("hours_studied"))
        w, b = joblib.load(pickle_file_path)

        predicted_gpa = w * hours_studied + b
        new_prediction = Prediction(hours_studied=hours_studied, predicted_gpa=predicted_gpa)
        new_prediction.save()
        #
        serializer = self.get_serializer(new_prediction)

        return Response(serializer.data, status=status.HTTP_200_OK)

