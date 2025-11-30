from django.db import models

class WebhookLog(models.Model):
    event_type = models.CharField(max_length=50)
    payload = models.JSONField()
    received_at = models.DateTimeField(auto_now_add=True)
