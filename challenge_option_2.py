# Challenge 1: Write a function that will reverse the given input string.
def reverseString(input: str) -> str:
    return input[::-1]

# Challenge 2: Write a function that accepts three integers as input and returns as output the largest of the three.
def largestInt(num1: int, num2: int, num3: int) -> int:
    result = num1

    if (result < num2): result = num2
    if (result < num3): result = num3

    return result

# Challenge 3: Write a function that calculates the factorial of an input integer using recursion.
def factorial(num: int) -> int:
    if (num == 1): return 1;

    return num * factorial(num-1)

# Challenge 4: Write a function that calculates the Nth entry of the Fibonacci sequence.
def fib(n: int) -> int:
    if (n < 2): return 1

    fibSequence = [1, 1]

    for i in range(2, n):
        fibSequence.append(fibSequence[i-1] + fibSequence[i-2])

    return fibSequence[n-1]

# Test cases
print(reverseString("string"))
print(reverseString("Hello, World!"))

print(largestInt(1, 3, 2))
print(largestInt(1, 1, 7))

print(factorial(3))
print(factorial(5))

print(fib(5))
print(fib(2))
