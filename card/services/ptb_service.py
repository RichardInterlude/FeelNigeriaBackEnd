import requests
import uuid

PTB_BASE_URL = "https://dummy-premiumtrust.com/api"  # Dummy endpoint

class PTBService:
    
    @staticmethod
    def check_account(account_number):
        # Dummy response simulating PTB
        return {"valid": True, "message": "Account validated"}

    @staticmethod
    def send_otp(account_number):
        # In a real system PTB sends OTP and redirects; we just fake
        return {"status": "otp_sent"}

    @staticmethod
    def check_balance(account_number, fee):
        # Dummy: randomly say balance is enough
        return {"sufficient": True}

    @staticmethod
    def debit_account(account_number, amount):
        # Generate fake reference for tracking
        ref = "FEEL-" + uuid.uuid4().hex[:12].upper()

        # In real life PTB would NOT return success immediately
        return {"reference": ref, "status": "debit_processing"}
