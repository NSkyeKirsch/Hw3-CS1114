"""
Author: Noa Kirschbaum
Assignment / Part: HW3 - Q3
Date due: 2022-02-24
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

cost = 0.0;
#input: day of week, start time, length (MUST BE 24 HOUR TIME)

day = input("Enter the day the call started at: ");
time = int(input("Enter the time the call started at (hhmm): "));
length = int(input("Enter the duration of the call (in minutes): "));

#call between 6am-9pm, Mon-Fri,0.5 per minute
#call before 6am or after 9pm, Mon-Fri, 0.3 per minute
#Sat-Sun, 0.15 per minute

if(day == "Mon" or day == "Tue" or day == "Wed" or day == "Thr" or day == "Fri"):
    if(time < 600 or time > 2100):
        #print("weekday night/morning");
        cost = length * 0.3;
    else:
        #print("weekday midday");
        cost = length * 0.5;
else:
    #print("weekend");
    cost = length * 0.15;
#output: cost of call

print("This call will cost $" + str(cost));