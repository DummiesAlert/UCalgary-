def howmanyvalues():

    g = int(input("How many values? "))
    a = []

    for i in range(0, g, 1): 

        h = int(input("enter a number:"))
        a.append(h)
        print(a)

def findmaxinlist():

    maximum = -1000

    for i in a: 

        if maximum > i:

            maximum = i

    return maximum

howmanyvalues()
print(findmaxinlist())