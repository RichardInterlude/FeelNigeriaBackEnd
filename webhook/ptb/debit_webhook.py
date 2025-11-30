from rest_framework.views import APIView
from rest_framework.response import Response
from card.models import CardApplication
from webhook.models import WebhookLog

class DebitWebhookView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        WebhookLog.objects.create(event_type="debit", payload=request.data)

        reference = request.data.get("reference")
        status_val = request.data.get("status")

        app = CardApplication.objects.filter(reference=reference).last()

        if status_val == "debit_success":
            app.status = "DEBIT_SUCCESS"
            app.pickup_token = request.data.get("pickup_token")
            app.save()
        else:
            app.status = "DEBIT_FAILED"
            app.save()

        return Response({"message": "Webhook processed"})
