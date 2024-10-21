# from threading import Thread
# def print_double(num):
#     print('The double of {} is {}'.format(num, num*2))
# double_maker = Thread(target=print_double, args=(10,))
# double_maker.start()
# print('Thread ended')

# from threading import Thread
# def get_squares(start, end):
#     for num in range(start, end+1, 1):
#         print('The square of {} is {}'.format(num, num*num))
# square_thread = Thread(target=get_squares, args=(10, 20))
# square_thread.start()
# print('Message One')
# print('Message Two')
# print('Message Three')

# from threading import Thread
# def get_squares(start, end):
#     for num in range(start, end+1, 1):
#         print('The square of {} is {}'.format(num, num*num))
# square_thread = Thread(target=get_squares, args=(10, 20))
# square_thread.start()
# square_thread.join()
# print('Message One')
# print('Message Two')
# print('Message Three')

# from threading import Thread
# def prime_checker(num):
#     prime = True
#     for d in range(2, int(num**0.5) + 1, 1):
#         print('{} checked with {}'.format(num, d))
#         if num % d == 0:
#             prime = False
#     if prime == True:
#         print('{} is a prime number'.format(num))
#     else:
#         print('{} is a not prime number'.format(num))


# def primes(numbers):
#     for num in numbers:
#         t = Thread(target=prime_checker, args=(num,))
#         t.start()
#         t.join()
#         print('Completed check for {}!'.format(num))



# prime_thread = Thread(target=primes, args=([4483, 4493, 4507, 4561, 4567, 4583, 4591], ))
# prime_thread.start()
# prime_thread.join()
# print('The program ended')

# from threading import Thread
# from time import sleep
# letters = ['A', 'B', 'C', 'D']


# def func():
#     for letter in letters:
#         print(letter)
#         sleep(2)



# thread = Thread(target=func)
# thread.start()
# thread.join()
# print('E')

# from threading import Thread
# from time import sleep


# def number_printer():
#     for number in range(1, 6, 1):
#         print(number)
#         sleep(1)



# thread = Thread(target=number_printer)
# thread.start()
# print('A')
# thread.join()
# print('B')


# import threading
# import random

# # Create a 2D list with 5 rows and 100 columns
# matrix = [[random.randint(1, 100) for _ in range(100)] for _ in range(5)]

# # Define a function to calculate the product of a row
# def calculate_product(row):
#     product = 1
#     for num in row:
#         product *= num
#     print(f"Product of row {matrix.index(row)}: {product}")

# # Create a thread for each row
# threads = []
# for row in matrix:
#     t = threading.Thread(target=calculate_product, args=(row,))
#     threads.append(t)
#     t.start()

# # Let the threads run and print the products in any order


# from threading import Thread
# def user_input():
#     while True:
#         number = int(input('Please enter a non-zero number: '))
#         if number == 0:
#             print('You entered zero')
#             break
#         print(number * 2)
# def checker_function():
#     while user_input_thread.is_alive():
#         pass
#     print('The thread is not alive')
# user_input_thread = Thread(target=user_input)
# checker_thread = Thread(target=checker_function)
# user_input_thread.start()
# checker_thread.start()

# import threading
# import random
# import time

# # Define a function to generate 100 random numbers
# def generate_numbers():
#     for _ in range(100):
#         print(random.randint(1, 100))
#         time.sleep(0.1)  # Simulate some work

# # Create a thread to generate numbers
# thread = threading.Thread(target=generate_numbers)

# # Start the thread
# thread.start()

# # Wait for the thread to finish execution
# thread.join()

# # Print a message when the thread completes
# print("The thread has finished execution")