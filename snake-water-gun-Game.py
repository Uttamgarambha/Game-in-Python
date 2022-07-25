import random
lst = ['s','w','g']

chance =5
no_of_chance = 0
computer_point = 0
You_point = 0

print(" \t \t \t \t Snake,Water, Gun Game \n\n")
print("s for snake \nw for water \ng gor gun \n")

while no_of_chance < chance:
    _input = input('Snake , Water , Gun :')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie both 0 point to each \n ")

    elif _input =='s' and _random == 'g':
            You_point = You_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("Computer wins 1 point \n")
            print(f"computet_point is {computer_point} and your point is {You_point} \n")

    elif _input =='s' and _random == 'w':
            You_point = You_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("You wins 1 point \n")
            print(f"computet_point is {computer_point} and your point is {You_point} \n")

    elif _input =='w' and _random == 's':
            You_point = You_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("Computer wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {You_point} \n")

    elif _input =='w' and _random == 'g':
            You_point = You_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("You wins 1 point \n")
            print(f"computet_point is {computer_point} and your point is {You_point} \n")

    elif _input =='g' and _random == 's':
            You_point = You_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("You wins 1 point \n")
            print(f"computet_point is {computer_point} and your point is {You_point} \n")


    elif _input =='g' and _random == 'w':
            You_point = You_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("Computer wins 1 point \n")
            print(f"computet_point is {computer_point} and your point is {You_point} \n")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance +1
    print(f"{chance - no_of_chance} chnace is left out of {chance} ")

print("Game over ")

if computer_point==You_point:
    print("Tie")

elif computer_point>You_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print("your point is {You_point} and computer point is {compuer_point}")