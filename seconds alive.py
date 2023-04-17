import datetime


def calculate_age_in_seconds(date_of_birth):
    # Calculate the number of seconds in a year, accounting for leap years
    seconds_per_year = 365.2425 * 24 * 60 * 60

    # Calculate the age in seconds
    age_in_seconds = (datetime.datetime.now() - date_of_birth).total_seconds()


    return age_in_seconds


while True:
    print("enter your date of birth")
    # getting date of birth from user
    day_str = input("day of birth\n")
    month_str = input("month of birth\n")
    year_str = input("year of birth\n")
    # converting the string inputs  into integer for calculations
    year = int(year_str)
    month = int(month_str)
    day = int(day_str)
    dob = datetime.datetime(year, month, day)  # May 23, 1990
    age_in_seconds = calculate_age_in_seconds(dob)
    print("You have been alive for approximately", age_in_seconds, "seconds.")
