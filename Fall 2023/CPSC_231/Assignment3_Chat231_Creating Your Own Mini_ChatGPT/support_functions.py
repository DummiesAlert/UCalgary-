"""Author: Zhuo Xi Hong 
   UCID: 30213715
   Last Modified: Nov/10/2023

Prompt: Write a mini Chat231 Program using Functions

Sources:  
    
    - Punctuation (Line 31-37): https://www.geeksforgeeks.org/python-remove-punctuation-from-string/
        
    Tutorial: get_answers()
    
        - TA Naman: Helped with adapting a way to check the 'keyword' in the question

"""

#get_greetings() Function
def get_greetings(name): 
    
    #If No Name Was Entered, Basic Greet. 
    if name == "": 
        
        return "Hello there! I am your virtual assistant Chat231."
    
    #Otherwise Print Greeting With Name
    return f"Greetings {name}! I am your virtual assistant Chat231."  

#is_whole_word() Function 
def is_whole_word(word, sentence):

    punctuation = [',', '.', '!', '?', ':', ';']

    #Remove All Punctuation in the Sentence and Replace With Double Space
    for symbols in punctuation: 

        word = word.replace(symbols, '  ')
        sentence = sentence.replace(symbols, '  ')

    #Add a Space Before and After in word and sentence 
    word = f" {word} "
    sentence = f" {sentence} "

    #Make word and sentence lowercase
    word = word.lower()
    sentence = sentence.lower()

    #Check if ' ' value is in word, if yes, return 

    if ' ' in word:

        return word in sentence

#get_answers() Function
def get_answers(q_and_a, question):

    #Set question to lower() to prevent problems
    question = question.lower()
    
    #Searches for keywords in the Dictionary q_and_a. If yes, Function returns q_and_a[keyword]
    for keyword in q_and_a:
        
        if is_whole_word(keyword, question):
            
            return q_and_a[keyword]
    
    #Otherwise, return Message
    return "Sorry, I do not understand your question."

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

Test is_whole_word('HEY', 'Hello Heyden!'):
===Your return value:     False    type: <class 'bool'>
===Expected return value: False    type: <class 'bool'>
===You are correct.

Test is_whole_word('250 days', 'There are 250 days!'):
===Your return value:     True    type: <class 'bool'>
===Expected return value: True    type: <class 'bool'>
===You are correct.

Test is_whole_word('CPSC.231', 'Doo you like cpsc.231!?'):
===Your return value:     True    type: <class 'bool'>
===Expected return value: True    type: <class 'bool'>
===You are correct.

Test get_answers(q_and_a, 'Boo'):
===Your return value:     Sorry, I do not understand your question.
===Expected return value: Sorry, I do not understand your question.
===You are correct.

Test cases 8 to 14 are withheld until TA grades your assignment.
Test your functions in scenarios that have not appeared above.

Total correct: 7

Total errors: 0

** Total test case mistakes (including errors): 0
    
"""