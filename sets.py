# SETS

"sets have no index, do not forget that"

setOneWhatACreativeName = {1, 2, 3, 4, 123, 4, 3, 2, 11, 1}
print(setOneWhatACreativeName)

"Do not forget: Every item can be in the set only one time. (Bad english alert'!)"

for items in setOneWhatACreativeName:
    print(items, end = ", ")

"As you can see we can't reach directy items of the set."

# Set to List, Tuple..

"But we can reach with convert to a list, tuple.."

listOne = list(setOneWhatACreativeName)
print("Index 1:", listOne[1])

tupleOne = tuple(setOneWhatACreativeName)
print(tupleOne)
print("Last item of the tuple:", tupleOne[len(tupleOne) - 1]) 
#I just noticed, it's ordered automatic.


#### METHODS OF THE SETS ####

# add() - adding an item.

"""if you add same items to set, it won't work but also we won't get an error"""

exampleSetOne = {1, 2, 3, "nihil"}
exampleSetOne.add("Python")
print("Updated:", exampleSetOne) 

"""Ordered again, but it's not important
because index is not important at sets."""

exampleSetOne.add(2)
print("Updated2:", exampleSetOne)

# discard() Function - deleting an item.


"""if you discard not exist items from set, it won't work but also we won't get an error"""


rockstar = {1, 2, 3}
rockstar.discard(2)
print("2 is discarded and rockstar set is updated:", rockstar)

rockstar.discard(2)
print("2 is tried to discard again but..:", rockstar)


# difference() Function

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7}

print(set1.difference(set2)) #gives us difference between set1 than set2 {1, 2, 3}
print(set2.difference(set1)) #gives us difference between set2 than set 1 {7}

# difference_update() Function

set1.difference_update(set2) #set1 is updated
print("Set 1 is updated, new Set 1:", set1) #{1, 2, 3}


# intersection() Function

set3 = {1, 2, 3, 4, 5, 6}
set4 = {4, 5, 6, 7, 8, 9}
print("Intersection between set3 and set4:", set3.intersection(set4))
print("Intersection between set3 and set4:", set4.intersection(set3)) #same thing.

# intersection_update() Function

set3.intersection_update(set4) # {4, 5, 6}
print("set3 updated as intersection between set4:", set3)
print("Nothing happened to set4:", set4)


# isdisjoint() Function

rasputin1 = {1, 2, 3}
rasputin2 = {1, 2, 3, 4, 5}
rasputin3 = {802, 60, 15}

print(rasputin1.isdisjoint(rasputin2)) #False
print(rasputin1.isdisjoint(rasputin3)) #True
print(rasputin2.isdisjoint(rasputin3)) #True

# issubset() Function

rasputin1 = {1, 2, 3}
rasputin2 = {1, 2, 3, 4, 5}
rasputin3 = {802, 60, 15}

print(rasputin1.issubset(rasputin2)) #True
print(rasputin2.issubset(rasputin1)) #False


# union() Function

louder1 = {1, 2, 3, 4}
louder2 = {4, 5, 6}
print(louder1.union(louder2)) #{1, 2, 3, 4, 5, 6}

# union_update() Function

louder1.update(louder2)
print("Louder1 is updated as:", louder1)
print("Louder1 is not updated:", louder2)