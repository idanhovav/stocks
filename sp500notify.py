from datetime import date, timedelta
import requests
import smtplib
import os
from email.mime.text import MIMEText

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

sender = "s&p500notify"
recipient = "idan61b@gmail.com"
with open('priv/p.txt', 'r') as p:
    pd = p.read().replace('\n', "")
with open('priv/alpha_vantage_key.txt', 'r') as av:
    apikey = av.read().replace('\n', "")
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
	server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server.login(recipient, pd)
	server.sendmail(sender, recipient, str(create_sp500_email(sender, recipient)))
	server.close()

def get_stock_daily_drop(symbol):
	today = date.today()
	today_str = today.isoformat()
	yesterday_str = (today + timedelta(days=-1)).isoformat()
	response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+symbol+"&apikey="+apikey+"&outputsize=compact")
	response_data = response.json()["Time Series (Daily)"]
	today_opening_price = response_data[today_str]["1. open"]
	yesterday_opening_price = response_data[yesterday_str]["1. open"]
	return float(yesterday_opening_price) - float(today_opening_price)
		
def get_spy_drop():
	return get_stock_daily_drop("SPY")

if get_spy_drop():
	send_sp500_email()