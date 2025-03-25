# Program to print Alphabet Fibonacci series
a = 'A'
b = 'B'
n = int(input("Enter the number of iteration: "))
if n > 0:
    print(a)
    print(b)
    for i in range(2, n):
        c = b + a
        print(c)
        a = b
        b = c
else:
    print("Please enter a valid integer")
