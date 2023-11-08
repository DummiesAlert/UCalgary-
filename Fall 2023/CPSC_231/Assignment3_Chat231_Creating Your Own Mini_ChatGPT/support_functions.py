"chat 231"

"chat 231 this is"
"this is chat 231"

#Gotta Check Space before and after the word, and determine the length of the value word 
#and subsquentiaclly check if it matches any of the formated words. 

#Chatgpt: python code to check if do nut matches donut in a sentence

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
        
        sentence = sentence.replace(punc, ' ')
    
    #After Replacing Punctuation, split() sentence into words
    words = sentence.split()
    
    #For Loop to Check if wds is in Words, if Yes return True
    for wds in words: 
        if word == wds: 
            
            return True
    
    #Otherwise, return False
    return False

#get_answers() Function
def get_answers(q_and_a, question):
    
    #Set question to lower()
    # question = question.lower()
    
    #Searches for keywords in the Dictionary q_and_a. If yes, Function returns q_and_a[keyword]
    for keyword in q_and_a: 
        
        if is_whole_word(keyword, question):
            
            return q_and_a[keyword]
    
    #Otherwise, return a Message
    return "Sorry, I do not understand your question."

# def get_answers(q_and_a, question):

#     question = question.lower()
    
#     answer = q_and_a.get(question, None)
    
#     if answer is not None:
#         return answer
    
#     return "Sorry, I do not understand your question."

# def get_answers(q_and_a, question):

#     question = question.lower()

#     matched_answers = [q_and_a[key] for key in q_and_a if is_whole_word(key, question)]

#     if matched_answers:

#         return matched_answers[0]

#     return "Sorry, I do not understand your question."

print(is_whole_word('CPSC.231', 'Doo you like cpsc.231!?')) #Should Return True

"""
    
Screen Dump: 

The following results are created by the auto-grader.
Test get_greetings("Mac"):
===Your return value:     "Greetings Mac! I am your virtual assistant Chat231."
===Expected return value: "Greetings Mac! I am your virtual assistant Chat231."
===You are correct.

Test get_greetings(""):
===Your return value:     "Hello there! I am your virtual assistant Chat231."
===Expected return value: "Hello there! I am your virtual assistant Chat231."
===You are correct.

Test is_whole_word('hi', 'Hi2,there!'):
===Your return value:     False    type: <class 'bool'>
===Expected return value: False    type: <class 'bool'>
===You are correct.

Test is_whole_word('Hey', 'Hello Heyden!'):
===Your return value:     False    type: <class 'bool'>
===Expected return value: False    type: <class 'bool'>
===You are correct.

Test is_whole_word('250 days', 'There are 250 days!'):
===Your return value:     True    type: <class 'bool'>
===Expected return value: True    type: <class 'bool'>
===You are correct.

Test is_whole_word('CPSC.231', 'Doo you like cpsc.231!?'):
===Your return value:     False    type: <class 'bool'>
===Expected return value: True    type: <class 'bool'>
===You are NOT correct.

Test get_answers(q_and_a, 'Boo'):
===Your return value:     Sorry, I do not understand your question.
===Expected return value: Sorry, I do not understand your question.
===You are correct.

Test cases 8 to 14 are withheld until TA grades your assignment.
Test your functions in scenarios that have not appeared above.

Total correct: 6

Total errors: 0

** Total test case mistakes (including errors): 1
    
"""