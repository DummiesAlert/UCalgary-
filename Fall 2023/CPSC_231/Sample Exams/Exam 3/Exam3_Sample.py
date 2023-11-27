# # Question 1: 

# # The following code should print a set of all positive integers up to 100 
# A = set() 
# i = 0 #Change to 1, zero to neutral 
# while i < 100: #<= so it includes 100
#     A.add(i) 
#     i += 1 
    
# for i in range(100): 
#     print(A[i]) #type error: cant use index for set()

# Question 2: 

# Write a Python function that takes a dictionary as a parameter, and returns the key in 
# the dictionary with the smallest corresponding value. No error checking is necessary.

dictionary = {
    'key1': 10,
    'key2': 20,
    'key3': 30,
    'key4': 5,
    'key5': 15
}

#Method 1:

def get_smallest_value(dictionary):
    
    return min(dictionary)

print(get_smallest_value(dictionary.values()))
print(get_smallest_value(dictionary))
print(get_smallest_value(dictionary.items()))

#Method 2:

def get_smallest_value2(dictionary):
    sorted_values = sorted(dictionary.values())
    return sorted_values[1]

print(get_smallest_value2(dictionary))

#Method 3: 

sample_dict = {
  'Physics': 65,
  'Math': 65,
  'History': 75
}

# GET THE KEYS CORRESPONDING TO THE MIN AND MAX VALUES:

sample_dictMax, sample_dictMin = max(sample_dict.values()), min(sample_dict.values())

print([k for k, v in sample_dict.items() if v == sample_dictMax])
print([k for k, v in sample_dict.items() if v == sample_dictMin])