from decouple import config
from django.core.mail import send_mail


def send_email(recipient_list, subject, message):
    try:
        EMAIL_SUPPORT = config("EMAIL_SUPPORT")
        EMAIL_HOST_USER = config("EMAIL_HOST_USER")

        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=recipient_list,
            auth_user=EMAIL_HOST_USER,
            auth_password=config("EMAIL_HOST_PASSWORD"),
            fail_silently=True,
        )
        print("send mail!!!!")

    except Exception as error:
        print("Internal error:", error)
        raise
