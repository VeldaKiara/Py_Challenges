#The function should append the size of lst 
# (inclusive) to the end of lst.
#  The function should then return this new list.


def append_size(lst):
    lst.append(len(lst))
    return lst

print(append_size([23, 42, 108]))

