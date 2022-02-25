"""
Author: Noa Kirschbaum
Assignment / Part: HW3 - Q5
Date due: 2022-02-24
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import math;

side_a = round(float(input("Length of side a: ")), 5);
side_b = round(float(input("Length of side b: ")), 5);
side_c = round(float(input("Length of side c: ")), 5);

if(side_a == side_b == side_c):
    print(str(side_a)+", "+str(side_b)+", "+str(side_c),"form an equilateral triangle");
elif(side_a == side_b or side_a == side_c or side_b == side_c):
    if(side_a == side_b):
        if(side_c == (side_a * math.sqrt(2.0))):
            print("Right isosceles");
        else:
            print("Isosceles (Not right triangle)");
    elif(side_a == side_c):
        if(side_b == (side_a * math.sqrt(2.0))):
            print("Right isosceles");
        else:
            print("Isosceles (Not right triangle)");
    else:
        if (side_a == (side_b * math.sqrt(2.0))):
            print("Right isosceles");
        else:
            print("Isosceles (Not right triangle)");

else:
    print("Scalene");