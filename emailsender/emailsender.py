from email.message import EmailMessage
from prop import password
import ssl
import smtplib


email_sender = 'satyamurthy18feb23@gmail.com'
email_password = password

email_receiver = 'joxabib453@v2ssr.com' # you can use temp-mail.org

subject ="don't forget to subscribe"
body = """Test body message
sfdsdf
sdfsdfsdf
sdfsdf"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject']= subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
