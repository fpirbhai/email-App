import smtplib, ssl
import os

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = "zafrip14@gmail.com"
    password = os.getenv('PASSWORD')

    receiver = "zafrip14@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    send_email("This is a test.")
