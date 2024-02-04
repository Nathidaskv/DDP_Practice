# US to UK

#import sys so can use sys.exit() to exit code
import sys

print("Currency convertor.")

try:
    USD = float(input("$"))
except: #only runs when try fails
    print("You can only enter numbers.")
    sys.exit()
    
print("Enter $", USD, ".")
print(USD, "is equal to", round(USD/1.24,2), "pounds")
