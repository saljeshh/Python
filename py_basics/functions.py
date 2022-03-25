def greetings_function(name):
    print('Welcome', name)

greetings_function(name = 'Saljesh')  

# Suppose you dont know the number of arguments we use *

def greet(*names):
    print("Welcome", names[2])

greet('saljesh','Annika','Anuska','Success')

# Lets make it dynamic 
def dynamic(name,age):
    print('Hello '+ name + ' you are now ', age)

name = input('Enter your name: ')
age = input('Enter your age: ')

dynamic(name, age)


# RETURN KEYWORD
def my(num1, num2):
    return num1 + num2
    print('hello')# This doesnt get executed because return keyword breaks the sequeence of the function 

print(my(2,3))