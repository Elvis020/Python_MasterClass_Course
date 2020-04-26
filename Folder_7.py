# Intro to Dictionaries and Sets

# Example 1
fruits = {'orange': "a sweet, orange citrus fruit",
          'apple': "good for making cider",
          "lemon": "a sour, yellow citrus fruit",
          "grape": "a mall, sweet fruit growing in bunches",
          "lime": "a sour, green citrus fruit"
          }
# # print(fruits['lemon'])
# fruits['apple'] = "a crunchy sweet fruit"
# print(fruits)
# To clear out a dictionary without deleting the dictionary
# fruits.clear()
# print(fruits)
# while True:
#     enq = input("Please enter a fruit: ")
#     if enq == 'quit':
#         break
#     if enq in fruits:
#         description = fruits.get(enq)  #The get() function can be used to retrieve values in a dict
#         print(description)
#     else:
#         print("We dont have "+ enq)

# #Listing the items in a dict
# for snack in fruits:
#     print(fruits[snack])

# Ordering items in a dict
# ordered_keys = list(fruits.keys())
# # ordered_keys.sort() #OR
# order = sorted(ordered_keys)
# for f in order:
#     print(f + "-"+ fruits[f])

# OR
# for f in sorted(fruits.keys()):
#     print(f + "-" + fruits[f])
# print(fruits.keys())
# print(fruits.values())

# Another way of getting around the above code
# while True:
#     enq = input("Please enter a fruit: ")
#     if enq == 'quit':
#         break
#     description = fruits.get(enq, "We don't have "+enq)  #The get() function can be used to retrieve values in a dict
#     print(description)

# Converting dictionaries to tuples
# fruits = tuple(fruits.items()) #for everything in the dict use fruits.items()
# # print(fruits)
#
# for snack in fruits:
#     item, description = snack
#     print(item + " is " + description)
#
# print(dict(fruits))

# Example 2
# bike = {"make":"Honda",
#         "model":"250 dream",
#         "color":"red",
#         "engine_size": 250}
# # print(bike)
# print(bike['engine_size'])
# print(bike['color'])


# Example 3
# mylist = ["a", 'b', 'c', 'd']
# letters = "abcdefghijklmnopqrstuvwxyz"
# newString = ""
# newString = ",".join(letters)
# print(newString)

# Example 4
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of the road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a wellhouse for a small stream",
             4: "You are ina valley beside a stream",
             5: "You are in a forest"}
exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]
