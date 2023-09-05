import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 465

sender_email = "SENDER"
receiver_email = "RECEIVER"
password = "PASSWORD"


message = MIMEMultipart("related")
message["Subject"] = "Test Email"
message["From"] = sender_email
message["To"] = receiver_email

html = """
"""

body = MIMEText(html, "html")
message.attach(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())