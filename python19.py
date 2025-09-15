def sum(a, b):
    s=a+b
    return s
print(sum(2,3))
# here a, b are the argument used in a function
print(sum(12,3))
print(sum(2,36))
print(sum(78,43))
print(sum(100,17777777))
# 5
# 15
# 38
# 121
# 17777877
def cal_sum(p,r):
    s=p+r
    return s
print(cal_sum(98,2))
# None without return
# 100

#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 9

print(type(str(5) + str(2.0)))
a = int(input("enter a value " ))
