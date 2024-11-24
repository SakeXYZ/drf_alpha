from django.urls import path
from .views import UploadModelView, PredictView

urlpatterns = [
    path('models/upload/', UploadModelView.as_view(), name='upload_model'),
    path('models/<int:model_id>/predict/', PredictView.as_view(), name='predict'),
]