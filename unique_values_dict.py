#The function 
# should return the number of unique values in the dictionary.

def unique_values(my_dictionary):
      seen_values = []
      for value in my_dictionary.values():
            if value not in seen_values:
                seen_values.append(value)
      return len(seen_values)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1