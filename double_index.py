#The function should return a new list where all elements
# are the same as in lst except for the element at index. 
# The element at index should be double the 
# value of the element at index of the original lst.
#If index is not a valid index,
#  the function should return the original list.


def double_index(lst, index):
  #Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
    # Adds double the value at index to the new list 
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

print(double_index([3, 8, -10, 12], 2))