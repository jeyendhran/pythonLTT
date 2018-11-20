# import the smtplib module. It should be included in Python by default
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = "jeyendhran.s@hcl.com"
# set up the SMTP server
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()




s.login(MY_ADDRESS, "Jeyen@95sudhar")

msg = MIMEMultipart()  # create a message

message = "Hai"

# setup the parameters of the message
msg['From'] = MY_ADDRESS
msg['To'] = 'nivedhita.s@hcl.com'
msg['Subject'] = "This is TEST"
# add in the message body
msg.attach(MIMEText(message, 'plain'))
# send the message via the server set up earlier.
s.send_message(msg)