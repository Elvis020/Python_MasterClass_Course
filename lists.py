# Example 1
# IpAddress = input("Please enter an Ip Address: ")
# print(IpAddress.count("."))

# Example 2
# parrot_list = ["non pinin'", "non more", "a stiff", "bereft of live "]
# parrot_list.append("a norwegian blue")
# for state in parrot_list:
#     print("The parrot is "+ state)

# Example 3
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = even+odd
# numbers_in_order = sorted(numbers)
# # numbers.sort()  #The sort method works in the existing variable bu doesn't create  new object
# print(numbers)
# print(numbers_in_order )
#
# if numbers == numbers_in_order:
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
#
# if numbers_in_order == sorted(numbers):
#     print("The lists are equal")
# else:
#     print("The lists are not equal")

# Example 4
# list_1 = []
# list_2 = list()
# print("List_1 is {}".format(list_1))
# print("List_2 is {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
#
# print(list("The list are equal"))

# Example 5
# even = [2, 4, 6, 8]
# another_even = list(even)
# another_even.sort(reverse=True)
# another_even = sorted(even, reverse=True)
# print(another_even is even)
# print(even)
# odd = [1, 3, 5, 7, 9]
# numbers = [even,odd]
# for number_set in numbers:
#     print(number_set)
#     for value in number_set:
#         print(value)


# Example 6
menu = []
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'])
menu.append(['spam', 'egg', 'sausage', 'spam'])

# print(menu)
for meal in menu:
    if not 'spam' in meal:
        for ingredient in meal:
            print(ingredient)



















