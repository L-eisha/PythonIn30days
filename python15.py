# syntax
# # Declaring a function
# def function_name():
# #     codes
# #     codes
# # Calling a function
# function_name()


#fn without parameters

def generate_full_name ():
    first_name = 'LEISHA'
    last_name = 'CHOUDHARY'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
# RETURNING VALUE IN A Fn.

def generate_full_name ():
    first_name = 'leisha'
    last_name = 'choudhary'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())