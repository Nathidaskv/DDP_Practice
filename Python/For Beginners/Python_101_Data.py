"""
1. TYPES
    1.1) int (integer) 
            >> 0,1,2,3,...,-1,-2,-3,... 
            >> + - * / ได้หมด
    1.2) float ทศนิยม (floating point) 
            >> 1.23, 0.5, 1.8, -69.6969
            >> + - * / ได้หมด
    1.3) str (string) 
            >> 'Hello', "World", "Good morning"
            >> + *
            >> len("Great") >> result : 5
            >> len("Great ") >> result : 6
    1.4) bool (Boolean) 
            >> True/False


2. STORAGE
    2.1) Store in VARIABLES ** ไม่ใช่สมการ แต่มันคือการยัดค่าตัวแปร
            >> x = 2
            >> y = 3
            >> Z = x + y #print(z) >> 5
                >> x = "Great"
                >> y = "likes Jennie"
                >> Z = x + y #print(z) >> Greatlikes Jennie
            >> x = 2
            >> x = x + 1 #print(x) >> 3
    2.2) Store in [LIST] **เอา Data มาเรียงกันเป็นแถว
            >> a = [1,2,3,4,5] **ใส่ [] เพื่อแสดงว่าเป็น list #len(a) >> 5
            >> b = ["I", "Love", "You"] #len(b) >> 3
            >> c = a + b #print(c) >> [1, 2, 3, 4, 5, 'I', 'Love', 'You'] #len(c) >> 8
            >> *ขอดู* ลิสด้วยการระบุ position print(b[1]) >> Love
            >> *ขอ Copy* x = b[1] #print(x) >> Love #คือ List in b ก็ยังคงอยู่
            >> *เปลี่ยนค่าในลิส* b[2] = "Jennie" #print(b) >> b = ["I", "Love", "Jennie"]
    2.3) Store in {DICTIONARY}
            >> age = {"Jon" : 32, "Joe" : 25, "Jen" : 40} #key:value
            >> print(age["Jon"]) >> 32
            >> *Add/Update*ข้อมูล 
                Add : age['Jean'] = 17 #print(age) >> {'Jon': 32, 'Joe': 25, 'Jen': 40, 'Jean': 17}
                Update : age['Jon'] = 33 #print(age) >> {'Jon': 33, 'Joe': 25, 'Jen': 40, 'Jean': 17}
            >> Value can be anything *can also be another dict as well
                people = {"Cherprang" : {"age" : 24, "hints" : ["Idol", "BNK48"]}, "Great" : {"age" : 30, "hints" : ["Teacher", "Male"]}}


"""

"""
#Practice : LIST

a = [1,2,3,4,5] #**ใส่ [] เพื่อแสดงว่าเป็น list
b = ["I", "Love", "You"]
c = a + b 
print(c) #>> [1,2,3,4,5,"I", "Love", "You"]
x = b[1]
print(x)
b[2] = "Jennie"
print(b)
"""


"""
#Practice : DICTIONARY

age = {"Jon" : 32, "Joe" : 25, "Jen" : 40}
print(age["Jon"])
age['Jean'] = 17 #Adding data
print(age)
age['Jon'] = 33 #Updating data
print(age)
"""
