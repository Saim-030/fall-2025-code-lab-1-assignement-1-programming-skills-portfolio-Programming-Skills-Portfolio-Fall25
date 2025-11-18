
month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


month = int(input("Enter the month number (1-12): "))


if month in month_days:
    print("Number of days:", month_days[month])
else:
    print("Invalid month number.")
