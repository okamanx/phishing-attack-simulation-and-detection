# phishing_simulation/email_simulator.py
# Simulates sending phishing emails for awareness testing

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# HTML template for a fake Instagram security alert
INSTAGRAM_PHISH_HTML = '''
<html>
  <body style="font-family: Arial, sans-serif; background: #fafafa; padding: 20px;">
    <div style="max-width: 400px; margin: auto; background: #fff; border: 1px solid #dbdbdb; border-radius: 8px; padding: 24px;">
      <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" style="width: 60px; display: block; margin: 0 auto 16px auto;">
      <h2 style="color: #262626; text-align: center;">Security Alert</h2>
      <p style="color: #262626;">We detected suspicious login activity on your Instagram account. Please verify your account to secure it.</p>
      <div style="text-align: center; margin: 24px 0;">
        <a href="{phish_link}" style="background: #3897f0; color: #fff; padding: 12px 24px; border-radius: 4px; text-decoration: none; font-weight: bold;">Verify Account</a>
      </div>
      <p style="color: #8e8e8e; font-size: 13px;">If you did not attempt to log in, please secure your account immediately.</p>
      <div style="text-align: center; color: #8e8e8e; font-size: 12px; margin-top: 16px;">© 2024 Instagram from Meta</div>
    </div>
  </body>
</html>
'''

def send_phishing_email(smtp_server, smtp_port, smtp_user, smtp_pass, to_email, subject, phish_link):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = to_email
    html_content = INSTAGRAM_PHISH_HTML.format(phish_link=phish_link)
    part = MIMEText(html_content, 'html')
    msg.attach(part)
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_user, to_email, msg.as_string())
        print(f"[SENT] Phishing email sent to {to_email}")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")

if __name__ == "__main__":
    print("--- Phishing Email Simulator ---")
    smtp_server = input("SMTP server (e.g., smtp.gmail.com): ")
    smtp_port = int(input("SMTP port (e.g., 465 for SSL): "))
    smtp_user = input("SMTP username (your email): ")
    smtp_pass = input("SMTP password (input will be visible): ")
    to_email = input("Recipient email: ")
    subject = input("Email subject [default: Instagram Security Alert]: ") or "Instagram Security Alert"
    phish_link = input("Phishing link (e.g., http://127.0.0.1:5000/): ")
    send_phishing_email(smtp_server, smtp_port, smtp_user, smtp_pass, to_email, subject, phish_link)

"""
How it works:
- Prompts for SMTP credentials, recipient, subject, and phishing link.
- Sends a realistic Instagram-style phishing email to the recipient.
- The email contains a 'Verify Account' button linking to your phishing website simulator.
- For safety, use a test account and never use for malicious purposes.
""" 