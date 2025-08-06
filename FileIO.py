# python can used to perform operation on a file.

""" text file: .txt, .docx, .log etc
    Binary file: mp4, .mov, .png etc

  -->  We have to open file beform reading or writting.
"""
# Reading file
"""
f = open("demo.txt", "r")

data = f.read()   # read entire file.
print(data)


line1 = f.readline()  # read whole line.
print(line1)        # same for next line e.g line2


line2 = f.readline()  # if there is nothing then it genrate blank line.
print(line2)     


f.close

# Writting file

f = open("demo.txt", "w")  # use to overwrite means previous data will del and new data will saved.

f.write(" I will crack BPSC") # this line will be saved in file.

f.close()

# Append file ---> means add at the end.

f = open("demo.txt", "a")  # helps to add new data in previous file.

f.write("\n& i'm sure for this.")  # this line add at the end of previous line or file.

f.close()

""" """
r+ --> it will  start overwitting at beigning of file, pointer will at starting pos.
w+ --> turketed mode, means whole data is being cleared then we write something.
a+ --> stream is position at end of file, then we add (write) something, pointer will at starting end.
all these are used for reading and wriiting operation both. """

"""
# e.g
f = open("demo.txt", "w+")
print(f.read())
f.write("abc")
f.close 

# with syntax

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)


with open("demo.txt", "w") as f:
    f.write("new data")



# Deleting a file   --> using os [module(like a library code)]

import os

os.remove("xyz") # --> help to remove file (xyz)."""

# Q1.

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning file I\O\n")
    f.write("using python.\nI like proggraming in python.")


# Q2.

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("python", "java")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# Q3
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")    


