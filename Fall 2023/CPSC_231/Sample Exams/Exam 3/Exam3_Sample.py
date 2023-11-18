# Question 1: 

# The following code should print a set of all positive integers up to 100 
A = set() 
i = 0 
while i < 100: 
    A.add(i) 
    i += 1 
    
for i in range(100): 
    print(A[i])

# Question 2: 

# Write a Python function that takes a dictionary as a parameter, and returns the key in 
# the dictionary with the smallest corresponding value. No error checking is necessary.

def get_key_with_smallest_value(dictionary):
    if not dictionary:
        return None
    
    min_value = min(dictionary.values())
    for key, value in dictionary.items():
        if value == min_value:
            return 