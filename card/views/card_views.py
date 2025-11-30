from rest_framework.views import APIView
from rest_framework.response import Response
from card.models import CardApplication
from card.serializers import SubmitAccountSerializer
from card.services.ptb_service import PTBService


class StartCardApplicationView(APIView):
    
    def post(self, request):
        app = CardApplication.objects.create(user=request.user)
        return Response({"message": "Application started", "application_id": app.id})


class SubmitAccountNumberView(APIView):

    def post(self, request, pk):
        serializer = SubmitAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        app = CardApplication.objects.get(id=pk, user=request.user)

        acct = serializer.validated_data['account_number']

        result = PTBService.check_account(acct)

        if not result["valid"]:
            app.status = "ACCOUNT_INVALID"
            app.save()
            return Response({"message": "Invalid PTB account"}, status=400)

        app.ptb_account_number = acct
        app.status = "ACCOUNT_SUBMITTED"
        app.save()

        # Redirect user to PTB OTP page
        redirect_url = f"https://dummy-ptb.com/otp?acct={acct}"

        return Response({"redirect_url": redirect_url})