from django.db import models
from django.contrib.auth.models import User

class CardApplication(models.Model):
    STATUS_CHOICES = [
        ("INITIATED", "Initiated"),
        ("ACCOUNT_SUBMITTED", "Account Submitted"),
        ("OTP_VERIFIED", "OTP Verified"),
        ("INSUFFICIENT_FUNDS", "Insufficient Funds"),
        ("DEBIT_PENDING", "Debit Pending"),
        ("DEBIT_SUCCESS", "Debit Success"),
        ("DEBIT_FAILED", "Debit Failed"),
        ("COMPLETED", "Completed"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ptb_account_number = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="INITIATED")
    reference = models.CharField(max_length=50, blank=True, null=True)
    pickup_token = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"
