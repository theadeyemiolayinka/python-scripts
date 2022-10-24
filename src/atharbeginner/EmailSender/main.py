import smtplib 
from email.message import EmailMessage

email = EmailMessage()                                       ## Creating a object for EmailMessage
email['from'] = 'xyz@gmail.com'                              ## Sender Email
email['to'] = 'abc@gmail.com'                                ## Receiver Email
email['subject'] = 'Hacktoberfest'                           ## Subject of Email
email.set_content("Hello User,\n Thank you for registering to hacktoberfest 2022")  ## Content of email

try:
    server = smtplib.SMTP('smtp.gmail.com',587)                  ## SMTP Session
    server.ehlo()                                       
    server.starttls()                                            ## used to send data between server and client
    server.login("email","password")                             ## login id and password of gmail
    server.send_message(email)                                   ## sending email
    server.quit()                                 
    print("email sent")    
except smtplib.SMTPException:
    print("Error: Unable to send email")                               