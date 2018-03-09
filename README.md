Idan Hovav

This is a repository of tools for trading stocks.

# Ideas include:
* A script that pings me if the S&P 500 goes under a certain value
* That's all I've got

#File Descriptions:
##sp500notify.py
This script emails me when the ETF tracking the S&P 500 (SPY) drops by 5 points over a day of trade. The script uses the [AlphaVantage](https://www.alphavantage.co/) API to get realtime data. I use `smtplib` to send the email. I also utilize Apple's Automator program to run this script every day automatically.
