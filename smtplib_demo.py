#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :usage of stmplib
@Date     :2021/04/28 21:51:13
@Author      :xbMa
'''

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename

'''
Execute this command in console:
python -m smtpd -c DebuggingServer -n localhost:1025
'''
############################
# Send msg only text
sender = 'admin@example.com'
receiver = ['info@example.com']

port = 1025
msg = MIMEText('This is a test email')

msg['Subject'] = 'Test Mail'
msg['From'] = "admin@example.com"
msg['To'] = "info@example.com"

with smtplib.SMTP('localhost', port) as server:
    # server.login('username', 'password')
    server.sendmail(sender, receiver, msg.as_string())
    print("Successfully sent email")

############################
# Send msg with attachment
msg_attach = MIMEMultipart()
msg_attach['Subject'] = 'Test send attachment msg'
msg_attach['From'] = "admin@example.com"
msg_attach['To'] = "info@example.com"

attachment_name = "smtplib_test_file.txt"

with open(attachment_name, 'r') as f:
    part = MIMEApplication(f.read(), Name=basename(attachment_name))

part["content-disposition"] = f'attachment; filename="{basename(attachment_name)}"'
msg_attach.attach(part)

with smtplib.SMTP('localhost', port ) as server:
    # server.login('username', 'password')
    server.sendmail(sender, receiver, msg_attach.as_string())
    print("Successfully sent email")

############################
# Send msg with ssl
sender = 'admin@example.com'
receivers = ['info@example.com']

ssl_port = 465
user = 'admin@example.com'
password = 'password'

msg_ssl = MIMEText('Test send ssl msg')
msg_ssl['Subject'] = 'Test mail'
msg_ssl['From'] = 'admin@example.com'
msg_ssl['To'] = 'info@example.com'

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.websupport.sk", port, context=context) as server:

    server.login(user, password)
    server.sendmail(sender, receivers, msg.as_string())
    print('mail successfully sent')