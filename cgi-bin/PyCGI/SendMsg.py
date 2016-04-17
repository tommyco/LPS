#!/usr/bin/python

# Import smtplib for the actual sending function
import smtplib
from ConfigParser import SafeConfigParser

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.header import Header

parser = SafeConfigParser()
parser.read('LPS.ini')

# In DEV
#mode = "_dev"
# In LIVE
mode = "_live"

# SMTP credential & receiving email account
smtp_host = parser.get('smtp' + mode, 'smtp_host')
smtp_login = parser.get('smtp' + mode, 'smtp_login')
smtp_password = parser.get('smtp' + mode, 'smtp_password')
rc_login = parser.get('smtp' + mode, 'rc_login')

def SendMsg(subject, name, from_email, phone, email_text):
   recipients_emails = [rc_login]

   # Create a text/plain message
   email_text = 'Name: ' + name + '\n\r' + 'Email: ' + from_email + '\n\r' + 'Phone: ' + phone + '\n\r\n\r' + email_text

   msg = MIMEText(email_text, 'plain', 'utf-8')

   # me == the sender's email address
   # you == the recipient's email address
   msg['Subject'] = Header(subject, 'utf-8')
   msg['From'] = smtp_login
   msg['To'] = ", ".join(recipients_emails)
   msg['reply-to'] = from_email

   # Send the message via our own SMTP server, but don't include the
   # envelope header.
   s = smtplib.SMTP(smtp_host, 587, timeout=10)
   s.set_debuglevel(1)

   try:
      s.starttls()
      s.login(smtp_login, smtp_password)
      s.sendmail(msg['From'], recipients_emails, msg.as_string())
   finally:
      s.quit()
   return


