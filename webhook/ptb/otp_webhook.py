from rest_framework.views import APIView
from rest_framework.response import Response
from card.models import CardApplication
from webhook.models import WebhookLog

class OTPWebhookView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        WebhookLog.objects.create(event_type="otp", payload=request.data)

        acct = request.data.get("account_number")
        status_val = request.data.get("status")

        if status_val != "otp_verified":
            return Response({"error": "OTP failed"}, status=400)

        app = CardApplication.objects.filter(ptb_account_number=acct).last()
        app.status = "OTP_VERIFIED"
        app.save()

        return Response({"message": "OTP verified"})
