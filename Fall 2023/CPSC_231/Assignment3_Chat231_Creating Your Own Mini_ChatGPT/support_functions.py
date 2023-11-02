def get_greetings(name): 
    
    if name == "": 
        
        return "Hello there! I am your virtual assistant Chat231."
    
    return f"Greetings {name}! I am your virtual assistant Chat231." 

def is_whole_word(word, sentence): 
    
    word = word.lower()
    sentence = sentence.lower()
   
    if ' ' in word: 
       
       return word in sentence
   
    punctuation = [',', '.', '!', '?', ':', ';']
    
    for char in punctuation: 
        
        sentence = sentence.replace(char, '')
        
    words = sentence.split()
    
    for w in words: 
        if word == w: 
            
            return True 
        
    return False

def get_answers(q_and_a, question):
    
    question = question.lower()
    
    for keyword in q_and_a: 
        
        if is_whole_word(keyword, question):
            
            return q_and_a[keyword]
        
    return "Sorry, I do not understand your question."