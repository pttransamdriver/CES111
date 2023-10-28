"""
CSE 111
Author: Tim Illguth
Instructor: Christian Eisingers
Filename: sentances.py
"""
# import the random capability which is in itself a function that someone smarter than me wrote :D
import random

# Defines the function "get_determiner()". When the "get_determiner" is called, whatever is inside the 
# "get_determiner(place_stuff_here)" is called that given parameter goes through the function
# if statment. That <place_stuff_here> I mentioned earlier, is represented by the variable "quantity"
def get_determiner(quantity_1): 
    # If statement that looks at "determiner = get_determiner(quantity_3b)" values that come from the 
    # "quantity_3a" if statments and uses that to plug into this "quantity_1" variable. 
    if quantity_1 == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

# Defines the get_noun() function. This function is called when "noun = get_noun(quantity_3b)" runs. 
# This takes that quantity and plugs it into the "quantity_2"  
def get_noun(quantity_2):
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    if quantity_2 == 1:
        return random.choice(single_nouns)
    else:
        return random.choice(plural_nouns)

# Defines the "get_verb() function. This function is called when the "verb = get_verb(quantity_3b, tense)" 
# is called. This is called when the "def make_sentence(quantity_3b, tense)" is called like the rest 
# of the funtions are called. 
def get_verb(quantity_3a, tense):
    past_verbs             = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    present_singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    present_plural_verbs   = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future_verbs = [f"will {verb}" for verb in present_plural_verbs]

    # This 'if' statment checks to see if the 'tense' parameter that is passed to the function when
    # it's called the if statment returns a 'random.choice' from the 'past_verbs' 
    if tense == "past":
        return random.choice(past_verbs)
    elif tense == "present":
        if quantity_3a == 1:
            return random.choice(present_singular_verbs)
        else:
            return random.choice(present_plural_verbs)
    elif tense == "future":
        return random.choice(future_verbs)

# Define the "get_preposition" function as a function that randomly chooses 
# from the list of preposition elements
def get_preposition():
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]
    return random.choice(prepositions)


# Define the "get_prepositional_phrase"function that takes from the  
def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner  = get_determiner(quantity)
    noun        = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"


# Defines the "make_sentance" function. This function is called when the "main()" function's 
# "make_sentance" is called. Then it calls the the "get_determiner", "get_noun" and the "get_verb"
# functions in that order
def make_sentence(quantity_3b, tense):
    determiner = get_determiner(quantity_3b)
    noun       = get_noun(quantity_3b)
    verb       = get_verb(quantity_3b, tense)

    # Capitalize the first letter of the sentence
    determiner = determiner.capitalize()

    # Build the sentence
    sentence = f"{determiner} {noun} {verb}."

    return sentence

def main():
    # Call make_sentence for different quantity and tense combinations. This you get from 
    # the "testing procedure" section of the assignment
    sentences = [
        make_sentence(1, "past"),
        make_sentence(1, "present"),
        make_sentence(1, "future"),
        make_sentence(2, "past"),
        make_sentence(2, "present"),
        make_sentence(2, "future")
    ]

    # For loop to print the sentences it sets up a loop to iterate over the sentences list. 
    # It uses the 'enumerate' function to get both the index (index) and the sentence (sentence) 
    # from the sentences list.
    for index, sentence in enumerate(sentences):
        # This takes uses the index 97 Which means 'a' to give the output the ('a', 'b', 'c', ...)
        # output as the testing procedure asks for. 
        identifier = chr(97 + index)
        # Prints the 'a', 'sentance', then 'b', 'setenace'... etc. for the output.  
        print(f"{identifier}. {sentence}") 


# Call the main function which calls the other functions. 
main()
