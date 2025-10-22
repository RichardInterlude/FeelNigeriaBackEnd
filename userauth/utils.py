from django.conf import settings  # use settings instead of global_settings
from sib_api_v3_sdk import ApiClient, Configuration
from sib_api_v3_sdk.api.transactional_emails_api import TransactionalEmailsApi
from sib_api_v3_sdk.models.send_smtp_email import SendSmtpEmail

def sendMail(to_email, username, activation_link):
    # Configure API key
    configuration = Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY  # Replace with your Brevo API key

    with ApiClient(configuration) as api_client:
        api_instance = TransactionalEmailsApi(api_client)

        # Construct the email
        email = SendSmtpEmail(
            to=[{"email": to_email, "name": username}],
            sender={"name": "FeelNigeria", "email": settings.BREVO_SENDER_EMAIL},  # Replace with verified sender
            subject="Activate Your Account",
            html_content=f"""
                <html>
                    <body>
                        <p>Hi {username},</p>
                        <p>Click <a href="{activation_link}">here</a> to activate your account.</p>
                    </body>
                </html>
            """
        )

        # Send the email
        try:
            api_instance.send_transac_email(email)
            print(f"Activation email sent to {to_email}")
        except Exception as e:
            print(f"Error sending email: {e}")















