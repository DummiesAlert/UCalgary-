dictionary = {
    
    'key1': 10,
    'key2': 20,
    'key3': 30,
    'key4': 5,
    'key5': 15
}

def second_smallest_number(dictionary):
    
    i = 1
    while i >= 1:
    
        sort = sorted(dictionary.items())
        return sort[1]
        i -= 1
    
print(second_smallest_number(dictionary))

def get_smallest_value2(dictionary):
    sorted_values = sorted(dictionary.values())
    return sorted_values[1]

print(get_smallest_value2(dictionary))