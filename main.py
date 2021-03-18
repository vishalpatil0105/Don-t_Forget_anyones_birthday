# importing modules
import pandas
import datetime as dt
import random
import smtplib

#getting hold of todays date and month
today = dt.datetime.now()
today_month_day = (today.month, today.day)

# Open csv file in which we stored all birthdates
with open("birthdays.csv") as data:
    birthday_list = pandas.read_csv(data)
    # To get hold of birthday and month for later comparision
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in
                      birthday_list.iterrows()}

# checking todays date with dates in csv files
if today_month_day in birthdays_dict:
    # getting name of birthday person
    birthday_person = birthdays_dict[today_month_day]["name"]
    # for letter prototype
    letter_choice = random.randint(1, 3)
    # opening letter prototype
    with open(f"letter_templates/letter_{letter_choice}.txt") as letter:
        # reading content
        content = letter.read()
        # Adding birthday person name in letter prototype
        letter_to_send = content.replace("[NAME]", f"{birthday_person}")

# To send msg to birthday person 
def send_email(msg, sender, reception, password):
    #  Using smtplib module
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        # sending actual email 
        connection.sendmail(from_addr=sender, to_addrs=reception, msg=f"Subject: HAPPY BIRTHDAY DEAR\n\n{msg}")


# all input from user end {Here U can make your email_id and password as default CONSTANT }
sender_email = input("Enter U r email address: ")
sender_password = input("Enter u r password: ")
reception_email = birthdays_dict[today_month_day]["email"]
# Calling function
send_email(letter_to_send, sender_email, reception_email, sender_password)






