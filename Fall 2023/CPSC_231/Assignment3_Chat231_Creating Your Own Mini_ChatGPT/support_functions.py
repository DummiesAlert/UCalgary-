def get_greetings(name): 
    
    if name == "": 
        
        return "Hello there! I am your virtual assistant Chat231."
    
    return f"Greetings {name}! I am your virtual assistant Chat231." 

def is_whole_word(word, sentence): 
    
    sentence = get_greetings() 

    word = "Hello"

    if word in sentence:

        return True
    
    else: 

        return False
 
"""A whole word is defined to be a word that is not a part of another word. For example: 
# • In the sentence "oh hi you!", "hi" is a whole word, so the function should return True.   
# • In the sentence, "high up in the sky", the word "hi" does not exist as a whole word since 
# it is a part of "high", so the function should return False.  
# • Normally in a sentence, any spaces or punctuations (comma, period, question mark, 
# exclamation mark, colon, and semicolon) separate two words. Numbers do not separate 
# a word.  For example, "Chat,231" are two words.  "Chat231" is one word. 
# • However, the string value of the parameter word is considered one word, regardless of 
# whether it contains spaces or other symbols in it.  For example, if word is “final exam”, 
# then “final exam” is defined to be one word, and the space in it is considered a part of 
# this word (this rule overrides the previous rule). 
# • If the word does not appear at all in the sentence, the function returns False.  
# More examples: 
# Given parameter values when function is called: Function should 
# return: 
# Reason 
# is_whole_word("hi", "oh hi you!") True hi is a whole word 
# is_whole_word("hi", "high up in the sky!") False hi is a part of high 
# is_whole_word("Chat231", "Hi chat231!") True Chat231 is a whole word 
# is_whole_word("Chat,231", "Hi chat,231!") True Chat,231 is a whole word 
# since comma is considered a 
# part of this word 
# is_whole_word("Chat", "Hi chat,231!") True Chat is a whole word. The 
# comma separates Chat and 
# 231. 
# is_whole_word("Chat", "Hi chat231!") False Chat is a part of Chat231 
 
# This function is case insensitive – meaning any combination of upper/lower case words are 
# accepted as valid, so "HI" counts as appearing in "hi you." Note: this is a different requirement 
# than assignment 1. You are building a chatbot, after all, and people don’t follow proper 
# grammar when chatting. """

def get_answers(q_and_a, question):
    print("")
    
    
""" # Step 8: 
# Create a new custom function in your support_functions.py file, called get_answers(q_and_a, 
# question).  The function has the following: 
# Parameters:  
# q_and_a, a dictionary 
# question, a string. 
# Returns: a string. 
# q_and_a will be assigned by the caller to be question keywords and their corresponding answers 
# in a dictionary. Here is one example of what it might look like (you can’t assume this is the only 
# value for the dictionary, since the dictionary, as a parameter, can be assigned any arbitrary value 
# by whoever is calling this function): 
#     { 
#         "name": "I am Chat231. My nickname is Riley.", 
#         "textbook": "The textbook we use is called The Python Workbook 2nd Edition.", 
#         "final exam": "The final exam will be on December 18th at 5-7pm. Check D2L for details." 
#     } 
 
# The basic idea is: 
# Your function will scan the user question for any keywords that appear in the dictionary. If a 
# keyword is found, the corresponding answer in the dictionary is returned. 
# For example, if the user types in “What’s your name?” , your function checks this sentence for 
# the keywords. If it sees “name”, it assumes the user is asking about name, and returns the 
# answer “I am Chat231. My nickname is Riley.” 
# Now, your get_answers function must call your own is_whole_word function at some point to 
# make sure the keyword is, in fact, a whole word and not a part of another word. 
# For example, if the user types in “What’s your namesake?” , your function checks this sentence, 
# calls is_whole_word on the keyword “name”.  The function is_whole_word returns False, telling 
# you that “name” is not a whole word in the sentence.  You keep checking other keywords. If no 
# other keywords appear in the sentence, Chat231 can’t answer the question, and this function 
# should return 
# "Sorry, I do not understand your question." 
 
# Copyright ©  2023. Do not distribute outside of the CPSC 231 Fall 2023 class. 
# See more examples below. Here q_and_a represents the entire dictionary, assuming the 
# dictionary example above is given to the function. 
# Given parameter values when function is called: Function should return: 
# get_answers(q_and_a, "Name!?") "I am Chat231. ..." (the full sentence) 
# get_answers(q_and_a, "What Textbook, do we 
# use?") 
# "The textbook we use is ..." 
# get_answers(q_and_a, "What’s on final exam.") "The final exam will be on December ..." 
# get_answers(q_and_a, "Ha ha ha!") "Sorry, I do not understand your ..." 
 
# Everything here is case insensitive – any upper/lower case combination of words should be 
# recognized as words. 
# You can assume the sentence will contain at most one keyword from the dictionary. If multiple 
# keywords appear in the sentence, choose any one keyword and return its answer