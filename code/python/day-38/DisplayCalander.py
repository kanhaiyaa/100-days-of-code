try:
    import calendar

    yy = int(input("Enter year in yyyy format: "))
    mm = int(input("Enter month in mm format: "))

    print(calendar.month(yy,mm))

    if calendar.isleap(yy):
        print(yy,"is leap year.")
        # if it is leap year then whole year calendar will be printed.
        print(calendar.prcal(yy))
except:
    print("Please Enter year in the form of yyyy and month in the form of mm(integer value only).")
