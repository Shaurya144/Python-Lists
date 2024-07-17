# Lists are one of 4 built-in data types in 
# Python used to store collections of data, the other 3 
# are Tuple, Set, and Dictionary, all with different qualities and usage.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

# List items are indexed, 
# the first item has index [0], the second item has index [1]
print(thislist[0]) # first item = apple


# List items can be of any data type
# A list can contain different data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# -1 refers to the last item
print(thislist[-1])
print(thislist[2:5])

# Check if item is in list
if "apple" in thislist:
    print("Apple is in the list")
else:
    print("Apple is not in the list")


# To change an Element in a List 
thislist[1] = "blackcurrant"
print(thislist)

# To Insert an item
thislist.insert(2, "watermelon")
print(thislist)

# The Append method adds the item to the end of the list
thislist.append("orange")
print(thislist)


# To join two lists together or append items from another list the 
# current list us the extend method
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)


# To remove Something Specific
thislist.remove("apple")

# To remove a specifc Index
thislist.pop(3)

# Use a for loop to go through a list
for x in thislist:
  print(x)