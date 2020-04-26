# Example 1
# t = "a", "b", "c"
# t1 = ("a", "b", "c")
# t2 = (("a", "b", "c"))
# print(t)
# print(t1)
# print(t2)
# print(type(t))
# print(type(t1))
# print(type(t2))
# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company" "Bad Company", 1973
# budgie = "Nightflight", "Budgie", 1982
# imelda = "More Mayhea", "Imilda Day", 2011
# metallica = "Ride the Lightning", "Metallica", 1994

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# # metallica[0] = "Master of puppets" #tuples are immutable so this won't work
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)

# metallica2 = ["Ride the Lightning", "Metallica", 1994]
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)

# Example 2
# imelda = "More Mayhea", "Imilda Day", 2011, 1, "Pulling the Rug", 2, "Psycho", 3, "Mayhem", 4, "Kentish Town Waltz"
# title, artist, year,track1, track2, track3, track4, = imelda
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)

# # Challenge 2
# imelda = "More Mayhea", "Imilda Day", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# title, artist, year,tracks= imelda
# print(title)
# print(artist)
# print(year)
# for song in tracks:
#     track,title = song
#     print("\tTrack number:{} Title: {}".format(track,title))

# NB: A tuple is not mutable but if it contains a list, then only the list in tuple is mutable.
# Example for NB
imelda = "More Mayhea", "Imilda Day", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

imelda[3].append((6, "Kiiling me softly"))
title, artist, year,tracks = imelda
tracks.append((7,"Willow"))
print(title)
print(artist)
print(year)
for song in tracks:
    track,title = song
    print("\tTrack number:{} Title: {}".format(track,title))

