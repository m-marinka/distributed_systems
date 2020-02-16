import math
from datetime import datetime



str1 = "Hello world!"
print(str1)

name = input("Enter your name: ")
print("Hello,", name)

print("Your name has", len(name), "lettes.")

print(len(name), "! = ", math.factorial(len(name)))

birth = input("Please, enter your birth date in format (DD.MM.YYYY): ")

try:
    birth = datetime.strptime(birth, '%d.%m.%Y')

except:
    print("Incorrect date!")
    exit()




today = datetime.now()

remainder1 = (today - birth).days
remainder2 = int(remainder1 // 365.24)

if (remainder1 < 0):
    print("Incorrect date!")
    exit()

print("Today is: ", today, "you are ", remainder2, "years", "(", remainder1, ") days old.")









