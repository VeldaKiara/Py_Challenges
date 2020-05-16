#The function should return a
# list where all elements in lst with an 
# index between start and end (inclusive) have been removed.

def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))