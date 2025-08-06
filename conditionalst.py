"""#if-elif-else
# vote eg.

age = int(input("age :"))

if(age>18):
    print("you re eligible")
elif(age<18):
    print("sorry, you re not eligible.")                        

print("End of code.")

# Traffic light.

light = input("Enter color of light : " )

if(light == "red"):
    print("plz stop.")
elif(light == "green"):
    print("Go.")
elif(light  == "yellow"):
    print("look")
else:
    print("light is broken.")         
print("End of code.")"""     

#Grade based on marks.

"""marks = int(input("Enter marks : "))

if(marks >= 90):
    print("Grade A")
elif(marks >= 80):
    print("Grade B")
elif(marks >= 70):
    print("Grade C")
elif(marks >= 60):
    print("Grade D")
else:
    print("Grade F")
"""

# Nesting..... means if ke aandr if.

age1 = 16

if(age1 >= 18):
    if(age1 <= 80):
        print("can't Drive.")
    else:
        print("can Drive")
else:
    print("can't drive")        





