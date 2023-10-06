"""import time

counter = 1
i = 1

while i >= 1:

    print("You've Been Trolled")
    
    time.sleep(0.0000000000001)
    
    i += 1

"""

userinput = str(input("Enter a word: "))
print(userinput)

while userinput != 'exit':
 
    userinput = str(input("Enter a Word (type 'exit' to exit): "))
    
    if userinput != 'exit':
        print(userinput)
    
print("goodbye")

"""

Bin: 

Enter a word: hello
hello
Enter a Word (type 'exit' to exit): how
how
Enter a Word (type 'exit' to exit): are
are
Enter a Word (type 'exit' to exit): you
you
Enter a Word (type 'exit' to exit): exit
goodbye
    
"""