#Create a function named more_than_n that has three parameters
#  named lst, item, and n.
#The function should return True if item appears in the
#  list more than n times. The function should return 
# False otherwise.

def more_than_n(lst, item, n):
      if lst.count(item) > n:
        return True
      else:
        return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))