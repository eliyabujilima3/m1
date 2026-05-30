import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

message = EmailMessage()
message['Subject'] = 'Test email from Portfolio Clouds'
message['From'] = 'sender@example.com'
message['To'] = 'recipient@example.com'
message.set_content('This is a test message from the portfolio backend.')

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        print('Connected to SMTP server. Update credentials before sending email.')
except Exception as exc:
    print(f'Unable to connect to SMTP server: {exc}')
