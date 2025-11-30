from rest_framework.views import APIView
from rest_framework.response import Response
from card.models import CardApplication
from card.services.ptb_service import PTBService

class CheckBalanceAndDebitView(APIView):

    def post(self, request, pk):
        app = CardApplication.objects.get(id=pk, user=request.user)

        balance = PTBService.check_balance(app.ptb_account_number, fee=2000)

        if not balance["sufficient"]:
            app.status = "INSUFFICIENT_FUNDS"
            app.save()
            return Response({"error": "Insufficient funds"}, status=402)

        debit = PTBService.debit_account(app.ptb_account_number, 2000)

        app.reference = debit["reference"]
        app.status = "DEBIT_PENDING"
        app.save()

        return Response({
            "message": "Debit initiated. Waiting for PTB callback.",
            "reference": debit["reference"]
        })
