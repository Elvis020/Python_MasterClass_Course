# day = 'Saturday'
# temperature = 30
# raining = True
#
# if day == 'Saturday' and temperature > 27 or not raining:
#     print("Go Swimming")
# else:
#     print("Learn Python")


# Example 2
# name = input("Please enter your name:\t")
# if name != '':
#     print(f"Hello, {name} nice to meet you!")
# else:
#     print("Are you the man with no name?")

# Example 3
# parrot = "Norwegian Blue"
#
# letters = input("Please enter a letter:\t")
#
# if letters in parrot:
#     print(f"{letters} is in Norwegian Blue")
# else:
#     print("I don't need that letter")

# Challenge 2
# name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))
#
# if age >= 18 and age < 31:
#     print(f"Hello {name}, you are welcome to this holiday since you are {age} years old.")
# else:
#     print(f"Sorry, you are {age} years old and are not permitted to partake in this holiday.")

# Example 4
# parrot = 'Norwegian Blue'
#
# for character in parrot:
#     print(character)

# Example 5
# number = "9,2!23;37(3:03,6 854,7%7*5;807"
# separators = ""
# values = ""
#
# for char in number:
#     if not char.isnumeric():
#         separators += char
#
#
# print(separators)


# Example 6
# for i in range(1,13):
#     for j in range(1,13):
#         print("{} times {} is {}".format(i,j,i*j))
#     print("--" * 9)

# Example 7
# shopping_list = ['milk', 'nido', 'milo', 'malta', 'spam','sugar', 'rice', 'bread' ]
#
# for item in shopping_list:
#     if item == 'spam':
#         continue
#     print("Buy: "+item)

# Example 8
# shopping_list = ['milk', 'nido', 'milo', 'malta', 'spam', 'sugar', 'rice', 'bread']
#
# index = len(shopping_list)
# item_to_find = 'albatross'
# found_at = None
# for i in range(0, index):
#     if shopping_list[i] == item_to_find:
#         found_at = i
#         break
# if found_at is not None:
#     print(f"{item_to_find} is found at position {found_at} ")
# else:
#     print(f"{item_to_find} not found")
# #

# Example 9
# directions = ['north','south','east','west']
# chosen_exit = ' '
# while chosen_exit not in directions:
#     chosen_exit = input("Please choose a direction")
#     if chosen_exit.casefold() == 'quit':
#         print("Very glad ain't yah!!")
