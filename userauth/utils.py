from django.conf import settings
from sib_api_v3_sdk import ApiClient, Configuration, TransactionalEmailsApi, SendSmtpEmail


def sendMail(subject, html_content, sender_email, recipient_email):
    configuration = Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY  # Your Brevo key

    api_client = ApiClient(configuration)
    api_instance = TransactionalEmailsApi(api_client)

    send_smtp_email = SendSmtpEmail(
        to=[{"email": recipient_email}],  # ✅ Correct field name
        html_content=html_content,
        subject=subject,
        sender={"email": sender_email},
    )

    try:
        api_instance.send_transac_email(send_smtp_email)
        print("✅ Email sent successfully")
    except Exception as e:
        print("❌ Error sending email:", e)
