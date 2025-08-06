# block of state. that perform a specific task. (block of code which take input as a parameter & return output)
#function definition
"""def cal_sum(a, b):  # (a, b) are parameters.
    sum = a + b     # return a + b ( we can also write)
    print(sum)

cal_sum(5, 7)    # function call, (5, 7) are arguments

def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()"""

# avg of 3 numbers
def cal_avg(a, b, c):
    sum = a + b + c
    avg = sum /3
    print(avg)

cal_avg(3, 3, 3)

# types of function (built in[print, type, range, len], user defined fun  )
# Default parameter --> those values which r used whwn no arugments are pased.

"""def cal_prod(a, b=1):
    print(a * b)
    return a * b

cal_prod(1, 7)
cal_prod(3, 7)
cal_prod(1)"""

#practice

"""cities = ["delhi", "gurgoan","Noida", "pune", "Mumbai"]

def print_len(list):
    print(len(cities))
  

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)"""

# 03
"""n = 5

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
       fact *= i
    print(fact)    

cal_fact(5)    """

#04.

def convertor(usd_value):
    inr_value = usd_value * 83
    print(usd_value, "USD =", inr_value, "INR")

convertor(75)















