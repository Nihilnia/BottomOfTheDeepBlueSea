# append()

"adding new item to list"

listOne = [1, 2, "nihil"]
listOne.append("ra ra rasputin")
print("List one is updated:", listOne)

# extend()

"adding new items to list from another list"

list2 = [1, 3, 5]
list3 = [2, 4, 6]
list2.extend(list3)
print("List2 is updated:", list2)

# insert()

"adding new item to list's spesific index"

list4 = [1, 3, 4, 5]
list4.insert(1, 2) # add item '2' to index '1'
print("List4 is updated:", list4)

list4.insert(3, "nihil") #add "nihil" to index3 
print("\"nihil\" is added to list's 3.index..:", list4)


# pop()

"deleting an item with index number"

list5 = ["a", 1, "b", 2, "c", 3]
list5.pop() #last item is deleted
print("Last item is deleted:", list5)

list5.pop(2) #2.index 'b' is deleted
print("2.index is deleted:", list5)

# list5.pop(8) #if you give a wrong index number, you get an error.
                # IndexError: pop index out of range


# remove()

"deleting an item with item name"

list6 = [1, 2, 3, "a", "b", "c"]
list6.remove(2) 

print("item '2' is deleted:", list6)

list6.remove("c")
print("item 'c' is deleted:", list6)

# list6.remove("n") #if you give a wrong item, you get an error.
                    # ValueError: list.remove(x): x not in list


# index()

"find an item"

list7 = ["a", "b", "c", "a", "b", "c",]
print(list7.index("b")) #1
print(list7.index("b", 3)) #4

# print(list7.index("d")) #if you give a wrong item, you get an error.
                         # ValueError: 'd' is not in list


# count() 

"count an item"

list12 = [1, 1, 1, 1, 2, 3, 2, 3, 4, 5, 6, 6, 3, 1, 2]
print(list12.count(2)) #3
print(list12.count(1)) #5
print(list12.count(12)) #0


# sort()

"""
Sort the list.
If list is numeric, then sort it small to big.
If list is alphabetic, then sort it A to Z
Note: if list alphanumeric, then do not anything."""


list21 = ["c", "y", "a", "d", "n"]
list21.sort()
print("List21 is sorted:", list21)

list32 = [2, 34634, -1, -929, 52, 1551]
list32.sort()
print("List32 is sorted:", list32)

list21.extend(list32)
print("List32's items add to list21:", list21)

# list21.sort() #we got an error:
                 # TypeError: '<' not supported between instances of 'int' and 'str'
                 #"""DO NOT FORGET: ALPHANUMERIC LIST'S CAN'T SORT"""
#PLUS: WE can sort as reversed

list32.sort(reverse = True)
print("List32 sorted as reverse", list32)