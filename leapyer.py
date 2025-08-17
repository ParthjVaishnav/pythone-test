from datetime import date, datetime


def age_and_leap_years() :
    # Take user input
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

    # Convert string to datetime object
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = date.today()

    # Calculate age
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    # Find leap years after birth year
    leap_years = []
    for year in range(birthdate.year + 1, today.year + 1) :
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
            leap_years.append(year)

    # Print results
    print(f"Your current age is {age} years.")
    print(f"Leap years after your birthdate: {leap_years}")


# Run program
age_and_leap_years()
