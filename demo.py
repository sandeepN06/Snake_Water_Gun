# def factorial(n):
#     fac = 1
#     for fact in range(n):
#         fac = fac*(fact+1)
#     return fac
# num = int(input("Enter the number"))
# print("Factorial is",factorial(num))


# def fun(n):
#     if n==1:
#         return 1
#
#     else:
#         return n*fun(n-1)
# num = int(input("Enter the number"))
# print(fun(num))

# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# num = int(input("Enter the number"))
# print(fib(num))





import random
lst = ['s','w','g']

chance = 10
no_of_chances = 0
computer_point = 0
human_point = 0

while no_of_chances<chance:
    _input = input("Choose any of these\nSnake or Water or gun")
    _random = random.choice(lst)

    if _input == _random:
        print("TIE no points given")

    if _input == "s" and _random == "g":
        computer_point = computer_point+1
        print(f"Your guess {_input} and computer guess is{_random}\n")
        print("Computer wins one point")
        print(f"computer_point is {computer_point} and your point is {human_point}")

    elif _input == "s" and _random == "w":
        human_point_point = human_point + 1
        print(f"Your guess {_input} and computer guess is{_random}\n")
        print("human wins one point")
        print(f"computer_point is {computer_point} and your point is {human_point}")

    elif _input == "w" and _random == "s":
        computer_point = computer_point+1
        print(f"Your guess {_input} and computer guess is{_random}\n")
        print("Computer wins one point")
        print(f"computer_point is {computer_point} and your point is {human_point}")

    elif _input == "w" and _random == "g":
        human_point_point = human_point + 1
        print(f"Your guess {_input} and computer guess is{_random}\n")
        print("human wins one point")
        print(f"computer_point is {computer_point} and your point is {human_point}")

    elif _input == "g" and _random == "s":
        human_point_point = human_point + 1
        print(f"Your guess {_input} and computer guess is{_random}\n")
        print("human wins one point")
        print(f"computer_point is {computer_point} and your point is {human_point}")

    elif _input == "g" and _random == "w":
        computer_point = computer_point+1
        print(f"Your guess {_input} and computer guess is{_random}\n")
        print("Computer wins one point")
        print(f"computer_point is {computer_point} and your point is {human_point}")

    else:
        print("You have entered wrong input\n")

    no_of_chances = no_of_chances+1
    print(f"{chance-no_of_chances} is left out of chance{chance}\n")
print("Game over")

if computer_point<human_point:
    print("You Won")

print("Computer won")

















