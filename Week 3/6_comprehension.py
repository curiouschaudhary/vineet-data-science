# Q6. Use a list comprehension to filter even numbers from a list. 

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in list if num % 2 == 0]
print(even_numbers)