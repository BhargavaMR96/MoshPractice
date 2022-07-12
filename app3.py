
# Xargs
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")  # debugging, Press F5 to start. to go to next line F10,
# to know the working of the function line by line F11
print(multiply(2, 3, 6, 4, 7))
