import  smtplib

my_email = "billyjackson@gmail.com"
password = "abcd1234"

with  smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="appbrewerybesting@yahoo.com",
            msg="hello")

#import datetime as dt

#now = dt.datetime.now()
#year = now.year

