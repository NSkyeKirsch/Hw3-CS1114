"""
Author: Noa Kirschbaum
Assignment / Part: HW3 - Q2
Date due: 2022-02-24
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import random;
Critical_Hit = False;

Level = int(input("What is this Pokemon's Level? "));
Speed =  int(input("What is this Pokemon's Speed? "));

#r is random 0-255 and t is random from 0-255
RandNum = random.randint(0,255);
Threshold = Speed / 2; #threshold value
if(RandNum < Threshold):
    Critical_Hit = True;
if(Critical_Hit == True):
    Multiplier = round((2*Level+5) / (Level+5)); #number that the attack will be multiplied by
else:
    Multiplier = 1;
print("The Pokemon's move will be",str(Multiplier) + "x stronger!");



