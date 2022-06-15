import smtplib, ssl
from email.message import EmailMessage
from auth import *

def send(subject, body):
    port = 465  # For SSL
    smtp_server = "smtp.qq.com"

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg)
    except smtplib.SMTPAuthenticationError as e:
        logging.error(e.smtp_code, e.smtp_error.decode("GBK"))


if __name__ == "__main__":
    import sys
    subject = (sys.argv[1:2] + ["Robot-sent Message"])[0]
    body = (sys.argv[2:3] + ["FYI"])[0]
    print(subject, body)
    send(subject, body)
