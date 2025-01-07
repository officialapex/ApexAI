import smtplib
from email.mime.text import MIMEText

def send_email_notification(email, subject, message):
    """Sends an email notification."""
    sender = "noreply@apex-ai.com"
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = email

    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("your-email@example.com", "your-password")
            server.sendmail(sender, [email], msg.as_string())
            print(f"Email sent to {email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
