#!/usr/bin/env python
##### coding : utf-8
import os
import smtplib
import string
import sys
 
from email import Encoders
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate
 
#----------------------------------------------------------------------
def send_email_with_attachment(subject, body_text, to_emails, cc_emails, bcc_emails, file_to_attach):
    """
    Send an email with an attachment
    """

    header = 'Content-Disposition', 'attachment; filename="%s"' % file_to_attach
    
    host = "smtp.sina.com"
    from_addr = "polyupdate@sina.com"
    
    # create the message
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    if body_text:
        msg.attach( MIMEText(body_text,'plain','utf-8') )
 
    msg["To"] = ', '.join(to_emails)
    msg["cc"] = ', '.join(cc_emails)
 
    attachment = MIMEBase('application', "octet-stream")
    try:
        with open(file_to_attach, "rb") as fh:
            data = fh.read()
        attachment.set_payload( data )
        Encoders.encode_base64(attachment)
        attachment.add_header(*header)
        msg.attach(attachment)
    except IOError:
        msg = "Error opening attachment file %s" % file_to_attach
        print msg
        sys.exit(1)
 
    emails = to_emails + cc_emails
 
    server = smtplib.SMTP(host)
    try:
        server.login(from_addr, "polyupdate")
        server.sendmail(from_addr, emails, msg.as_string())
        print("Send Success !")
    except SMTPAuthenticationError:
        print 'SMTPAuthenticationError'
    
    server.quit()
 
if __name__ == "__main__":
    #emails = ["hu.chen@polydata.com.cn","chunjiang.li@polydata.com.cn","tian.xia@polydata.com.cn","wei.zhang@polydata.com.cn"]
    emails = ["hu.chen@polydata.com.cn","chunjiang.li@polydata.com.cn"]
    cc_emails = [""]
    bcc_emails = [""]
 
    subject = sys.argv[1]
    body_text = sys.argv[2]
    path = sys.argv[3]
    
    send_email_with_attachment(subject, body_text, emails, cc_emails, bcc_emails, path)

