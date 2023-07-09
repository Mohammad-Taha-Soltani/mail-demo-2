from email.message import EmailMessage
import smtplib


def send_mail(sender_config, reciver, subject='BaseSubject', content='BaseContent'):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_config['HOST_USER']
    msg['To'] = reciver
    msg.set_content(content)

    with smtplib.SMTP_SSL(sender_config['HOST'], sender_config['PORT_SSL']) as server:
        server.login(sender_config['HOST_USER'], sender_config['HOST_PASSWORD'])
        server.send_message(msg)
