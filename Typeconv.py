# it means one type of var will converse in another type var.

a = 2  #int
b = 4.23 #float

sum = a + b  # auto converse
print(sum)

# int func change into str.
x = 3.14
x = int(x)
print(type(x)) 