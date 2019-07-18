# -*- coding: utf-8 -*-
# Python code to illustrate Sending mail from  
# your Gmail account  

import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP() 
s.connect("smtp.gmail.com",587)
s.ehlo()
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("scrapper137@gmail.com", "dontgotosleep") 
  
# message to be sent 
message = "Message_you_need_to_send"
  
# sending the mail 
s.sendmail("scrapper137@gmail.com", "scrapper137@gmail.com", message) 
  
# terminating the session 
s.quit() 