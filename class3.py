# Example1
# import random
#
# highest = 1000
# answer = random.randint(1, highest)
# # print(answer) #TODO: Remember to remove this ine after development
# print("Please enter 'q' to quit ")
# guess = int(input(f"Please guess a number between 1 and {highest}: "))
#
# while guess != answer:
#     if guess == 0:
#         break
#     elif guess < answer:
#         print("Please guess higher")
#         guess = int(input())
#     elif guess > answer:
#         print("Please guess lower")
#         guess = int(input())
#         continue
# else:
#     print("Well done, you guessed it!")


# The Hilo Game
# low = 1
# high = 1000
# guesses = 1
# print("Please guess a number between {} and {} ".format(low, high))
# print("Press Enter to continue")
#
# while low != high:
#     guess = low + (high - low) // 2
#     high_low = input("I guessed {}, Should I guess high or lower? "
#                      "Please enter h or l, or c if my guess is correct "
#                      .format(guess)).casefold()
#
#     if high_low == 'h':
#         low = guess + 1
#     elif high_low == 'l':
#         high = guess - 1
#     elif high_low == 'c':
#         print("I got it in  {} guesses !".format(guesses))
#         break
#     else:
#         print("Please enter h, l or c")
#     guesses += 1
# else:
#     print("You though of the number {}".format(low))
#     print("And I got it in {} guesses !".format(guesses))

# Challenge 35
# print("Please choose an option: ")
# index = [1, 2, 3, 4, 5, 6, 0]
# op1 = print("{}. Learn Python".format(index[0]))
# op2 = print("{}. Learn Java".format(index[1]))
# op3 = print("{}. Go Swimming".format(index[2]))
# op4 = print("{}. Have dinner".format(index[3]))
# op5 = print("{}. Go to bed".format(index[4]))
# op6 = print("{}. Exit".format(index[5]))
#
# user_input = int(input("\n"))
# while user_input <= len(index):
#     if user_input == index[0]:
#         print("Thanks for selecting {}".format(index[0]))
#         user_input = int(input("\n"))
#     elif user_input == index[1]:
#         print("Thanks for selecting {}".format(index[1]))
#         user_input = int(input("\n"))
#     elif user_input == index[2]:
#         print("Thanks for selecting {}".format(index[2]))
#         user_input = int(input("\n"))
#     elif user_input == index[3]:
#         print("Thanks for selecting {}".format(index[3]))
#         user_input = int(input("\n"))
#     elif user_input == index[4]:
#         print("Thanks for selecting {}".format(index[4]))
#         user_input = int(input("\n"))
#     elif user_input == index[5]:
#         break

# Chaenge 35 -solution
choice = '-'
while choice != '0':
    if choice in "123456":
        print("You chose {}".format(choice))
    else:
        print("Please choose an option: ")
        print("1.\tLearn Python")
        print("2.\tLearn Java")
        print("3.\tGo Swimming")
        print("4.\tHave dinner")
        print("5.\tGo Partying")
        print("6.\tLearn C++")

    choice = input()


