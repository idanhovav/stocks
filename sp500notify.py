import smtplib
from email.mime.text import MIMEText

sender = "s&p500notify"
recipient = "idan61b@gmail.com"
with open('p.txt', 'r') as p:
    pd = p.read().replace('\n', "")
def create_email(sender, recipient, subject, text):
	msg = MIMEText(text)
	msg['Subject'] = subject
	msg['From'] = sender
	msg['To'] = recipient
	return msg

def create_sp500_email(sender, recipient):
	subject = "S&P 500 Drop"
	text = "The S&P 500 Dropped Today. Should I buy?"
	return create_email(sender, recipient, subject, text)

def send_sp500_email():
	server = smtplib.SMTP_SSL("smtp.gmail.com", 465) #port 465 or 587
	#server.ehlo()
	#server.starttls()
	#server.ehlo()
	server.login(recipient, pd)
	server.sendmail(sender, recipient, str(create_sp500_email(sender, recipient)))
	server.close()

send_sp500_email()