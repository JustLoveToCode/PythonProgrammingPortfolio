import smtplib, ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    # The username is the person to send the email
    username = 'glad2r32@gmail.com'
    # This is the password for the App
    # password you create for your Gmail Account
    password = '123456789'

    # This is the person who will receive the gmail email.
    receiver = 'gla3r22e23@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
