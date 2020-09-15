import os
import time
import sys
from time import sleep
import random

# AREA (comments for area unit type)
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
choose_from_area = """\nConvert from:
\n1.) square kilometers
2.) square meters
3.) square miles
4.) square feet
5.) square inches
6.) Back
"""
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►

# LENGTH (comments for length unit type)
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
choose_from_length = """\nConvert from:
\n1.) kilometers
2.) meters
3.) centimeters
4.) decimeters
5.) miles
6.) feet
7.) inches
8.) Back
"""
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►

# MASS (comments for mass unit type)
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
choose_from_mass = """\nConvert from:
\n1.) tonnes
2.) kilograms
3.) grams
4.) milligrams
5.) pounds
6.) Back
"""
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►

# PRESSURE (comments for pressure unit type)
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
choose_from_pressure = """\nConvert from:
\n1.) bars
2.) atmospheres
3.) pascals
4.) torr
5.) psi
6.) Back
"""
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►

# SPEED (comments for speed unit type)
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
choose_from_speed = """\nConvert from:
\n1.) km_per_hour
2.) feet_per_hour
3.) inches_per_minute
4.) miles_per_hour
5.) knots
6.) Back
"""
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►

# TEMPERATURE (comments for temperature unit type)
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
choose_from_temperature = """\nConvert from:
\n1.) Celsius
2.) Fahrenheit
3.) Kelvin
4.) Back
"""
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►

# TIME (comments for time unit type)
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
choose_from_time = """\nConvert from:
\n1.) seconds
2.) minutes
3.) hours
4.) days
5.) weeks
6.) months
7.) years
8.) Back
"""
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►

# VOLUME (comments for volume unit type)
# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
choose_from_volume = """\nConvert from:
\n1.) liters
2.) cubic meters
3.) gallons
4.) Back
"""

# defining main function

def main():
    os.system("cls")
    navigation = """\n       ►◄ UNIT CONVERTER ►◄
\n Please choose a Unit Type:
1.) Area
2.) Length
3.) Mass
4.) Pressure
5.) Speed
6.) Temperature
7.) Time
8.) Volume
9.) Credits
10.) Exit
"""

    credits = """
-----------------------------------------------
|Developer: Orkhan Nasirli                    |
|                                             |
|Contact info:                                |
|    e-mail: nasirli93@hotmail.com            |
|            93nasirli93@gmail.com            |
|                                             |
|    github: https://github.com/Twinko2020    |
|                                             |
|Idea: Orkhan Nasirli, Chingiz Nasirli        |
-----------------------------------------------
                                    Copyright © Twinko 2020
"""
    for char in navigation:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.003)
    choice = input("\n► ")

    # logic for user input
    if choice == "1":
        area_option()
    elif choice == "2":
        length_option()
    elif choice == "3":
        mass_option()
    elif choice == "4":
        pressure_option()
    elif choice == "5":
        speed_option()
    elif choice == "6":
        temperature_option()
    elif choice == "7":
        time_option()
    elif choice == "8":
        volume_option()
    elif choice == "9":
        os.system("cls")
        for char in credits:
            sys.stdout.write(char)
            sys.stdout.flush()
            if char != "\n":
                sleep(0.003)
            else:
                sleep(0.00)
        option = input("Press ENTER to go to main menu")
        main()
    elif choice == "10":
        sys.exit()
    else:
        main()

# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
# defining area_option function. Main function for area unit type

def area_option():
    global value_from
    os.system("cls")
    for char in choose_from_area:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.01)
    option_from = input("\n► ")
    # logic for user input
    if option_from == "1":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        area_sqkm()

    elif option_from == "2":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        area_sqm()

    elif option_from == "3":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        area_sqmile()

    elif option_from == "4":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        area_sqfoot()

    elif option_from == "5":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        area_sqinch()

    elif option_from == "6":
        main()

    else:
        area_option()

# creating class so it will store several functions that can be called later. These functions contains code for converter calculation
class area_units():

    def sqkm(self):
        os.system("cls")
        print(f"\nValue: {value_from} square kilometers\n")

        result1 = int(value_from * 1e+6)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\n◄► square kilometers --> square meters ◄►\n")
        print(f"\nResult: {result1} square meters\n")

        result2 = value_from / 2.59
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\n◄► square kilometers --> square miles ◄►\n")
        print(f"\nResult: {result2} square miles\n")

        result3 = int(value_from * 1.076e+7)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\n◄► square kilometers --> square feet ◄►\n")
        print(f"\nResult: {result3} square feet\n")

        result4 = int(value_from * 1.55e+9)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\n◄► square kilometers --> square inches ◄►\n")
        print(f"\nResult: {result4} square inches\n")

        return_back = input("Press ENTER to return to main menu: ")
        area_option()



    def sqm(self):
        os.system("cls")
        print(f"\nValue: {value_from} square meters\n")

        result1 = value_from / 1e+6
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square meters --> square kilometers\n")
        print(f"\nResult: {result1} square kilometers\n")

        result2 = value_from / 2.59e+6
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square meters --> square miles\n")
        print(f"\nResult: {result2} square miles\n")

        result3 = int(value_from * 10.764)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square meters --> square feet\n")
        print(f"\nResult: {result3} square feet\n")

        result4 = int(value_from * 1550)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square meters --> square inches\n")
        print(f"\nResult: {result4} square inches\n")

        return_back = input("Press ENTER to return to main menu: ")
        area_option()

    def sqmile(self):
        os.system("cls")
        print(f"\nValue: {value_from} square miles\n")

        result1 = int(value_from * 2.59)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square miles --> square kilometers\n")
        print(f"\nResult: {result1} square kilometers\n")

        result2 = int(value_from * 2.59e+6)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square miles --> square meters\n")
        print(f"\nResult: {result2} square meters\n")

        result3 = int(value_from * 2.788e+7)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square miles --> square feet\n")
        print(f"\nResult: {result3} square feet\n")

        result4 = int(value_from * 4.014e+9)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square miles --> square inches\n")
        print(f"\nResult: {result4} square inches\n")

        return_back = input("Press ENTER to return to main menu: ")
        area_option()

    def sqfoot(self):
        os.system("cls")
        print(f"\nValue: {value_from} square feet\n")

        result1 = value_from / 1.076e+7
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square feet --> square kilometers\n")
        print(f"\nResult: {result1} square kilometers\n")

        result2 = value_from / 10.764
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square feet --> square meters\n")
        print(f"\nResult: {result2} square meters\n")

        result3 = value_from / 2.788e+7
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square feet --> square miles\n")
        print(f"\nResult: {result3} square miles\n")

        result4 = int(value_from * 144)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square feet --> square inches\n")
        print(f"\nResult: {result4} square inches\n")

        return_back = input("Press ENTER to return to main menu: ")
        area_option()

    def sqinch(self):
        os.system("cls")
        print(f"\nValue: {value_from} square inches\n")

        result = value_from / 1.55e+9
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square inches --> square kilometers\n")
        print(f"\nResult: {result} square kilometers\n")

        result = value_from / 1550
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square inches --> square meters\n")
        print(f"\nResult: {result} square meters\n")

        result = value_from / 4.014e+9
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square inches --> square miles\n")
        print(f"\nResult: {result} square miles\n")

        result = value_from / 144
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: square inches --> square feet\n")
        print(f"\nResult: {result} square feet\n")

        return_back = input("Press ENTER to return to main menu: ")
        area_option()

# defining several functions according to the unit choosen (square kilometer, square meter and etc.). These functions calling class "area_units" and then a required function from it
def area_sqkm():
    os.system("cls")
    sqkm1 = area_units()
    sqkm1.sqkm()

def area_sqm():
    os.system("cls")
    sqm1 = area_units()
    sqm1.sqm()

def area_sqmile():
    os.system("cls")
    sqmile1 = area_units()
    sqmile1.sqmile()

def area_sqfoot():
    os.system("cls")
    sqfoot1 = area_units()
    sqfoot1.sqfoot()

def area_sqinch():
    os.system("cls")
    sqinch1 = area_units()
    sqinch1.sqinch()



# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
# defining length_option function. Main function for length unit type

def length_option():
    global value_from
    os.system("cls")
    for char in choose_from_length:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.01)
    option_from = input("\n► ")
    # logic for user input
    if option_from == "1":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        length_km()

    elif option_from == "2":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        length_meter()

    elif option_from == "3":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        length_cm()

    elif option_from == "4":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        length_dm()

    elif option_from == "5":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        length_mile()

    elif option_from == "6":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        length_foot()

    elif option_from == "7":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        length_inch()

    elif option_from == "8":
        main()

    else:
        length_option()

# creating class so it will store several functions that can be called later. These functions contains code for converter calculation
class length_units():

    def km(self):
        os.system("cls")
        print(f"\nValue: {value_from} kilometers\n")

        result1 = int(value_from * 1e+3)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: kilometers --> meters\n")
        print(f"\nResult: {result1} meters\n")

        result2 = int(value_from * 1e+5)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: kilometers --> centimeters\n")
        print(f"\nResult: {result2} centimeters\n")

        result3 = int(value_from * 1e+4)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: kilometers --> decimeters\n")
        print(f"\nResult: {result3} decimeters\n")

        result4 = value_from / 1.8520
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: kilometers --> miles\n")
        print(f"\nResult: {result4} miles\n")

        result5 = int(value_from * 3280.84)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: kilometers --> feet\n")
        print(f"\nResult: {result5} feet\n")

        result6 = int(value_from * 39370.08)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: kilometers --> inches\n")
        print(f"\nResult: {result6} inches\n")

        return_back = input("Press ENTER to return to main menu: ")
        length_option()



    def meter(self):
        os.system("cls")
        print(f"\nValue: {value_from} meters\n")

        result1 = value_from / 1e+3
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: meters --> kilometers\n")
        print(f"\nResult: {result1} kilometers\n")

        result2 = int(value_from * 100)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: meters --> centimeters\n")
        print(f"\nResult: {result2} centimeters\n")

        result3 = int(value_from * 10)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: meters --> decimeters\n")
        print(f"\nResult: {result3} decimeters\n")

        result4 = value_from / 1851.85
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: meters --> miles\n")
        print(f"\nResult: {result4} miles\n")

        result5 = int(value_from * 3.28)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: meters --> feet\n")
        print(f"\nResult: {result5} feet\n")

        result6 = int(value_from * 39.37)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: meters --> inches\n")
        print(f"\nResult: {result6} inches\n")

        return_back = input("Press ENTER to return to main menu: ")
        length_option()

    def cm(self):
        os.system("cls")
        print(f"\nValue: {value_from} centimeters\n")

        result1 = value_from / 1e+5
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: centimeters --> kilometers\n")
        print(f"\nResult: {result1} kilometers\n")

        result2 = value_from / 100
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: centimeters --> meters\n")
        print(f"\nResult: {result2} meters\n")

        result3 = value_from / 10
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: centimeters --> decimeters\n")
        print(f"\nResult: {result3} decimeters\n")

        result4 = value_from / 200e+3
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: centimeters --> miles\n")
        print(f"\nResult: {result4} miles\n")

        result5 = value_from / 30.48
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: centimeters --> feet\n")
        print(f"\nResult: {result5} feet\n")

        result6 = value_from / 2.54
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: centimeters --> inches\n")
        print(f"\nResult: {result6} inches\n")

        return_back = input("Press ENTER to return to main menu: ")
        length_option()

    def dm(self):
        os.system("cls")
        print(f"\nValue: {value_from} decimeters\n")

        result1 = value_from / 1e+4
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: decimeters --> kilometers\n")
        print(f"\nResult: {result1} kilometers\n")

        result2 = value_from / 10
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: decimeters --> meters\n")
        print(f"\nResult: {result2} meters\n")

        result3 = int(value_from * 10)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: decimeters --> centimeters\n")
        print(f"\nResult: {result3} centimeters\n")

        result4 = value_from / 18518.52
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: decimeters --> miles\n")
        print(f"\nResult: {result4} miles\n")

        result5 = value_from / 3.048
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: decimeters --> feet\n")
        print(f"\nResult: {result5} feet\n")

        result6 = int(value_from * 3.937)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: decimeters --> inches\n")
        print(f"\nResult: {result6} inches\n")

        return_back = input("Press ENTER to return to main menu: ")
        length_option()

    def mile(self):
        os.system("cls")
        print(f"\nValue: {value_from} miles\n")

        result1 = int(value_from * 1.8520)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: miles --> kilometers\n")
        print(f"\nResult: {result1} kilometers\n")

        result2 = int(value_from * 1852)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: miles --> meters\n")
        print(f"\nResult: {result2} meters\n")

        result3 = int(value_from * 185200)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: miles --> centimeters\n")
        print(f"\nResult: {result3} centimeters\n")

        result4 = int(value_from * 18520)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: miles --> decimeters\n")
        print(f"\nResult: {result4} decimeters\n")

        result5 = int(value_from * 6080)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: miles --> feet\n")
        print(f"\nResult: {result5} feet\n")

        result6 = int(value_from * 72960)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: miles --> inches\n")
        print(f"\nResult: {result6} inches\n")

        return_back = input("Press ENTER to return to main menu: ")
        length_option()

    def foot(self):
        os.system("cls")
        print(f"\nValue: {value_from} feet\n")

        result1 = value_from / 3278.70
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: feet --> kilometers\n")
        print(f"\nResult: {result1} kilometers\n")

        result2 = value_from / 3.28
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: feet --> meters\n")
        print(f"\nResult: {result2} meters\n")

        result3 = int(value_from * 30.48)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: feet --> centimeters\n")
        print(f"\nResult: {result3} centimeters\n")

        result4 = int(value_from * 3.048)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: feet --> decimeters\n")
        print(f"\nResult: {result4} decimeters\n")

        result5 = value_from / 6060.60
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: feet --> miles\n")
        print(f"\nResult: {result5} miles\n")

        result6 = int(value_from * 12)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: feet --> inches\n")
        print(f"\nResult: {result6} inches\n")

        return_back = input("Press ENTER to return to main menu: ")
        length_option()

    def inch(self):
        os.system("cls")
        print(f"\nValue: {value_from} inches\n")

        result1 = value_from / 40000
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: inches --> kilometers\n")
        print(f"\nResult: {result1} kilometers\n")

        result2 = value_from / 39.37
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: inches --> meters\n")
        print(f"\nResult: {result2} meters\n")

        result3 = int(value_from * 2.54)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: inches --> centimeters\n")
        print(f"\nResult: {result3} centimeters\n")

        result4 = value_from / 3.97
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: inches --> decimeters\n")
        print(f"\nResult: {result4} decimeters\n")

        result5 = value_from / 71428.57
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: inches --> miles\n")
        print(f"\nResult: {result5} miles\n")

        result6 = value_from / 12
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: inches --> feet\n")
        print(f"\nResult: {result6} feet\n")

        return_back = input("Press ENTER to return to main menu: ")
        length_option()

# defining several functions according to the unit choosen (square kilometer, square meter and etc.). These functions calling class "length_units" and then a required function from it
def length_km():
    os.system("cls")
    km1 = length_units()
    km1.km()

def length_meter():
    os.system("cls")
    meter1 = length_units()
    meter1.meter()

def length_cm():
    os.system("cls")
    cm1 = length_units()
    cm1.cm()

def length_dm():
    os.system("cls")
    dm1 = length_units()
    dm1.dm()

def length_mile():
    os.system("cls")
    mile1 = length_units()
    mile1.mile()

def length_foot():
    os.system("cls")
    foot1 = length_units()
    foot1.foot()

def length_inch():
    os.system("cls")
    inch1 = length_units()
    inch1.inch()



# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
# defining mass_option function. Main function for mass unit type

def mass_option():
    os.system("cls")
    global value_from
    for char in choose_from_mass:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.01)
    option_from = input("\n► ")
    # logic for user input
    if option_from == "1":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        mass_tonne()

    elif option_from == "2":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        mass_kilogram()

    elif option_from == "3":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        mass_gram()

    elif option_from == "4":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        mass_milligram()

    elif option_from == "5":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        mass_pound()

    elif option_from == "6":
        main()

    else:
        mass_option()

# creating class so it will store several functions that can be called later. These functions contains code for converter calculation
class mass_units():

    def tonne(self):
        os.system("cls")
        print(f"\nValue: {value_from} tonnes\n")

        result1 = int(value_from * 1e+3)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: tonnes --> kilograms\n")
        print(f"\nResult: {result1} kilograms\n")

        result2 = int(value_from * 1e+6)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: tonnes --> grams\n")
        print(f"\nResult: {result2} grams\n")

        result3 = int(value_from * 1e+9)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: tonnes --> milligrams\n")
        print(f"\nResult: {result3} milligrams\n")

        result4 = int(value_from * 2204.62)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: tonnes --> pounds\n")
        print(f"\nResult: {result4} pounds\n")

        return_back = input("Press ENTER to return to main menu: ")
        mass_option()



    def kilogram(self):
        os.system("cls")
        print(f"\nValue: {value_from} kilograms\n")

        result1 = value_from / 1e+3
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: kilograms --> tonnes\n")
        print(f"\nResult: {result1} tonnes\n")

        result2 = int(value_from * 1e+3)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: kilograms --> grams\n")
        print(f"\nResult: {result2} grams\n")

        result3 = int(value_from * 1e+6)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: kilograms --> milligrams\n")
        print(f"\nResult: {result3} milligrams\n")

        result4 = int(value_from * 2.204)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: kilograms --> pounds\n")
        print(f"\nResult: {result4} pounds\n")

        return_back = input("Press ENTER to return to main menu: ")
        mass_option()

    def gram(self):
        os.system("cls")
        print(f"\nValue: {value_from} grams\n")

        result1 = value_from / 1e+6
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: grams --> tonnes\n")
        print(f"\nResult: {result1} tonnes\n")

        result2 = value_from / 1e+3
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: grams --> kilograms\n")
        print(f"\nResult: {result2} kilograms\n")

        result3 = int(value_from * 1e+3)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: grams --> milligrams\n")
        print(f"\nResult: {result3} milligrams\n")

        result4 = value_from / 453.51
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: grams --> pounds\n")
        print(f"\nResult: {result4} pounds\n")

        return_back = input("Press ENTER to return to main menu: ")
        mass_option()

    def milligram(self):
        os.system("cls")
        print(f"\nValue: {value_from} milligrams\n")

        result1 = value_from / 1e+9
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: milligrams --> tonnes\n")
        print(f"\nResult: {result1} tonnes\n")

        result2 = value_from / 1e+6
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: milligrams --> kilograms\n")
        print(f"\nResult: {result2} kilograms\n")

        result3 = value_from / 1e+3
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: milligrams --> grams\n")
        print(f"\nResult: {result3} grams\n")

        result4 = value_from / 500
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: milligrams --> pounds\n")
        print(f"\nResult: {result4} pounds\n")

        return_back = input("Press ENTER to return to main menu: ")
        mass_option()

    def pound(self):
        os.system("cls")
        print(f"\nValue: {value_from} pounds\n")

        result1 = value_from / 2202.64
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: pounds --> tonnes\n")
        print(f"\nResult: {result1} tonnes\n")

        result2 = value_from / 2.205
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: pounds --> kilograms\n")
        print(f"\nResult: {result2} kilograms\n")

        result3 = int(value_from * 453.6)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: pounds --> grams\n")
        print(f"\nResult: {result3} grams\n")

        result4 = int(value_from * 453592)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: pounds --> milligrams\n")
        print(f"\nResult: {result4} milligrams\n")

        return_back = input("Press ENTER to return to main menu: ")
        mass_option()

# defining several functions according to the unit choosen (square kilometer, square meter and etc.). These functions calling class "mass_units" and then a required function from it
def mass_tonne():
    os.system("cls")
    tonne1 = mass_units()
    tonne1.tonne()

def mass_kilogram():
    os.system("cls")
    kilogram1 = mass_units()
    kilogram1.kilogram()

def mass_gram():
    os.system("cls")
    gram1 = mass_units()
    gram1.gram()

def mass_milligram():
    os.system("cls")
    milligram1 = mass_units()
    milligram1.milligram()

def mass_pound():
    os.system("cls")
    pound1 = mass_units()
    pound1.pound()

# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
# defining presure_option function. Main function for pressure unit type

def pressure_option():
    os.system("cls")
    global value_from
    for char in choose_from_pressure:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.01)
    option_from = input("\n► ")
    # logic for user input
    if option_from == "1":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        pressure_bar()

    elif option_from == "2":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        pressure_atmosphere()

    elif option_from == "3":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        pressure_pascal()

    elif option_from == "4":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        pressure_torr()

    elif option_from == "5":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        pressure_psi()

    elif option_from == "6":
        main()

    else:
        pressure_option()

# creating class so it will store several functions that can be called later. These functions contains code for converter calculation
class pressure_units():

    def bar(self):
        os.system("cls")
        print(f"\nValue: {value_from} bars\n")

        result1 = value_from / 1.01326
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: bars --> atmospheres\n")
        print(f"\nResult: {result1} atmospheres\n")

        result2 = int(value_from * 1e+5)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: bars --> pascals\n")
        print(f"\nResult: {result2} pascals\n")

        result3 = int(value_from * 750.063)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: bars --> torr\n")
        print(f"\nResult: {result3} torr\n")

        result4 = int(value_from * 14.50)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: bars --> psi\n")
        print(f"\nResult: {result4} psi\n")

        return_back = input("Press ENTER to return to main menu: ")
        pressure_option()



    def atmosphere(self):
        os.system("cls")
        print(f"\nValue: {value_from} atmospheres\n")


        result1 = int(value_from * 1.01325)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: atmospheres --> bars\n")
        print(f"\nResult: {result1} bars\n")

        result2 = int(value_from * 101325)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: atmospheres --> pascals\n")
        print(f"\nResult: {result2} pascals\n")

        result3 = int(value_from * 760.002)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: atmospheres --> torr\n")
        print(f"\nResult: {result3} torr\n")

        result4 = int(value_from * 14.7)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: atmospheres --> psi\n")
        print(f"\nResult: {result4} psi\n")

        return_back = input("Press ENTER to return to main menu: ")
        pressure_option()

    def pascal(self):
        os.system("cls")
        print(f"\nValue: {value_from} pascals\n")

        result1 = value_from / 1e+5
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: pascals --> bars\n")
        print(f"\nResult: {result1} bars\n")

        result2 = value_from / 1e+5
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: pascals --> atmospheres\n")
        print(f"\nResult: {result2} atmospheres\n")

        result3 = value_from / 133.32
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: pascals --> torr\n")
        print(f"\nResult: {result3} torr\n")

        result4 = value_from / 6896.51
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: pascals --> psi\n")
        print(f"\nResult: {result4} psi\n")

        return_back = input("Press ENTER to return to main menu: ")
        pressure_option()

    def torr(self):
        os.system("cls")
        print(f"\nValue: {value_from} torr\n")

        result1 = value_from / 750.2
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: torr --> bars\n")
        print(f"\nResult: {result1} bars\n")

        result2 = value_from / 750.2
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: torr --> atmospheres\n")
        print(f"\nResult: {result2} atmospheres\n")

        result3 = int(value_from * 133.32)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: torr --> pascals\n")
        print(f"\nResult: {result3} pascals\n")

        result4 = value_from / 51.72
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: torr --> psi\n")
        print(f"\nResult: {result4} psi\n")

        return_back = input("Press ENTER to return to main menu: ")
        pressure_option()

    def psi(self):
        os.system("cls")
        print(f"\nValue: {value_from} psi\n")

        result1 = value_from / 14.5
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: psi --> bars\n")
        print(f"\nResult: {result1} bars\n")

        result2 = value_from / 14.7
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: psi --> atmospheres\n")
        print(f"\nResult: {result2} atmospheres\n")

        result3 = int(value_from * 6896.51)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: psi --> pascals\n")
        print(f"\nResult: {result3} pascals\n")

        result4 = int(value_from * 51.72)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: psi --> torr\n")
        print(f"\nResult: {result4} torr\n")

        return_back = input("Press ENTER to return to main menu: ")
        pressure_option()

# defining several functions according to the unit choosen (square kilometer, square meter and etc.). These functions calling class "pressure_units" and then a required function from it
def pressure_bar():
    bar1 = pressure_units()
    bar1.bar()

def pressure_atmosphere():
    atmosphere1 = pressure_units()
    atmosphere1.atmosphere()

def pressure_pascal():
    pascal1 = pressure_units()
    pascal1.pascal()

def pressure_torr():
    torr1 = pressure_units()
    torr1.torr()

def pressure_psi():
    psi1 = pressure_units()
    psi1.psi()

# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
# defining Speed function. Main function for Speed unit type
def speed_option():
    os.system("cls")
    global value_from
    for char in choose_from_speed:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.01)
    option_from = input("\n► ")
    # logic for user input
    if option_from == "1":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        speed_km_per_hour()

    elif option_from == "2":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        speed_feet_per_hour()

    elif option_from == "3":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        speed_inches_per_minute()

    elif option_from == "4":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        speed_miles_per_hour()

    elif option_from == "5":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        speed_knots()

    elif option_from == "6":
        main()

    else:
        speed_option()

# creating class so it will store several functions that can be called later. These functions contains code for converter calculation
class speed_units():

    def km_per_hour(self):
        os.system("cls")
        print(f"\nValue: {value_from} km_per_hour\n")

        result1 = int(value_from * 3280.83)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: km_per_hour --> feet_per_hour\n")
        print(f"\nResult: {result1} feet_per_hour\n")

        result2 = int(value_from * 656.16)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: km_per_hour --> inches_per_minute\n")
        print(f"\nResult: {result2} inches_per_minute\n")

        result3 = value_from / 1.1610
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: km_per_hour --> miles_per_hour\n")
        print(f"\nResult: {result3} miles_per_hour\n")

        result4 = value_from / 1.85
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: km_per_hour --> knots\n")
        print(f"\nResult: {result4} knots\n")

        return_back = input("Press ENTER to return to main menu: ")
        speed_option()



    def foot_per_hour(self):
        os.system("cls")
        print(f"\nValue: {value_from} feet_per_hour\n")


        result1 = value_from / 3278.68
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: feet_per_hour --> km_per_hour\n")
        print(f"\nResult: {result1} km_per_hour\n")

        result2 = value_from / 5
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: feet_per_hour --> inches_per_minute\n")
        print(f"\nResult: {result2} inches_per_minute\n")

        result3 = value_from / 5291
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: feet_per_hour --> miles_per_hour\n")
        print(f"\nResult: {result3} miles_per_hour\n")

        result4 = value_from / 6060
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: feet_per_hour --> knots\n")
        print(f"\nResult: {result4} knots\n")

        return_back = input("Press ENTER to return to main menu: ")
        speed_option()

    def inch_per_minute(self):
        os.system("cls")
        print(f"\nValue: {value_from} inches_per_minute\n")

        result1 = value_from / 656.17
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: inches_per_minute --> km_per_hour\n")
        print(f"\nResult: {result1} km_per_hour\n")

        result2 = int(value_from * 5)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: inches_per_minute --> feet_per_hour\n")
        print(f"\nResult: {result2} feet_per_hour\n")

        result3 = value_from / 1056
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: inches_per_minute --> miles_per_hour\n")
        print(f"\nResult: {result3} miles_per_hour\n")

        result4 = value_from / 1215
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: inches_per_minute --> knots\n")
        print(f"\nResult: {result4} knots\n")

        return_back = input("Press ENTER to return to main menu: ")
        speed_option()

    def mile_per_hour(self):
        os.system("cls")
        print(f"\nValue: {value_from} miles_per_hour\n")

        result1 = int(value_from * 1.610)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: miles_per_hour --> km_per_hour\n")
        print(f"\nResult: {result1} km_per_hour\n")

        result2 = int(value_from * 5280)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: miles_per_hour --> feet_per_hour\n")
        print(f"\nResult: {result2} feet_per_hour\n")

        result3 = int(value_from * 1056)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: miles_per_hour --> inches_per_minute\n")
        print(f"\nResult: {result3} inches_per_minute\n")

        result4 = value_from / 1150
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: miles_per_hour --> knots\n")
        print(f"\nResult: {result4} knots\n")

        return_back = input("Press ENTER to return to main menu: ")
        speed_option()

    def knots(self):
        os.system("cls")
        print(f"\nValue: {value_from} knots\n")

        result1 = int(value_from * 1852)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: knots --> km_per_hour\n")
        print(f"\nResult: {result1} km_per_hour\n")

        result2 = int(value_from * 6076.10)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: knots --> feet_per_hour\n")
        print(f"\nResult: {result2} feet_per_hour\n")

        result3 = int(value_from * 1215.22)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: knots --> inches_per_minute\n")
        print(f"\nResult: {result3} inches_per_minute\n")

        result4 = int(value_from * 1.15)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: knots --> miles_per_hour\n")
        print(f"\nResult: {result4} miles_per_hour\n")

        return_back = input("Press ENTER to return to main menu: ")
        speed_option()

# defining several functions according to the unit choosen (square kilometer, square meter and etc.). These functions calling class "speed_units" and then a required function from it
def speed_km_per_hour():
    km_per_hour1 = speed_units()
    km_per_hour1.km_per_hour()

def speed_feet_per_hour():
    feet_per_hour1 = speed_units()
    feet_per_hour1.foot_per_hour()

def speed_inches_per_minute():
    inches_per_minute1 = speed_units()
    inches_per_minute1.inch_per_minute()

def speed_miles_per_hour():
    miles_per_hour1 = speed_units()
    miles_per_hour1.mile_per_hour()

def speed_knots():
    knots1 = speed_units()
    knots1.knots()

# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
# defining Temperature function. Main function for Temperature unit type
def temperature_option():
    os.system("cls")
    global value_from
    for char in choose_from_temperature:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.01)
    option_from = input("\n► ")
    # logic for user input
    if option_from == "1":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        temperature_celsius()

    elif option_from == "2":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        temperature_fahrenheit()

    elif option_from == "3":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        temperature_kelvin()

    elif option_from == "4":
        main()

    else:
        temperature_option()

# creating class so it will store several functions that can be called later. These functions contains code for converter calculation
class temperature_units():

    def celsius(self):
        os.system("cls")
        print(f"\nValue: {value_from} celsius\n")

        result1 = int(((value_from * 9) / 5) + 32)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: celsius --> fahrenheit\n")
        print(f"\nResult: {result1} fahrenheit\n")

        result2 = int(value_from + 273.15)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: celsius --> kelvin\n")
        print(f"\nResult: {result2} kelvin\n")

        return_back = input("Press ENTER to return to main menu: ")
        temperature_option()



    def fahrenheit(self):
        os.system("cls")
        print(f"\nValue: {value_from} fahrenheit\n")


        result1 = int(((value_from - 32) * 5) / 9)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: fahrenheit --> celsius\n")
        print(f"\nResult: {result1} celsius\n")

        result2 = int((((value_from - 32) * 5) / 9) + 273.15)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: fahrenheit --> kelvin\n")
        print(f"\nResult: {result2} kelvin\n")

        return_back = input("Press ENTER to return to main menu: ")
        temperature_option()

    def kelvin(self):
        os.system("cls")
        print(f"\nValue: {value_from} kelvin\n")

        result1 = value_from - 273.15
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: kelvin --> celsius\n")
        print(f"\nResult: {result1} celsius\n")

        result2 = int((((value_from - 273.15) * 9) / 5) + 32)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: kelvin --> fahrenheit\n")
        print(f"\nResult: {result2} fahrenheit\n")

        return_back = input("Press ENTER to return to main menu: ")
        temperature_option()


# defining several functions according to the unit choosen (square kilometer, square meter and etc.). These functions calling class "temperature_units" and then a required function from it
def temperature_celsius():
    celsius1 = temperature_units()
    celsius1.celsius()

def temperature_fahrenheit():
    fahrenheit1 = temperature_units()
    fahrenheit1.fahrenheit()

def temperature_kelvin():
    kelvin1 = temperature_units()
    kelvin1.kelvin()


# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
# defining Time function. Main function for Time unit type
def time_option():
    global value_from
    os.system("cls")
    for char in choose_from_time:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.01)
    option_from = input("\n► ")
    # logic for user input
    if option_from == "1":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        time_second()

    elif option_from == "2":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        time_minute()

    elif option_from == "3":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        time_hour()

    elif option_from == "4":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        time_day()

    elif option_from == "5":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        time_week()

    elif option_from == "6":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        time_month()

    elif option_from == "7":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        time_year()

    elif option_from == "8":
        main()

    else:
        time_option()

# creating class so it will store several functions that can be called later. These functions contains code for converter calculation
class time_units():

    def second(self):
        os.system("cls")
        print(f"\nValue: {value_from} seconds\n")

        result1 = value_from / 60
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: seconds --> minutes\n")
        print(f"\nResult: {result1} minutes\n")

        result2 = value_from / 3600
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: seconds --> hours\n")
        print(f"\nResult: {result2} hours\n")

        result3 = value_from / 86400
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: seconds --> days\n")
        print(f"\nResult: {result3} days\n")

        result4 = value_from / 604800
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: seconds --> weeks\n")
        print(f"\nResult: {result4} weeks\n")

        result5 = value_from / 10886400
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: seconds --> months\n")
        print(f"\nResult: {result5} months\n")

        result6 = value_from / 378432000
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: seconds --> years\n")
        print(f"\nResult: {result6} years\n")

        return_back = input("Press ENTER to return to main menu: ")
        time_option()



    def minute(self):
        os.system("cls")
        print(f"\nValue: {value_from} minutes\n")

        result1 = int(value_from * 60)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: minutes --> seconds\n")
        print(f"\nResult: {result1} seconds\n")

        result2 = value_from / 60
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: minutes --> hours\n")
        print(f"\nResult: {result2} hours\n")

        result3 = value_from / 1440
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: minutes --> days\n")
        print(f"\nResult: {result3} days\n")

        result4 = value_from / 10080
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: minutes --> weeks\n")
        print(f"\nResult: {result4} weeks\n")

        result5 = value_from / 181440
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: minutes --> months\n")
        print(f"\nResult: {result5} months\n")

        result6 = value_from / 6307200
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: minutes --> years\n")
        print(f"\nResult: {result6} years\n")

        return_back = input("Press ENTER to return to main menu: ")
        time_option()

    def hour(self):
        os.system("cls")
        print(f"\nValue: {value_from} hours\n")

        result1 = int(value_from * 3600)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: hours --> seconds\n")
        print(f"\nResult: {result1} seconds\n")

        result2 = int(value_from * 60)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: hours --> minutes\n")
        print(f"\nResult: {result2} minutes\n")

        result3 = value_from / 24
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: hours --> days\n")
        print(f"\nResult: {result3} days\n")

        result4 = value_from / 168
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: hours --> weeks\n")
        print(f"\nResult: {result4} weeks\n")

        result5 = value_from / 720
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: hours --> months\n")
        print(f"\nResult: {result5} months\n")

        result6 = value_from / 8760
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: hours --> years\n")
        print(f"\nResult: {result6} years\n")

        return_back = input("Press ENTER to return to main menu: ")
        time_option()

    def day(self):
        os.system("cls")
        print(f"\nValue: {value_from} days\n")

        result1 = int(value_from * 86400)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: days --> seconds\n")
        print(f"\nResult: {result1} seconds\n")

        result2 = int(value_from * 1440)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: days --> minutes\n")
        print(f"\nResult: {result2} minutes\n")

        result3 = int(value_from * 24)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: days --> hours\n")
        print(f"\nResult: {result3} hours\n")

        result4 = value_from / 7
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: days --> weeks\n")
        print(f"\nResult: {result4} weeks\n")

        result5 = value_from / 30
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: days --> months\n")
        print(f"\nResult: {result5} months\n")

        result6 = value_from / 365
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: days --> years\n")
        print(f"\nResult: {result6} years\n")

        return_back = input("Press ENTER to return to main menu: ")
        time_option()

    def week(self):
        os.system("cls")
        print(f"\nValue: {value_from} weeks\n")

        result1 = value_from * 604800
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: weeks --> seconds\n")
        print(f"\nResult: {result1} seconds\n")

        result2 = value_from * 10080
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: weeks --> minutes\n")
        print(f"\nResult: {result2} minutes\n")

        result3 = value_from * 168
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: weeks --> hours\n")
        print(f"\nResult: {result3} hours\n")

        result4 = value_from * 7
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: weeks --> days\n")
        print(f"\nResult: {result4} days\n")

        result5 = value_from / 4
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: weeks --> months\n")
        print(f"\nResult: {result5} months\n")

        result6 = value_from / 48
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: weeks --> years\n")
        print(f"\nResult: {result6} years\n")

        return_back = input("Press ENTER to return to main menu: ")
        time_option()

    def month(self):
        os.system("cls")
        print(f"\nValue: {value_from} months\n")

        result1 = int(value_from * 10886400)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: months --> seconds\n")
        print(f"\nResult: {result1} seconds\n")

        result2 = int(value_from * 181440)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: months --> minutes\n")
        print(f"\nResult: {result2} minutes\n")

        result3 = int(value_from * 720)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: months --> hours\n")
        print(f"\nResult: {result3} hours\n")

        result4 = int(value_from * 30)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: months --> days\n")
        print(f"\nResult: {result4} days\n")

        result5 = int(value_from * 4)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: months --> weeks\n")
        print(f"\nResult: {result5} weeks\n")

        result6 = value_from / 12
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: months --> years\n")
        print(f"\nResult: {result6} years\n")

        return_back = input("Press ENTER to return to main menu: ")
        time_option()

    def year(self):
        os.system("cls")
        print(f"\nValue: {value_from} years\n")

        result1 = int(value_from * 378432000)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: years --> seconds\n")
        print(f"\nResult: {result1} seconds\n")

        result2 = int(value_from * 6307200)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: years --> minutes\n")
        print(f"\nResult: {result2} minutes\n")

        result3 = int(value_from * 8760)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: years --> hours\n")
        print(f"\nResult: {result3} hours\n")

        result4 = int(value_from * 365)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: years --> days\n")
        print(f"\nResult: {result4} days\n")

        result5 = int(value_from * 48)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: years --> weeks\n")
        print(f"\nResult: {result5} weeks\n")

        result6 = int(value_from * 12)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: years --> months\n")
        print(f"\nResult: {result6} months\n")

        return_back = input("Press ENTER to return to main menu: ")
        time_option()

# defining several functions according to the unit choosen (square kilometer, square meter and etc.). These functions calling class "time_units" and then a required function from it
def time_second():
    os.system("cls")
    second1 = time_units()
    second1.second()

def time_minute():
    os.system("cls")
    minute1 = time_units()
    minute1.minute()

def time_hour():
    os.system("cls")
    hour1 = time_units()
    hour1.hour()

def time_day():
    os.system("cls")
    day1 = time_units()
    day1.day()

def time_week():
    os.system("cls")
    week1 = time_units()
    week1.week()

def time_month():
    os.system("cls")
    month1 = time_units()
    month1.month()

def time_year():
    os.system("cls")
    year1 = time_units()
    year1.year()

# ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►
# defining Volume function. Main function for Volume unit type
def volume_option():
    os.system("cls")
    global value_from
    for char in choose_from_volume:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.01)
    option_from = input("\n► ")
    # logic for user input
    if option_from == "1":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        volume_liter()

    elif option_from == "2":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        volume_cubic_meter()

    elif option_from == "3":
        while True:
            os.system("cls")
            # try and except command. Used for getting "number" input from user, and if it is not a number it will execute "except"
            try:
                value_from = int(input("\nPlease enter a value to convert: "))
                break
            except ValueError:
                os.system("cls")
                option = input("\nPlease enter a number!!! ")
                continue
        volume_gallon()

    elif option_from == "4":
        main()

    else:
        volume_option()

# creating class so it will store several functions that can be called later. These functions contains code for converter calculation
class volume_units():

    def liter(self):
        os.system("cls")
        print(f"\nValue: {value_from} liters\n")

        result1 = value_from * 1e-3
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: liters --> cubic_meters\n")
        print(f"\nResult: {result1} cubic_meters\n")

        result2 = value_from / 4.5461
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: liters --> gallons\n")
        print(f"\nResult: {result2} gallons\n")

        return_back = input("Press ENTER to return to main menu: ")
        volume_option()



    def cubic_meter(self):
        os.system("cls")
        print(f"\nValue: {value_from} cubic_meters\n")


        result1 = int(value_from * 1000)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: cubic_meters --> liters\n")
        print(f"\nResult: {result1} liters\n")

        result2 = int(value_from * 219.97)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: cubic_meters --> gallons\n")
        print(f"\nResult: {result2} gallons\n")

        return_back = input("Press ENTER to return to main menu: ")
        volume_option()

    def gallon(self):
        os.system("cls")
        print(f"\nValue: {value_from} gallons\n")

        result1 = int(value_from * 4.5461)
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: gallons --> liters\n")
        print(f"\nResult: {result1} liters\n")

        result2 = value_from / 219.97
        print("\n◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄► ◄►\n")
        print("\nRequest: gallons --> cubic_meters\n")
        print(f"\nResult: {result2} cubic_meters\n")

        return_back = input("Press ENTER to return to main menu: ")
        volume_option()


# defining several functions according to the unit choosen (square kilometer, square meter and etc.). These functions calling class "temperature_units" and then a required function from it
def volume_liter():
    liter1 = volume_units()
    liter1.liter()

def volume_cubic_meter():
    cubic_meter1 = volume_units()
    cubic_meter1.cubic_meter()

def volume_gallon():
    gallon1 = volume_units()
    gallon1.gallon()





main()
