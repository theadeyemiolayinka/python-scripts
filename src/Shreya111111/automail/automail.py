import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
SMTP_SERVER = 'your-smtp-server.com'
SMTP_PORT = 587  # The port may vary depending on your email service provider
EMAIL_ADDRESS = 'your-email@example.com'
EMAIL_PASSWORD = 'your-email-password'
CUSTOMER_EMAIL = 'customer@example.com'

# Create an SMTP connection
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

# Create an email response
response_subject = "Re: Your Query"
response_body = """
Dear Customer,

Thank you for reaching out to us. Here is a response to your query:

[Your response here]

If you have any further questions or concerns, please don't hesitate to contact us.

Best regards,
Your Name
Your Company
"""

# Create an email message
msg = MIMEMultipart()
msg['From'] = EMAIL_ADDRESS
msg['To'] = CUSTOMER_EMAIL
msg['Subject'] = response_subject
msg.attach(MIMEText(response_body, 'plain'))

# Send the email
server.sendmail(EMAIL_ADDRESS, CUSTOMER_EMAIL, msg.as_string())

# Close the SMTP connection
server.quit()
