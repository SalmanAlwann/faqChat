# Adder

import pyautogui as pag
import sys
import json
import requests
import keyboard
from time import sleep
import random

print("Adder SnapChat Bot By Salman Alwan")

try:
    namesFile = open("names.txt", "r")
except:
    print("Could not open names.txt - please make sure this file exists")

namesData = namesFile.read()
names = namesData.strip().split("\n")

print("Retrieved names from names.txt\n")


print(":: Click enter when your mouse is over 'Add Friend' Button ::")
if keyboard.read_key() == "enter":
    addFriendbutton = pag.position()
    print("Successfully captured mouse coordinates.\n")
    sleep(1)
print(":: Click enter when your mouse is over 'Close' Button ::")
if keyboard.read_key() == "enter":
    closeButton = pag.position()
    print("Successfully captured mouse coordinates.\n")
    sleep(1)

print(":: Click enter when your mouse is over 'Add Friend Search Bar' ::")
if keyboard.read_key() == "enter":
    searchBar = pag.position()
    print("Successfully captured mouse coordinates.\n")
    sleep(1)

print(":: Click enter when your mouse is over 'Clear Friend Bar' Button ::")
if keyboard.read_key() == "enter":
    clearButton = pag.position()
    print("Successfully captured mouse coordinates.\n")
    sleep(1)

print(":: Click enter when your mouse is over 'First Add' Button ::")
if keyboard.read_key() == "enter":
    firstAddButton = pag.position()
    print("Successfully captured mouse coordinates.\n")
    sleep(4)
else:
    pass

sleep(2)
print(":: Go Back To The Camera Screen. Waiting For you to press 'Enter' :: \n")
if keyboard.read_key() == "enter":
    pass
else:
    print("Press Enter To Continue When You are Ready.\n")

sleep(1)


def adder(name):
    x = 20
    pag.moveTo(addFriendbutton[0], addFriendbutton[1], 0.5)
    sleep(2)

    pag.click()
    sleep(2)

    pag.moveTo(searchBar[0], searchBar[1], 0.5)
    sleep(2)

    pag.click()
    sleep(2)

    pag.typewrite(name, interval=0.50)
    sleep(3)

    pag.moveTo(firstAddButton[0], firstAddButton[1], 0.5)
    sleep(2)
    print(":: PRESS 'ENTER' TO STOP ADDING AND JUMP TO THE NEXT NAME")
    while x != 0:
        pag.click()
        sleep(1.5)
        x -= 1


for name in names:
    print("Doing: {0}".format(name))
    adder(name)
    sleep(1)
