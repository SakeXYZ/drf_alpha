# deployment/views.py
import os
import torch
import tensorflow as tf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MLModel
from .serializers import MLModelSerializer


class UploadModelView(APIView):
    def post(self, request):
        serializer = MLModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PredictView(APIView):
    def post(self, request, model_id):
        try:
            ml_model = MLModel.objects.get(id=model_id)
        except MLModel.DoesNotExist:
            return Response({'error': 'Model not found'}, status=status.HTTP_404_NOT_FOUND)

        # Загрузка модели
        model_path = ml_model.file_path.path
        input_data = request.data.get('input_data')

        if not input_data:
            return Response({'error': 'Input data is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Предсказания для TensorFlow
        if ml_model.framework == 'tensorflow':
            model = tf.keras.models.load_model(model_path)
            prediction = model.predict([input_data])

        # Предсказания для PyTorch
        elif ml_model.framework == 'pytorch':
            model = torch.load(model_path)
            model.eval()
            input_tensor = torch.tensor(input_data, dtype=torch.float32)
            with torch.no_grad():
                prediction = model(input_tensor).tolist()

        else:
            return Response({'error': 'Unsupported framework'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'prediction': prediction}, status=status.HTTP_200_OK)
