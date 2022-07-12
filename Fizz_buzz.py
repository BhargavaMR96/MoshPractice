
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        print(f"{input} is Fizz_buzz")
    elif(input % 3 == 0):
        print(f"{input} is fizz")
    elif(input % 5 == 0):
        print(f"{input} is Buzz")
    else:
        print(input)


x = input("Please enter the no. for the game: ")
fizz_buzz(int(x))
