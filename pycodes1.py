#1. Check if a number is Even or Odd
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#2. To check palindrome or not
text = input("Enter text: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#3. Find the Largest of Three Numbers
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a > b and a > c:
    print("A is largest")
elif b > c:
    print("B is largest")
else:
    print("C is largest")


#4. To check prime number or not
num = int(input("Enter number: "))
flag = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

    if flag:
        print("Prime number")
    else:
        print("Not prime")
else:
    print("Not prime")


#5. Leap year or not
year = int(input("Enter year: "))

if (year % 400 == 0):

    print("Leap Year")
else:
    print("Not Leap Year")


#6. Factorial
num = int(input("Enter number: "))
fact = 1

for i in range(1, num+1):
    fact *= i

print("Factorial:", fact)


#7. Fibonacci number
n = int(input("Enter limit: "))

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
