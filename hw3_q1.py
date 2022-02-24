"""
Author: Noa Kirschbaum
Assignment / Part: HW3 - Q1
Date due: 2022-02-24
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

xp_points = float(input("Enter this user's current XP: "));
invalid_xp = False;

if(40.0 <= xp_points <= 50.0):
    player_level = 5;
elif(30.0 <= xp_points <= 39.9):
    player_level = 4;
elif(25.0 <= xp_points <= 29.9):
    player_level = 3;
elif(18.5 <= xp_points <= 24.9):
    player_level = 2;
elif(xp_points < 18.5):
    player_level = 1;
else:
    invalid_xp = True;

if(invalid_xp == False):
    print("Level",player_level,"Player (XP:",str(xp_points) + ")");

else:
    print("ERROR: Please enter a valid XP value.");