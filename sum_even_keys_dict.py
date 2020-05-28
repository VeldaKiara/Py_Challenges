def sum_even_keys(my_dictionary):
  even = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      even += my_dictionary[key]
    return even

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6