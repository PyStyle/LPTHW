def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# instuctions:
# 1. start python
# 2. python
# >>> import ex25
# When you import this it will create a new file on your computer called
# "ex25.pyc", which is a "Python Bytecode Document", which helps the module
# load faster in the future.

# 3. Create an object to work with.
# >>> sentence = "All good things come to those who wait."

# 4. Run "break words" and show results
# >>> words = ex25.break_words(sentence)
# can also >>> print ex25.break_words(sentence)

# 5. Run "sort_words" and show results.
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words

# 6. Run "print_first_word" (diplays automatically)
# >>> ex25.print_first_word(words)

# 7. Run "print_last_word" (diplays automatically)
# >>> ex25.print_last_word(words)

# 8. Run "sort_sentence" and show results
# >>> sorted_sentence = ex25.sort_sentence(sentence)

# 9. Run "print_first_and_last" (diplays automatically)
# >>> ex25.print_first_and_last(sentence)

# 10. Run "print_first_and_last_sorted" (diplays automatically)
# >>> ex25.print_first_and_last_sorted(sentence)

# type help(ex25) -> documentation comment
# avoid typing "ex25" at every beginning if u import the module like this:
# >>> from ex25 import *
# print_break_words(sentence)
