# Sources: Punctuation used https://www.geeksforgeeks.org/python-remove-punctuation-from-string/

"chat 231"

"chat 231 this is"
"this is chat 231"

#Gotta Check Space before and after the word, and determine the length of the value word 
#and subsquentiaclly check if it matches any of the formated words. 

#get_greetings() Function
def get_greetings(name): 
    
    #If No Name Was Entered, Basic Greet. 
    if name == "": 
        
        return "Hello there! I am your virtual assistant Chat231."
    
    #Otherwise Print Greeting With Name
    return f"Greetings {name}! I am your virtual assistant Chat231."  

#is_whole_word() Function 
def is_whole_word(word, sentence): 
    
# Method 1:
    
    # #Set All Words and Sentences to lower() to Easily Handle Words in a Sentence. 
    # word = word.lower()
    # sentence = sentence.lower()
   
    # #Checks Value(s) in word
    # if ' ' in word: 
          
    #    return word in sentence
   
    # #Assign List Containing punctuation. 
    # punctuation = [',', '.', '!', '?', ':', ';']
    
    # #Remove All Punctuation in the Sentence and Replace With a Space
    # for punc in punctuation: 
        
    #     word = word.replace(punc, ' ')
    #     sentence = sentence.replace(punc, ' ')
    
    # #After Replacing Punctuation, split() sentence into words
    # words = sentence.split()
    
    # #For Loop to Check if wds is in Words, if Yes return True
    # for wds in words: 
    #     if word == wds: 
            
    #         return True
    
    # #Otherwise, return False
    # return False
    
# Method 1.5: 

    # #Set All Words and Sentences to lower() to Easily Handle Words in a Sentence. 
    # word = word.lower()
    # sentence = sentence.lower()
   
    # #Assign List Containing punctuation. 
    # punctuation = [',', '.', '!', '?', ':', ';']
    
    # #Remove All Punctuation in the Sentence and Replace With a Space
    # for punc in punctuation: 
        
    #     word = word.replace(punc, ' ')
    #     sentence = sentence.replace(punc, ' ')
    
    # #Checks Value(s) in word
    # if ' ' in word: 
          
    #    return word in sentence

# Method 2:

    punctuation = [',', '.', '!', '?', ':', ';']
    
    #Remove All Punctuation in the Sentence and Replace With a Space
    for punc in punctuation: 
        
        word = word.replace(punc, ' ')
        sentence = sentence.replace(punc, ' ')
        
    word = f" {word} "
    sentence = f" {sentence} "
    word = word.lower()
    sentence = sentence.lower()
    
    return word in sentence

#get_answers() Function
def get_answers(q_and_a, question):
    
# Method 1:

    #Set question to lower()
    question = question.lower()
    
    #Searches for keywords in the Dictionary q_and_a. If yes, Function returns q_and_a[keyword]
    for keyword in q_and_a:
        
        if is_whole_word(keyword, question):
            
            return q_and_a[keyword]
    
    #Otherwise, return a Message
    return "Sorry, I do not understand your question."
    
# print(is_whole_word("hi", "oh hi you!"))
# print(is_whole_word("hi", "high up in the sky!"))
# print(is_whole_word("Chat231", "Hi chat231!"))
# print(is_whole_word("Chat,231", "Hi chat,231!"))
# print(is_whole_word("Chat", "Hi chat,231!"))
# print(is_whole_word("Chat", "Hi chat231!"))
# print(is_whole_word("name", "name"))
# print(is_whole_word('CPSC.231', 'Doo you like cpsc.231!?'))

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