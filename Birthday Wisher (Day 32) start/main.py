import smtplib
import random
import datetime as dt
quotes=[]
date=dt.datetime.now()
today=date.weekday()
with open("quotes.txt","r") as f:
    for quote in f.read().split("\n"):
        quotes.append(quote)
message=random.choice(quotes)
if today==0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="jambah1801@gmail.com",password="Aamir@1801")
        connection.sendmail(from_addr="jambah1801@gmail.com",to_addrs="jambah1801@gmail.com",msg=f"subject:Information\n\n{message}")
        connection.close()