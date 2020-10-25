import os
import smtplib
import imghdr
from email.message import EmailMessage
import re
import time
import datetime

RECIPIENT = input("To:")

date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

MESSAGE_SUBJECT = input("Subject: ")
MESSAGE_CONTENTS = input("Main content: ") + "\n\n" + date_time

EMAIL_ADDRESS = 'EMAIL'
EMAIL_PASSWORD = 'GMAIL PASSWORD'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    msg = EmailMessage()
    msg['Subject'] = MESSAGE_SUBJECT
    msg['From'] = EMAIL_ADDRESS
    msg.set_content(MESSAGE_CONTENTS)
    msg['To'] = RECIPIENT
    smtp.send_message(msg)

print("Email has been sent to: " + RECIPIENT + "\nWith the Subject: " + MESSAGE_SUBJECT + "\nWith the contents: " + MESSAGE_CONTENTS + "\nfrom " + EMAIL_ADDRESS + " at:" + date_time)
