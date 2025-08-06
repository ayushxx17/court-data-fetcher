# sets is collection of unordered itemsq, Each element in the set must be unique & immutable.
"""collection = {1,2,3,4, "Hello", "world"}

print(collection)
print(type(collection))

#if we provide multiple same values then set will ignore them.  eg--> 2,2,2,2 oupput will 2

print(len(collection))

sets = set()
print(type(sets))

#sets methods

sets.add(2)   #add ement   same for remove.
sets.add(3)
sets.add(4)
sets.add("Hello")
print(sets)
print(len(sets))

print(sets.pop())  #pop element
print(sets.pop())

#Sets methods
# sets.union --> combine both set value  & return new

set1 = {1,2,3,4}
set2 = {5,6,7,2}

print(set1.union(set2)) 

# set.intercestion --> combines commons value & return new

print(set1.intersection(set2)) """


#problem

subjects = {
    "python", "java", "c++", "python","js", "python", "java", "c++", "c"
}

print(len(subjects))