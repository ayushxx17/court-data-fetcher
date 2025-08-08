# it is used to repeat instructions.

# while loops

"""count = 1
while count <= 5:
    print("Ayush", count)
    count +=1
    print("loop ended") """

#We also print in reverse form

"""i = 5
while i >= 1:
    print("Hello" ,i)
    i -= 1
    print("loop exit")"""

#pracice
# print number from 1 to 100
"""i = 1
while i <= 100:
    print(i)
    i += 1 """

# 2. print in reverse from

"""i = 100
while i >= 1:
 print(i)
 i -= 1
print("loop ended")"""

# 3. print multiplication table of n eg 3
"""
n = int(input(" enter number : "))
i = 1
while i <= 10:
    print(n*i)
    i += 1 """

# 4. print the element of the following list uding loops
"""
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1 """

# 5. search number x in this tuples using loops
"""
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i =0
while i < len(nums):
    if(nums[i] == x):
        print("found", i)
    else:
        print("finding..")    
    i += 1  """     

# Break & Continue  (break is used to terminate the loop,   terminate execution in the current iteration & contnue execution of loop)
"""
i = 1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i +=1 """

# for loops --> genreally used for sequential traversal.
"""
list = [1, 2, 3, 4, 5, "patato"]

for num in list:
    print(num) """

# same in tuple also
"""
tup = (1, 2, 3, 4, 5)

for num in tup:
    print(num) """

# same in string also
"""
str = "ayush"

for char in str:
    print(char)
else:                    # that type of work which we want to done at end of loop then else is used.
    print("End")    """


# 1. print all element using for loop
"""
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el) """

# 2. search number x in this tuples using loops
"""
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
        break
    idx += 1 """


# Range --> it return seq of numbers, start from 0 by default & increment by 1
# range(start, stop, stepsize)

# writing method of range

"""
for i in range(10):
    print(i)


for i in range(2, 10):
    print(i)"""

# e.g. 

for i in range(2, 100, 2):
    print(i)


    











