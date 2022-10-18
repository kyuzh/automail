import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = ""
EMAIL_PASSWORSD = ""

contacts =[]
msg = EmailMessage()
msg['Subject'] = 'Grab dinner'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ','.join(contacts)
msg.set_content('how about dinner')

# mail attachment
"""
with open('img.jpg', 'rb') as f:
    file_data = f.read()
    #image file
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
"""
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORSD)

    smtp.send_message(msg)
