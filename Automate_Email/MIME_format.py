import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config 
import email.utils

fromaddr = config.fromaddr
toaddr = config.toaddr
msg = MIMEMultipart()
msg['Subject'] = 'Hello'
msg['To'] = email.utils.formataddr(('Recipient', toaddr))
msg['From'] = email.utils.formataddr(('Nicole', fromaddr))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, config.password)
text = msg.as_string()
print 'Text is:', text
server.sendmail(fromaddr, toaddr, text)
server.quit()