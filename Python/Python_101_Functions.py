"""
1.Function : กระบวนการที่เปลี่ยน input -> output ที่ต้องการ
    >> Step 1. def : Define function + inputs + return(outputs)
    >> Step 2. call function
2.Methods
    >> คือ functions ที่ py สร้างไว้ให้สำหรับ object หลักๆอยู่แล้ว เช่น str, list, dict
    >> เรียกใช้ได้เลย
    >> ex. a="Great"    
        a.lower() >> great
        a.upper() >> GREAT
        a.find("E") >> 2
    >> ex. b="P'Great is happy"
        b.split() >> ["P'Great", "is", "happy"] #แบ่งคำกลายเป็น list
    >> ex. c="    Teacher Great    "
        c.strip() >> Teacher Great (with no l/r space)
    >> ex. names = ["Great", "Cher", "Jennie"]
        "".join(names) >> "GreatCherJennie"

"""

"""
#Practice : Functions
def greet_pgreat():
    print("Hello P'Grreat")
greet_pgreat()

def greet(name):
    print("Hello", name)
greet("Jennie")

def square(x):
    return x**2
a=square(4)
print(a)

def devided(x,y):
    if y==0:
        print("Error")
        return "Retry..."
    return x/y
print(devided(2,3))
print(devided(2,0))
"""

b="P'Great is happy"
print(b.split()) #=["P'Great", "is", "happy"]

c="    Teacher Great    "
space = c.strip()           #เอา space ออก
left_space = c.lstrip()     #เอา left space ออก
right_space = c.rstrip()    #เอา right space ออก
print(c)
print(space)
print(left_space)
print(right_space)

names = ["Great", "Cher", "Jennie"]
print("".join(names))   #>> GreatCherJennie
print("-".join(names))  #>> Great-Cher-Jennie
print("❤".join(names)) #>> Great❤Cher❤Jennie