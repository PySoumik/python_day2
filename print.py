#Join list
num1 = [1,2,3,]
num2 = [4,5,6]
num3 = num1 + num2
#print(num3)
#Another way
num1.extend(num2)
print(num1)
#reverse
num = [1,2,3,4,5,6,7,8,9]
num.sort(reverse=True)
print(num)
#sort
number = [5,3,1,2,7,9,]
number.sort()
print(number)
#loop
looplist = ["Samajit","nobo","debdip"]
for s in looplist :
    print(s)
bestfriend = ["Arko","dIPON","NOBO"]
bestfriend.append("Abir")
print(bestfriend)  
# 07/01/2026
# soumik = ["Name","Section","Class"] 
# soumik[3] ="Roll"
# print(soumik)

# pythoncastimg
num = "12567839"
print(int(num))
print(type(int(num)))

num1 = '51'
print(float(num1))
# sawpping
s=41
c=56
s,c = c,s
print(s,c)
numbers = 44.535
print(type(numbers))
num2 = 45j
print(type(num2))

n = True
print(type(n))
