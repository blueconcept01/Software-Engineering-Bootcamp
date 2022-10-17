
def add_three_nums(a, b, c):
    return a + b + c

def double_num(a):
    return a * 2

def is_even(a):
    return (a % 2) == 0

def is_negative(a):
    return a < 0

def increment_by(a, i=1):
    a += i

def add_one(arr):
    arr.append(1)

b = 1
increment_by(b, i=10)
print(b)

lst = []
add_one(lst)
print(lst)