from rest_framework.routers import SimpleRouter


from .viewsets import PredictionsViewSet

api_router = SimpleRouter()

api_router.register("prediction", PredictionsViewSet, basename="prediction-api")

api_routes = api_router.urls

urlpatterns = api_routes + []