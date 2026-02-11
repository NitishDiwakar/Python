python3 - <<'EOF'
import smtplib
import ssl
from email.message import EmailMessage
from datetime import date

SMTP_SERVER = "smtp.zoho.in"
SMTP_PORT = 587
USERNAME = "username@zohomail.in"
PASSWORD = "PASSWORD"

msg = EmailMessage()
msg["From"] = USERNAME
msg["To"] = "actual_mail@gmail.com"
msg["Subject"] = f"Python Test - {date.today()}"
msg.set_content("Hello from Python on Fedora server.")

context = ssl.create_default_context()

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(USERNAME, PASSWORD)
    server.send_message(msg)

print("Mail sent successfully.")
EOF