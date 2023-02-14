from decouple import config
from django.core.mail import send_mail


def send_mail2():
    try:
        MAIL_TEST = config("MAIL_TEST")
        send_mail(
            subject="title",
            message="teste teste",
            from_email=MAIL_TEST,
            recipient_list=[MAIL_TEST],
            auth_user=MAIL_TEST,
            auth_password=config("EMAIL_HOST_PASSWORD"),
            fail_silently=False,
        )
        print("send mail!!!!")

    except Exception as error:
        print("Internal error:", error)
        raise
