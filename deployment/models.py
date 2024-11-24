from django.db import models

# Create your models here.

class MLModel(models.Model):
    name = models.CharField(max_length=255)
    framework = models.CharField(max_length=50, choices=[('tensorflow', 'TensorFlow'), ('pytorch', 'PyTorch')])
    file_path = models.FileField(upload_to='models/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name