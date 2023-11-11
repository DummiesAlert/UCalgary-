#get_greetings() Function
def get_greetings(name): 
    
    #If No Name Was Entered, Basic Greet. 
    if name == "": 
        
        return "Hello there! I am your virtual assistant Chat231."
    
    #Otherwise Print Greeting With Name
    return f"Greetings {name}! I am your virtual assistant Chat231." 

#is_whole_word() Function 
def is_whole_word(word, sentence):
    
    # Set the sentence to lowercase for comparison
    word = word.lower()
    sentence = sentence.lower()
   
    # Checks if the word contains spaces
    if ' ' in word:
        return word in sentence

    # Assign a list containing punctuation
    punctuation = [',', '.', '!', '?', ':', ';']
    
    # Remove all punctuation in the sentence and replace with a space
    for punc in punctuation:
        word = sentence.replace(punc, ' ')
        sentence = sentence.replace(punc, ' ')
    
    # After replacing punctuation, split the sentence into words
    words = sentence.split()
    
    # For loop to check if word is in words (case-insensitive)
    for wds in words:
        if word == wds:
            return True
    
    # Otherwise, return False
    return False

#get_answers() Function
def get_answers(q_and_a, question):
    
    #Set question to lower()
    question = question.lower()
    
    #Searches for keywords in the Dictionary q_and_a. If yes, Function returns q_and_a[keyword]
    for keyword in q_and_a: 
        
        if is_whole_word(keyword, question):
            
            return q_and_a[keyword]
    
    #Otherwise, return a Message
    return "Sorry, I do not understand your question."

print(is_whole_word('hi', 'oh hi you!')) #True
print(is_whole_word('hi', 'high up in the sky!')) #False
print(is_whole_word('Chat231', 'Hi chat231!')) #True
print(is_whole_word('Chat,231', 'Hi chat,231!')) #True
print(is_whole_word('Chat', 'Hi chat,231!')) #True
print(is_whole_word('Chat', 'Hi chat231!')) #False
print(is_whole_word('chat', 'Hi!chat,231!')) #True
print(is_whole_word('CPSC.231', 'Doo you like cpsc.231!?')) #True
print(is_whole_word('NAME', 'What is your nakesake name?')) #True
print(is_whole_word('Chat', 'What chat1 of chat!chat is chatting?')) #True
print(is_whole_word('name', 'name')) #True
print(is_whole_word('final exam', 'final,exam')) #Should return False
print(is_whole_word('name', 'what is your name sake?')) #True
print(is_whole_word('deadline', "what's the ,deadline!")) #True
print(is_whole_word(',name', 'name,name')) #False
print(is_whole_word('250-days', 'There are 250 days in the school year.')) #False
print(is_whole_word('250-days', 'There are  250-days in the school year.')) #True
print(is_whole_word('apple pie', 'I like apple pieing together puzzles.')) #False
print(is_whole_word("   ", "    ")) #True
print(is_whole_word("", "")) #True