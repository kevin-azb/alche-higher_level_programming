#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

Lst_dgt = number % 10 if number >= 0 else -(abs(number) % 10)

if Lst_dgt > 5:
    print(f"Last digit of {number} is {Lst_dgt} and is greater than 5")

if Lst_dgt == 0:
    print(f"Last digit of {number} is {Lst_dgt} and is 0")

if Lat_dgt < 6 and Last_digit != 0:
    print(f"Last digit of {number} is {Lst_dgt} and is less than 6 and not 0")
