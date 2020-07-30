import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def Spoof():
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = input("From Email (gmail) : ")
    password = input(f"Password for {sender_email}: ")
    #input("Type your password and press enter: ")
    html = open("/Users/snowden/Programmation/python/webProgrammation/security/html/rawfile.html", 'r').read()
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        Message = MIMEMultipart('alternative')
        Message['Subject'] = "Information Free.fr"
        Message['From'] = sender_email
        Message['To'] = input("destination Email Adress: ")
        html = MIMEText(html, 'html')
        Message.attach(html)
        server.sendmail(from_addr=sender_email, to_addrs=Message['To'], msg=Message.as_string())
        

        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()



if __name__ == "__main__":
  Spoof()