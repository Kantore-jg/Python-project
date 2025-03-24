def leap_year():
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("is a leap year.")
            else:
                print("not a leap year.")
        else:
            print("leap year.")
    else:
        print("not a leap year.")
def daysInMonth(year,month):
    months_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year() and month==2:
        return 29
    else:
        return months_days[month-1]
year=int(input("enter a year: "))
month=int(input("enter a month: "))
days=daysInMonth(year,month)
print(days)