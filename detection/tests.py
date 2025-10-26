from django.test import TestCase
from django.contrib.auth.models import User
from .models import DetectionHistory

class DetectionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
    
    def test_detection_history_creation(self):
        history = DetectionHistory.objects.create(
            user=self.user,
            predicted_disease='Healthy',
            confidence=0.95,
            symptoms='No symptoms',
            treatment='No treatment needed'
        )
        self.assertEqual(history.predicted_disease, 'Healthy')
        self.assertEqual(history.confidence, 0.95)