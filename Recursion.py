# when function call itself.
"""
def show(n):
    if(n == -1):  #Base case
        return
    print(n)
    show(n - 1)

show(5)    """

# using fact.
"""
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

print(fact(5))    """ 

# Q1
"""
def cal_sum(n):
    if(n == 0):
        return 0
    else:
        return cal_sum(n-1) + n
    

sum = cal_sum(5)
print(sum)"""

#Q2
"""
def print_list(list, idx=0):
    if(idx == len(list)):
       return 
    else:
        print(list[idx])
        print_list(list, idx+1)

fruits = ["Mango", "Banana", "Litchi", "Watermelon", "Apple"]

print_list(fruits)   """   