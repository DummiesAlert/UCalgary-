#get_greetings() Function
def get_greetings(name): 
    
    #If No Name Was Entered, Basic Greet. 
    if name == "": 
        
        return "Hello there! I am your virtual assistant Chat231."
    
    #Otherwise Print Greeting With Name
    return f"Greetings {name}! I am your virtual assistant Chat231." 

#is_whole_word() Function 
def is_whole_word(word, sentence): 
    
    #Set All Words and Sentences to lower() to Easily Handle Words in a Sentence. 
    word = word.lower()
    sentence = sentence.lower()
   
   #Checks Value(s) in word

    if ' ' in word: 
       
       return word in sentence
   
    #Assign List Containing punctuation. 
    punctuation = [',', '.', '!', '?', ':', ';']
    
    #Remove All Punctuation in the Sentence and Replace With a Space
    for punc in punctuation: 
        
        sentence = sentence.replace(punc, '')
    
    #After Replacing Punctuation, split() sentence into words
    words = sentence.split()
    
    #For Loop to Check if wds is in Words, if Yes return True
    for wds in words: 
        if word == wds: 
            
            return True 
    
    #Otherwise, return False
    return False    #Set All Words and Sentences to lower() to Easily Handle Words in a Sentence. 

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