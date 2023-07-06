def add_numbers(num1,num2):
    sum=num1+num2
    print(sum)
add_numbers(5,9)

# function return type
def square_numbers(num):
    result=num*num
    return result
print(square_numbers(3))

# square root
# def squareroot():
# import math
# square_root=math.sqrt(4)
# print(square_root())
# squareroot()

# calculate the factorial of 5
def factorial(n):

    if n == 0:

        return 1

    else:

        return n * factorial(n-1)

print(factorial(5))    
# or
# import math
# print(math.factorial(5))

# write a function in python that calculates a square or a cube or 
# any other power of a number? How to do it ?
# to find power use pow
import math
x = math.pow(2,3) # x = 2 to the power of 3
print(x)

# How to calculate square root of a number in python
import math
y=math.sqrt(9)
print(y)
# How to filter out any digit that contains odd number in a range of number in Python
filter=""
for i in range (1000,3001):
    if i % 2 == 0:
        if '1' not in str(i) and '3' not in str(i) and '5' not in str(i) and '7' not in str(i) and '9' not in str(i):
             filter = filter+str(i)+" , "
print (filter[:-3])

#  write a program in python for the occurrences of a character given 
# the start and stop values of that string only 
# using while
check = input("Enter athe character: ")
start = int(input("Start index: "))
stop = int(input("Stop index: "))
sentence = 'PPYYTTHON'
count = 0

for i in sentence[start+1: stop]:
    if i == check:
        count+=1

print (count)