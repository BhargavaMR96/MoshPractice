print("hello world")
# To execute press (ctrl + `) a terminal will open
# SAVE and Execute , otherwise it wont show the changes
# install Python extension
# pyLint extension helps in showing the errors while coding rather thn waiting until executed
# Format docuent on save
# code runner to avoid typing python and filename in terminal to execute
# (ctrl+alt+n) - to run the code and expect the o/p in O/P terminaal
students = 1000
rating = 4.99
print(students, ', ', rating)
course = "Python \" programming"  # escape sequence '\', \n,\\

first = 'Mosh'
last = 'Hame'
full = first + ' ' + last
full2 = f"{first} {last}"
print(full, "\n", full2)

# Ternary operator
age = 32
messsage = "Eligible" if age >= 18 else "Not eligible"
print(messsage)

# chaining conparison operators
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")

# FOR Else
successfull = False
for number in range(3):
    print("Attempt")
    if successfull:
        print("successful")
        break
else:
    print("Attempted 3 times and failed")

# Even numbers
a = 0
for i in range(1, 10):
    if(i % 2 != 1):
        print(i)
        a += 1
print(f"We have {a} even numbers")
