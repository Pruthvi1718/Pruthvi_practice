#Simple Calculator
a = input("Enter first number: ")
b = input("Enter second number: ")
op = input("Enter operation (+, -, *, /): ")
print("Result =", eval(a + op + b))


#another way
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    print("Result =", a / b)
else:
    print("Invalid Choice")




#BASIC EXAMPLES on CONDITIONS, LOOPING & FUNCTIONS
n = int(input("Enter Number:"))
if n % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")


age = int(input("Enter age: "))
if age >= 18:
    print("You can vote")
else:
    print("Not eligible")


age = int(input("Enter age: "))
if age > 18:
    print("You can vote")
elif age == 18:
    print("You can wait 1 year")
else:
    print("You can vote")

a = 10
b = 20
if a > b:
    print(a)
else:
    print(b)


a = 30
b = 20
if a > b:
    print("a is greater")
else:
    print("b is greater")

a = 20
b = 30
c = 40
if a > b:
    print("a is greater")
elif b > c:
    print("b is greater")
else:
    print("c is greater")


a = 70
b = 60
c = 50
if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")

a, b, c = 10, 20, 5
print(max(a, b, c))


m = 85
if m >= 90:
    print("A")
elif m >= 75:
    print("B")
else:
    print("C")


n = -5
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

n = 25
if n % 5 == 0:
    print("Divisible")

y = 2024
if (y % 400 == 0):
    print("Leap Year")

pwd = "abc123"
if pwd == "abc123":
    print("Login Success")





for i in range(1, 6):
    print(i)

for i in range(1, 6):
    print(i)
    print("")

s = 0
for i in range(1, 11):
    s += i
print(s)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

for ch in "PYTHON":
    print(ch)

n = 5
for i in range(1, 11):
    print(n * i)





