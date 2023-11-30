c = 1
a = []

if c == 1:
    try:
            
        with open('exit.txt', 'r') as exit_file:
                
            line = exit_file.readline().strip()
            #b = (int(line[0]), int(line[1]))
                
    except FileNotFoundError:
            
        print("Exit file not found")
print(line)