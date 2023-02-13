from decouple import config
from django.core.mail import EmailMessage


def send_mail():
    try:
        MAIL_TEST = config("MAIL_TEST")
        mail = EmailMessage(
            subject="title",
            from_email=MAIL_TEST,
            to=[MAIL_TEST],
            body="Chamado Criado com sucesso",
            headers={"Replay-To": MAIL_TEST},
            fail_silently=False,
        )
        mail.send()

    except Exception as error:
        print("Internal error:", error)
        raise
