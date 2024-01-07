import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # This is the sender email address
    sender = "This is the Sender Email Address"
    password = "This is the App Password"

    # The person who will receive the email
    # on the other side is the receiver
    receiver = 'This is the person receiving the Email'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

# Generating the App Password
# https://support.google.com/accounts/answer/185833?hl=en
# Generating the App Password for Google:
# Go to your Google Account
# Select Security
# Under the Signing in to Google,
# Select the 2 Steps Verification.
# At the Bottom of the Page, Select the App Password
# Enter a name for your App Password
# Select Generate
# The App Password is what you have entered on the screen.
# Select Done

