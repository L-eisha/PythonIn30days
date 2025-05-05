def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Leisha'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10))
 # 55
print(sum_of_numbers(100))
 # 5050

#  Leisha, welcome to Python for Everyone!
# 100
# 4
# 314.0
# 55
# None
# 5050
# None

  # syntax


 
 
def generate_full_name ():
    first_name = 'Leisha'
    last_name = 'Choudhary'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 24
    num_two = 34
    total = num_one + num_two
    print(total)
add_two_numbers()
# Leisha Choudhary
# 58