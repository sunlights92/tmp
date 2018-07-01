import smtplib

s = smtplib.SMTP("smtp.gmail.com",587)

#tolist = ["deepa.it26@gmail.com","sunlights92@gmail.com"]
s.starttls()
s.login("deepa.it26@gmail.com","deepadeep@26")

message = '''\
    From:deepa
    Subject:Testing mail
    
    Testing.......thanks for ur patience '''

s.sendmail('deepa.it26@gmail.com',"deepa.it26@gmail.com",message)

#s.expn("deepa.it26@gmail.com")
s.quit()

