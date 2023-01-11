def main() :
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    format1 = str(month)+"/"+str(day)+"/"+str(year)

    months = ["January", "February", "March", "April", 
            "May", "June", "July", "August", 
            "September", "October", "November", "December"]
    monthStr = months[month-1]
    format2 = monthStr+" " + str(day) + ", " + str(year)

    print("The date is {0} or {1}.".format(format1, format2))

main()
