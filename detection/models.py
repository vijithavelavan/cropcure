from django.db import models
from django.contrib.auth.models import User

class DetectionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    predicted_disease = models.CharField(max_length=100)
    confidence = models.FloatField()
    symptoms = models.TextField()
    treatment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.predicted_disease}"