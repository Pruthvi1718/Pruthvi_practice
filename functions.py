#20+ examples for functions in python (Easy to Hard):
#Check even or odd function calling
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even and true"
    else:
        return f"{num} is Odd and false"
print(check_even_odd(10))

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

#square number
def square(n):
    return n * n
print(square(6))

#