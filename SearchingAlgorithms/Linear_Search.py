
# linear search of an item in the list inputted by the user (python 2.7)
print("Enter numbers to be stored in a list (space separated")

""" map function in order to store the values of the two space separated integers
	map (function, iterable..) applies the function on all the items of the iterable """

# linear search of an item in the list inputted by the user

l = map(int, raw_input().split())   #enter space separated entries in a list
item = input()                      #item to be searched for
found = 0                           #check to find if th eitem has been found or not

for i in range(len(l)):             #iterating through the array
	if(l[i] == item):                 #if element found
		found = 1
		print('Item found in the list at index position : ' + str(i)) 
		break
if(found == 0):                     #if element not found
	print("Sorry, Item not found in the list ")
