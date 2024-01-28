"""
1. FOR LOOP : ทำซ้ำด้วยจำนวนรอบที่แน่นอน
    >> ex. a = [0,1,2,3] ต้องการ print แต่ละตัวในลิส : a = [0,1,2,3]    for i in a:    print(i)
2. WHILE LOOP : ทำซ้ำตราบใดที่เงื่อนไขยังจริงอยู่
    >> ex. down there
"""

#Practice : FOR LOOP
a = [0,1,2,3,"Great"]
for i in a:
    print(i)

for i in range(3): #just for the first 3 positions
    print(i)

for name in ["A","B","C"]:
    print("I am " + name + ".")


#Practice : WHILE LOOP
x=4
while x>0:
    print(x)
    x=x-1 #Without this line the loop will process infinitely

while True:
    name = input("Hi! Who are you?: ")
    if name == "exit":
        print("Window is closing...")
        break #ออกจาก WHILE LOOP
    else:
        print("Nice to meet you, " + name + " :)")
