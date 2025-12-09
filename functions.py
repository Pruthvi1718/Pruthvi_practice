#20+ examples for functions in python (Easy to Hard):
#Check even or odd function calling
def func1(num):
    if num % 2 == 0:
        return f"{num} is Even and true"
    else:
        return f"{num} is Odd and false"
print(func1(10))

def even1(n):
    return n % 2 == 0
print(even1(7))


#Simple function
def greet():
    print("Hello!")
greet()

#function with parameter
def fun1(name):
    print("Welcome", name)
fun1("ABC")

# add 2 numbers
def add(a, b):
    return a + b
print(add(10, 5))

def subtract(a, b):
    return a - b
print(subtract(20, 8))

#square number
def square(n):
    return n * n
print(square(6))

#default parameter
def country(name="India"):
    print("Country:", name)
country()
#country("Japan")

#function with keywords
def details(name, age):
    print(name, age)
details(age=21, name="PQR")

#function with positional
def multiply(a, b):
    print(a * b)
multiply(5, 4)

#reverse string
def reverse(s):
    return s[::-1]
print(reverse("python"))

#count vowels
def vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count
print(vowels("nidurie"))

#tables with function
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)
table(9)

#factorial with loop
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
print(fact(5))

#function with arguments
def total(*nums):
    return sum(nums)
print(total(5, 10, 15))

#function inside function
def outer():
    def inner():
        return "Hello! itd"
    return inner()
print(outer())

#function with keyarguments
def info(**data):
    print(data)
info(name="Pruthvi", age=21, city="Bengaluru")

#function returning another function
def outer():
    def inner():
        return "Hello"
    return inner
f = outer()
print(f())

#function with lamda
add = lambda a, b: a + b
print(add(10, 20))

#map
num = [1,2,3,4]
result = list(map(lambda x: x*2, num))
print(result)

#filter
nums = [10,15,20,25]
even = list(filter(lambda x: x%2==0, nums))
print(even)

#reduce
from functools import reduce
nums = [1,2,3,4]
print(reduce(lambda a,b: a+b, nums))

#palindrome
def palindrome(s):
    return s == s[::-1]
print(palindrome("madam"))

#function with closures and wrapper
def my_decorator(func):
    def wrapper():
        print("User need to verify!")
        func()
        print("User Verified.")
    return wrapper

@my_decorator
def say_hello():
    print("User Details")
say_hello()

#remove duplicants
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1,2,2,3,3,4]))

#to find second largest
def second_largest(lst):
    return sorted(list(set(lst)))[-2]
print(second_largest([10,20,4,45,99]))

#function in error handling
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(divide(10, 0))

#merge 2 dictionaries
def merge_dictionary(d1, d2):
    return {**d1, **d2}
print(merge_dictionary({"a":1}, {"b":2}))


#using function count characters
def frequency(s):
    return {ch: s.count(ch) for ch in s}
print(frequency("banana"))