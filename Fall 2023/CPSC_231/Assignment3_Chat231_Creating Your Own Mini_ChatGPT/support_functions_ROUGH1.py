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
    sentence = sentence.lower()
   
    # Checks if the word contains spaces
    if ' ' in word:
        return word.lower() in sentence

    # Assign a list containing punctuation
    punctuation = [',', '.', '!', '?', ':', ';', '/', '"'] # Added the /, onwards.
    
    # Remove all punctuation in the sentence and replace with a space
    for punc in punctuation:
        sentence = sentence.replace(punc, ' ')
    
    # After replacing punctuation, split the sentence into words
    words = sentence.split()
    
    # For loop to check if word is in words (case-insensitive)
    for wds in words:
        if word.lower() == wds:
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