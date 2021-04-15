#   You are tasked by JHB Metro Police to write a program for their new Camera Driver Demerit System. The program
#   should ask the driver to give you their current speed in km/h and the average allowed speed of the road. The
#   program should conform to the following requirements:
#
#   1. If the speed is less than 60, it should print “OK”.
#   2. Otherwise, for every 5km above the speed limit ( e.g 60), it should give the driver one demerit point and
#       print the total number of demerit points. For example, if the speed is 70km/h and the location’s average is
#       60km/h, it should print: “Points: 2”.
#   3. If the driver gets more than 12 demerit points, the function should print “Time to go to jail!”

# GET THE DRIVERS SPEED
driver_speed = int(input("Enter your current speed: "))
# GET THE ALLOWED AVERAGE SPEED
allowed_speed = int(input("Enter the average allowed speed: "))

# HERE WE CHECK IF DRIVERS SPEED IS LESS THAN 60 KM/H
if driver_speed <= 60:
    # IF YES, PRINT OK
    print("Ok")
# OTHERWISE...
else:
    # TO GET THE AMOUNT OF POINTS TO GIVE THE DRIVER, WE HAVE TO GET THE DIFFERENCE BETWEEN THE DRIVERS SPEED AND THE
    # ACTUAL SPEED LIMIT...
    difference = driver_speed - 60
    # ...THEN DIVIDE IT BY 5, TO GET THE PROPER AMOUNT OF POINTS
    demerit_points = difference / 5
    # WE CONVERT THE demerit_points TO AN INTEGER TO GET RID OF THE DECIMAL NUMBERS
    print(int(demerit_points))

    # IF demerit_points ARE MORE THAN 12, THEN ITS TIME TO GO TO JAIL
    if int(demerit_points) >= 12:
        print("Time to go to jail!")
