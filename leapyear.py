year=int(input("Enter the year:"))
if (((year%4==0) and (year%100!=0)) or (year%400==0)):
    """"
    if a year is multiple of 4 then it is a leap year
    """
    print("{0} is a leap year!!".format(year))
    """"
    printing the output
    """
else:
    print("{0} is not a leap year!!".format(year))
    