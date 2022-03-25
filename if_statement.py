import string


a = 2 
b = 3

if a < b:
    print(str(a) + ' is greater then ' + str(b))

name = 'annika'
boyfriend = 'saljesh'

if len(name) == len(boyfriend):
    print("You are perfect match")
else:
    print("You are not !")    

aa = True

if a == True:
    print('a is equals to True')

if a != True:
    print('a is not equals to True')


# else if 

a = 2
b = 3

if a == b:
    print('A and B is equal')
elif a > b:
    print('A is greater than B')
else:
    print('B is greater than A')    


a = 'saljesh'
listt = ['a','b']

if type(listt) == list:
    print('It is list')

if type(a) == int:
    print("A is integer")
elif type(a) == float:
    print("A is floating")
elif type(a) == str:
    print("A is string")
else:
    print("none of the above")


# value = int(input('Input a number: '))

# if type(value) == str:
#     print(value, ' is a string')
# else:
#     print(value, ' is not a string')



print(22 % 5)

num = int(input('Input a number'))

if num % 5:
    print(num, ' can be divided by 5')
else:
    print(num,' cant be divided by 5')


# length
value = int(input('Input a number: '))

if value < 10: 
    print(value, ' is less then 10')
else:
    print(value, ' is more than 10')