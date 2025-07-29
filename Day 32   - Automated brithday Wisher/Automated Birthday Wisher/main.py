##########################################---Hard Starting Project---##################################################
##1. Update the birthdays.csv with your friends & family's details.
##HINT: Make sure one of the entries matches today's date for testing purposes.

##2. Check if today matches a birthday in the birthdays.csv
##HINT 1: Only the month and day matter.
##HINT 2: You could create a dictionary from birthdays.csv that looks like this:
##birthdays_dict = {
#     (month, day): data_row
# }
##HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
##if (today_month, today_day) in birthdays_dict:

#----------------------------------------------------Set-up and Variables----------------------------------------------#
import pandas as pd
import datetime as dt


#---------------------------------------------Get the Birthday CSV and check for month and days-------------------------#
data = pd.read_csv("./birthdays.csv")
# Todo: creates the items in the csv file into a list of dictionaries.
dataset= data.to_dict(orient= "records")
print (dataset)
# Todo: running the check for months and days
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

for i in dataset:
    if i["month"]==today_month and i["day"]==today_day:
        



#----------------------------------Only case if the Birthday is true then pick a random template-----------------------#




#------------------------------------Send the email to them at a certain time------------------------------------------#