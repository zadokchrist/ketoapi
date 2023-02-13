from django.core.mail import EmailMessage
class Util:
    @staticmethod
    def sendMail(data):
        email = EmailMessage(
            subject = data['email_subject'],
            body=data['body'],
            to=[data['email']]
            )
        email.send()