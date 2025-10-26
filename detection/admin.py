from django.contrib import admin
from .models import DetectionHistory

@admin.register(DetectionHistory)
class DetectionHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'predicted_disease', 'confidence', 'created_at']
    list_filter = ['predicted_disease', 'created_at']
    search_fields = ['user__username', 'predicted_disease']