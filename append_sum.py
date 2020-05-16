#The function should add the last two elements of 
# lst together and append the result to lst. <lst> is the argument.
#It should do this process three times and then return lst.

def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

print(append_sum([1, 1, 2]))