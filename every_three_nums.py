#The function should return a list of every 
# third number between start and 100 (inclusive). 
# For example, every_three_nums(91) should return the 
# list [91, 94, 97, 100].
#  If start is greater than 100,
#  the function should return an empty list.

def every_three_nums(start):
    return list(range(start, 101, 3))

print(every_three_nums(91))