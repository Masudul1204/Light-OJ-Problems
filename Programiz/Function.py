# Example-1
# def greet():
#     print('Hello World!')
# greet()
# print('Outside Function')

# Example-2
# def add_numbers(num1, num2):
#     sum = num1 + num2
#     print('Sum: ', sum)

# add_numbers()

# Example-3
# def find_square(num):
#     result = num * num
#     return result

# square = find_square(int(input('Enter a number: ')))
# print('square: ', square)

# Example-4
# def add_numbers(num1, num2):
#     sum = num1 + num2
#     return sum
# result = add_numbers(5, 4)
# print('Sum: ', result)

# Example-5
# import math
# square_root = math.sqrt(4)

# print("Square Root of 4 is", square_root)

# power = pow(2, 3)
# print("2 to the power 3 is", power)

# Example-6
# def get_square(num):
#     return num * num

# for i in [1,2,3]:
#     result = get_square(i)
#     print('Square of',i, '=', result)

## Function Argument

# Example-1
# def add_number(a, b):
#     sum = a + b
#     print('Sum: ', sum)

# add_number(2,3)

# Example-2
# def add_number( a = 7, b = 8):
#     sum = a + b
#     print('sum:', sum)

# add_number(2,3)
# add_number(a = 2)
# add_number()

# Example-3
# def display_info(first_name, last_name):
#     print('First Name:', first_name)
#     print('Last Name:', last_name)

# display_info(last_name='Cartman', first_name='Eric')

# Example-4
# def find_sum(*numbers):
#     result = 0
#     for num in numbers:
#         result = result + num

#     print("Sum = ", result)

# find_sum(1, 2, 3)
# find_sum(4,9)

## Recursion Function

# Example-1

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return (n * fact(n-1))

# print(fact(5))

## Anonymous Function

# Example-1
# greet = lambda : print('Hello World')

# greet()

# Example-2

# greet_user = lambda name : print('Hey there,', name)

# greet_user('Masud')

## Global, Local and Nonlocal

