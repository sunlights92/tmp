import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
  
fromaddr = "deepa.it26@gmail.com"
toaddr = "deepa.it26@gmail.com"
  
msg = MIMEMultipart()
 
msg['From'] = fromaddr
 
msg['To'] = toaddr
 
msg['Subject'] = "Testing"
 
body = "Testing............Thanks for ur patience...:-)"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "image.jpg"
attachment = open(filename, "rb")
 
p = MIMEBase('application', 'plain')
 
p.set_payload((attachment).read())
 
encoders.encode_base64(p)
  
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(p)
 
s = smtplib.SMTP('smtp.gmail.com', 587)
 
s.starttls()
 
s.login("deepa.it26@gmail.com", "password")
 
text = "I got msg"
 
s.sendmail(fromaddr, toaddr, text)
 
s.quit()
