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

def greetings (name = 'Leisha'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Choudhary'))

def generate_full_name (first_name = 'Leisha', last_name = 'Choudhary'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('muskan','riya'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
# Leisha, welcome to Python for Everyone!
# Choudhary, welcome to Python for Everyone!
# Leisha Choudhary
# muskan riya
# Age:  200
# Weight of an object in Newtons:  981.0 N
# Weight of an object in Newtons:  162.0 N

print(12+3)


print(2 ** 3 ** 0)
