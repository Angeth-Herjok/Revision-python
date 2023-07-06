def increment(number,by):
    return number+by
result=increment(3,7)
print(result)
# you can make code more readable by using keywod arguments
def increment(number,by):
    return number+by
result=increment(3,7)
# print(increment(2 by=1))

def multiply(*numbers):
    total=1
    for number in numbers:
        total*=number
    return total
print(multiply(2,3,4,6,5))

# args**
def user_saver(**user):
    print(user["name"])
user_saver(id=2,name="John",age=22,country="Kenya",city="Nairobi")
# solution of fizzbuzz in python

def fizz_buzz(input):
    if (input % 3==0) and (input % 5==0):
        return "fizz_buzz"
    if input % 3==0:
        return "fizz"
    if input % 5==0:
        return "buzz"
    # if false or does not meet the conditions
    return input 
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))

print(fizz_buzz(7))
# it will return 7

def add(*b):
    result=0
    for i in b:
        result=result+i
        return result
    print(add(2,5,1,2))
    print(add(12,4))

    
        