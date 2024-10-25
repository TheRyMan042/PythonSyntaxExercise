#Ryan Hutchings
#Unit 21.1 - Python Syntax Exercise

#1.
lower_words = ['hey', 'hi', 'hello', 'sup']
for word in lower_words:
    print(word.upper())

print('\nnew function\n')
#2.
"""
    Given a list of words(strings only), make each letter uppercase for all the words and print each word onto the screen (in a new line )

    Ex:
    print_upper_words(['hey', 'Hi', 'hello', 'Sup'])

    Should be:
    HEY
    HI
    HELLO
    SUP
"""
def print_upper_words(lowercase_words):
    for word in lowercase_words:
        print(word.upper())

print_upper_words(['hey', 'Hi', 'hello', 'Sup'])

#3.
"""
    Given a list of words(strings only), make each letter uppercase for all the words that start with an 'e' in them and print them onto the screen (in a new line )

    Ex:
    print_upper_words_with_E(['Easy', 'peasy', 'elbow', 'Grease'])

    Should be:
    EASY
    ELBOW
"""
#
def print_upper_words_starting_with_E(lowercase_words):
    for word in lowercase_words:
        all_lowered = word.lower() #make all characters lowercased
        if all_lowered[0] == 'e': #index 0 is the first letter of the word
            print(all_lowered.upper())

print('\nnew function\n')

print_upper_words_starting_with_E(['Easy', 'peasy', 'elbow', 'Grease'])

#4.
"""
    Given a list of words(strings only) and starting letters, make each letter uppercase for every word that starts with any letter in the starting letters list and print those words onto the screen (in a new line)

    Ex:
    print_upper_words_with_starting_letters(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

    Should be:
    HELLO
    HEY
    YO
    YES
    
"""
def print_upper_words_with_starting_letters(lowercase_words, must_start_with):
    #goes through all the list of words
    for word in lowercase_words:
        all_lowered = word.lower()
        #goes through all the list of starting letters
        for start_letter in must_start_with:
            if all_lowered[0] == start_letter: 
                print(all_lowered.upper())

print('\nnew function\n')

# this should print "HELLO", "HEY", "YO", and "YES"
print_upper_words_with_starting_letters(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})