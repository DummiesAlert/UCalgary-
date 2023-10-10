dataPoints = int(input("How Many Data Points? "))

i = 1

while dataPoints >= 0: 
    
    dataPoints = i
    
    a = int(input(f"What is the year of data point {i}?"))
    b = float(input(f"What is the birth rate of data point {i}?"))
    
    i += 1
    
    if i != dataPoints:
        
        print("")
        
    else: 
        
        break