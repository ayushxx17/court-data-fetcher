# Dictionary are used to store data value in key:value pair. && they re mutable.
"""
info = {
    "key" : "value",
    "name" : "Ayush",
    "subject" : ["python", "java", "c" ],
    "topics" : ("dict" , "sets"),
    "age" : "22",
    "is_adult" : "True",
    "cg" : "6.5"
    
    }
print(type(info))  # we can also print it one by one means like key, name, etc.
print(info["name"])
print(info["topics"])
print(info["age"])
print(info["cg"])

info["name"] = "Ayush Singh" # we can also change like this in dict.
print(info) """

"""# we can also create null dict.

null_dict = {}
null_dict["name"] = "ayush"
print(type(null_dict))
"""
"""# Nested dict.
student = {
    "name" : "Ayush Singh.",
    "subjects" : {
        "phy" : 92,
        "maths" :78,
        "chem" : 95
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])"""

# Dict methods.
"""
student = {
    "name" : "Ayush Singh.",
    "subjects" : {
        "phy" : 92,
        "maths" :78,
        "chem" : 95
    }
}

print(student.keys())                #print all keys.
print(list(student.keys()))          #typecasting.

print(student.values())              #print all values.
print(list(student.values()))

print(student.items())               #return all key:value pair as a tuples.
print(list(student.items()))

print(student.get("name"))                 #return key according to value. /or
print(student["name"])                     #both print same things.

Example ---> if any key does't exist.
print(student["name2"])   ---> error 
print(student.get("name2"))    #--> no error show none (after code will run)

new_dict = {"place" : "Delhi"}
student.update(new_dict)       #update the dict.
print(student) """




# practice ques

dict = {
    "cat" : "a small animal",
    "table" : [" a piece of furniture", "list of fact and fax"]
}

print(dict) 

dict1 ={}
print(dict1)

x = int (input("enter phy : "))
dict1.update({"phy" : x})


x = int (input("enter maths: "))
dict1.update({"maths" : x})

x = int (input("enter chem : "))
dict1.update({"chem" : x})

print(dict1)
