import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "freemail.contacts@gmail.com"
you = "louispuyo@yahoo.fr"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).

html = open("/Users/snowden/Programmation/python/webProgrammation/security/html/index.html", 'r').read()


# Record the MIME types of both parts - text/plain and text/html.
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.

msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email = "freemail.contacts@gmail.com"
password = "gringo007"
s.login(sender_email, password)
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg=msg)
s.quit()