import time
import os
import sys
print("""
········································································
: ___  ___      ________      ___      ___  ________      ___          :
:|\  \|\  \    |\   __  \    |\  \    /  /||\   __  \    |\  \         :
:\ \  \\\  \   \ \  \|\  \   \ \  \  /  / /\ \  \|\  \   \ \  \        :
: \ \   __  \   \ \   __  \   \ \  \/  / /  \ \   __  \   \ \  \       :
:  \ \  \ \  \   \ \  \ \  \   \ \    / /    \ \  \ \  \   \ \  \____  :
:   \ \__\ \__\   \ \__\ \__\   \ \__/ /      \ \__\ \__\   \ \_______\:
: ___\|___\|__| _______|\|__| ________/     ___\|___\|__| ____________|:
:|\  \|\  \    |\  ___ \     |\_____  \    |\  \|\  \    |\   __  \    :
:\ \  \\\  \   \ \   __/|     \|___/  /|   \ \  \\\  \   \ \  \|\  \   :
: \ \   __  \   \ \  \_|/__       /  / /    \ \   __  \   \ \   __  \  :
:  \ \  \ \  \   \ \  \_|\ \     /  /_/__    \ \  \ \  \   \ \  \ \  \ :
:   \ \__\ \__\   \ \_______\   |\________\   \ \__\ \__\   \ \__\ \__\:
:    \|__|\|__|    \|_______|    \|_______|    \|__|\|__|    \|__|\|__|:
········································································
""")
print("welcome to this calculator")

num1 = input("What is Your First Number ?")
print("")
print("list of opariatiors")
print("+ , - , * , / ")
opa = input("What is your oparatior")

num2 = input("What is your Second Number ?")
if opa == "+":
    print("=")
    print(int(num1) + int(num2))
elif opa == "-":
    print("=")
    print(int(num1) - int(num2))
elif opa == "*":
    print("=")
    print(int(num1) * int(num2))
elif opa == "/":
    print("=")
    print(int(num1) / int(num2))

cun = input("continue ? ")
if cun == "yes":
    os.system('clear')
    os.system('python3 calculator.py')
else:
    exit()

