'''🔥 Level 1 — Very Easy

Store your name and age in variables and print:
My name is ___ and I am ___ years old.

Create variables of all data types (int, float, string, bool, None) and print their types.

Swap two variables (a = 5, b = 10 → swap them).

Check if two numbers are equal using comparison operators.

Take a string input and print its length using len().'''


name = 'ayan'
age = 15
print(f'My name is {name} and I am {age} years old')

# int = -12
float = 12.3
string = 'named string'
bool = True
bool2 = False
none = None

print(type(int))
print(type(float))
print(type(string))
print(type(bool))
print(type(bool2))
print(type(none))



a = 5
b = 10

print('Before swap ', a, b)

tem = a
a = b
b = tem 

print('Before swap ', a, b)


Number1 = int(input("Enter you rnumber: "))
Number2 = int(input('Enter 2nd number '))

if Number1 == Number2 :
    print('Equal')
else:
    print("Unequal")



Its_a_String = 'Here is the string. I need to check its length'
print(len(Its_a_String))