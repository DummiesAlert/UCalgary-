import sys

print(sys.argv)

file_opened = False
filename = sys.argv[1]
while not file_opened:

    try:
        chatFile = open(filename,"r", encoding="utf8")
        print("managed to open the file")
        file_opened = True
#        x = 1/0
    except FileNotFoundError as file_error:
        print(file_error)
        filename = input("couldn't open file " + filename + ".\nWhat is the name of the file ")
    except ZeroDivisionError:
        print("zero division error")
    else:
        print("no errors encountered when opening the file")
    finally:
        print("finally block: maybe there was an error, maybe not, but I really want to do this")
        
    
sortableChatFile = open(sys.argv[2],"w", encoding="utf8")

line = chatFile.readline()
while line != "":
    if (line[0].isdigit()):
        sortableChatFile.write("\n")
    words = line.strip().split(" ")
    for word in words:
        sortableChatFile.write(word)
        sortableChatFile.write(',')
    line = chatFile.readline()
        
chatFile.close()
sortableChatFile.close()
