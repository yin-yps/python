#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '18310578905@163.com'
receivers = '18310578905@163.com'

mail_stmp = 'smtp.163.com'
mail_user = '18310578905@163.com'
mail_pass = 'yinpeng@263.cn'

messages = MIMEText('Python test email send','plain','utf-8')
messages['from'] = Header("test mail",'utf-8')
messages['to'] = Header("reciver mail",'utf-8')

subject = 'Python SMTP test mail'
messages['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_stmp,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,messages.as_string())
    print('send success')
except smtplib.SMTPException as e:
	print('ERROR:',e)