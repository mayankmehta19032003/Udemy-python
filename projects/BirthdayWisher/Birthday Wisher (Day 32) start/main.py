# import smtplib

# my_email = "mayankmehta880@gmail.com"
# password = "mtndew123@"  # Avoid hardcoding passwords like this!

# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs=my_email,
#     msg="Subject:Hello\n\nThis is example"
# )
# connection.close()
import datetime as dt
time =dt.datetime.now()
print(time)