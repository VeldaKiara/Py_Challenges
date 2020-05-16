#The function should return the last element 
# of the list that contains more elements. 
# If both lists are the same size, 
# then return the last element of lst1.

def larger_list(lst1, lst2):
    if len(lst1) > len(lst2):
        return lst1[-1]
    elif len(lst2) > len(lst1):
        return lst2[-1]
    else:
        return lst1[-1]
        
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))       
        
    
        
    
        


