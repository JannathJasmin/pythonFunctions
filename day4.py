# 1) wrtie a program to find the fibonacii series using function
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
length = int(input("Enter the length of the Fibonacci series: "))
fibonacci(length)
print()

#2.find the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number to calculate its factorial: "))
print("Factorial of", number, "is", factorial(number))

# 3) print the prime numbers within a range
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def print_primes(start, end):
    print("Prime numbers between", start, "and", end, "are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
print_primes(start_range, end_range)

# 4) Palindrome check using slicing
def is_palindrome(s):
    return s == s[::-1]
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
# 5) find the occurrence of a character in a given string.
given_string = input("Enter a string: ")
character_to_find = input("Enter a character to find: ")

occurrences = given_string.count(character_to_find)
print(f"The character '{character_to_find}' appears {occurrences} times in the given string.")

# find the armstrong numbers in an interval
def is_armstrong(number):
    return number == sum(int(digit) ** len(str(number)) for digit in str(number))
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
armstrong_numbers = [num for num in range(start, end + 1) if is_armstrong(num)]
print("Armstrong numbers in the interval [{}, {}]: {}".format(start, end, armstrong_numbers))



