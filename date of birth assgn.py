import calendar

age = int(input("What is your age? \n"))
year = 2017 - age
print("You were born in",year)


month = int(input("\nIn which month were you born? (1 - 12)\n"))
month_string = calendar.month_name[month]
print("You were born in " + month_string)

date = int(input("\nWhat is your date of birth?\n"))
date_string = calendar.day_name[calendar.weekday(year,month,date)]
print("You were born on a",date_string)

print("\n\nYou were born on",date_string,month_string,year)
