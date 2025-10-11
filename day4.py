#len
letter =  'p'
print(letter)

print(len(letter))

greeting = 'hello, World!'

print(greeting)

print(len(greeting))

# STRING CONCATENATION =

first_name = 'Soumik'
last_name  = 'Ghosh'  
space = '   '
full_name = first_name + space + last_name 
print(full_name) 

#ESCAPE SQUENCES IN STRING

text = "Line\t1\nLine\t2\tSoumik\nHe said \"Python is intesting!\""
print(text)
  
# String Formatting
name = 'Soumik'  
age  = 12
Inforation = f"My name is {name} and i am {age} years old" 
print(Inforation)

#03/10/2025
# UNPACKING Caracters
programing_language = "python"
a,b,c,d,e,f = programing_language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Slcing python strings
programing_language = 'python'
first_three = programing_language[0:5]
print(first_three)
#Another way
last_three =  programing_language[-3:]
print(last_three)
#Reversing a python
greeting = "Hello , World !"
print(greeting[::-2])

# 11/10/2025
#PYTHON METHODS

# Capitalize()
dear = "thirty days of python"
print(dear.capitalize() )
 
 #count()
dear = "thirty days of python"
print(dear.count('h'))
print(dear.count('y' , 7,14))
print(dear.count('th'))

#endwith()
dear = 'thirty days of python'
print(dear.endswith('on'))
print(dear.endswith('tion'))

#expandtabe()

dear =('thirty\tdays\tof\tpython')
#print(dear)
# print(dear.expandtabs())

print(dear.expandtabs(2))
#find
dear =('thirty days of python')
print(dear.find('y'))
#rfind
print(dear.rfind('y'))




