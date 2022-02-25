"""
Author: Noa Kirschbaum
Assignment / Part: HW3 - Q4
Date due: 2022-02-24
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import math;

a = float(input("a = "));
b = float(input("b = "));
c = float(input("c = "));

#positive = 2 solutions, zero = 1 solution, negative = no real solution
discriminant = (b**2.0) - (4.0*a*c);

if(a == 0.0 and b == 0.0 and c == 0.0):
    print("This equation has an infinite number of solutions.")
elif(discriminant > 0.0):

    solution_one = (-(b) + math.sqrt(discriminant))/(2.0*a);
    solution_two = (-(b) - math.sqrt(discriminant))/(2.0*a);
    print("This equation has two solutions: x =",solution_one,"and x =",solution_two);

elif(discriminant == 0.0):

    solution_one = (-(b) + math.sqrt(discriminant)) / (2.0 * a);
    print("This equation has one solution: x =",solution_one);

else:
    print("No Real Solutions");
