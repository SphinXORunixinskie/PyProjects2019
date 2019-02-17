import smtplib
import config
import encrypt_msg
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(config.fromaddr, config.password)
msg = "Hey dude what is up"
server.sendmail(config.fromaddr, config.toaddr, msg)
server.quit()