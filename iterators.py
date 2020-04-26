# Example 1
# string = '1234567890'
# # for char in string:
# #      print(char)
# for char in iter(string):
#     print(char)
#

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# Challenge_1
string = list([2, 3, 4, 5, 7, 8, 10, 3, 3, 4, 2, 1, 12])
string = list(["monday","tuesday","wednesday","thursday","friday","saturday","sunday",])
my_iterator = iter(string)
n = len(string)
for n in range(n):
    print(next(my_iterator))