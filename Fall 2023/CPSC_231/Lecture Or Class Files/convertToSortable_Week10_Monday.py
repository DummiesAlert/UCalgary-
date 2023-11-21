chatFile = open("meeting_saved_chat23.txt","r", encoding="utf8")
sortableChatFile = open("sortable23.csv","w", encoding="utf8")

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
