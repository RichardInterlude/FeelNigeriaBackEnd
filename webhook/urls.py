from django.urls import path
from webhook.ptb.otp_webhook import OTPWebhookView
from webhook.ptb.debit_webhook import DebitWebhookView

urlpatterns = [
    path("ptb/otp/", OTPWebhookView.as_view()),
    path("ptb/debit/", DebitWebhookView.as_view()),
]
