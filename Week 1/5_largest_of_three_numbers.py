a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

def largest_of_three_numbers(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

largest = largest_of_three_numbers(a, b, c)
print("The largest number is:", largest)