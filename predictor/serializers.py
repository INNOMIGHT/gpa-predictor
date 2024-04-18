from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import Prediction


class PredictionSerializer(ModelSerializer):

    class Meta:
        model = Prediction
        fields = "__all__"
