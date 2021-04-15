#   You are tasked by JHB Metro Police to write a program for their new Camera Driver Demerit System. The program
#   should ask the driver to give you their current speed in km/h and the average allowed speed of the road. The
#   program should conform to the following requirements:
#
#   1. If the speed is less than 60, it should print “OK”.
#   2. Otherwise, for every 5km above the speed limit ( e.g 60), it should give the driver one demerit point and
#       print the total number of demerit points. For example, if the speed is 70km/h and the location’s average is
#       60km/h, it should print: “Points: 2”.
#   3. If the driver gets more than 12 demerit points, the function should print “Time to go to jail!”