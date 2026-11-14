# EXERCISE 1: Greeting Function
def greet(name):
    return f"Hello, {name}!"


# EXERCISE 2: Addition Function
def add(a, b):
    return a + b


# EXERCISE 3: Square Function
def square(number):
    return number * number


# EXERCISE 4: Even or Odd
def is_even(number):
    return number % 2 == 0


# EXERCISE 5: Find the Largest
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# EXERCISE 6: Temperature Converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# EXERCISE 7: Discount Calculator
def calculate_discount(price, discount):
    return price - (price * discount / 100)


# EXERCISE 8: Factorial (Challenge)
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# TESTS
print(greet("Ali"))                  # Hello, Ali!
print(add(10, 20))                   # 30
print(square(5))                     # 25
print(is_even(8))                    # True
print(is_even(7))                    # False
print(largest(10, 25, 15))           # 25
print(celsius_to_fahrenheit(25))     # 77.0
print(calculate_discount(1000, 20))  # 800.0
print(factorial(5))                  # 120
print(factorial(0))                  # 1
