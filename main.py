
import pandas
import datetime as dt
import random
import smtplib

today = dt.datetime.now()
today_month_day = (today.month, today.day)
with open("birthdays.csv") as data:
    birthday_list = pandas.read_csv(data)
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in
                      birthday_list.iterrows()}


if today_month_day in birthdays_dict:
    birthday_person = birthdays_dict[today_month_day]["name"]
    letter_choice = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_choice}.txt") as letter:
        content = letter.read()
        letter_to_send = content.replace("[NAME]", f"{birthday_person}")


def send_email(msg, sender, reception, password):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(from_addr=sender, to_addrs=reception, msg=f"Subject: HAPPY BIRTHDAY DEAR\n\n{msg}")


sender_email = input("Enter U r email address: ")
sender_password = input("Enter u r password: ")
reception_email = birthdays_dict[today_month_day]["email"]
send_email(letter_to_send, sender_email, reception_email, sender_password)






