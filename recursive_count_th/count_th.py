'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # CHECK IF EMPTY
    if word == '':
        return 0

    # BASE CASE
    # recurse until word == 2, then check
    if len(word) == 2:
        return 1 if word == 'th' else 0
    
    # MOVE TOWARDS BASE CASE
    # need to shorten word (input)
    # CALL ITSELF
    # we can check the first two characters, but then recursively check from 
    # the 2nd character on 

    return (word[:2] == 'th') + count_th(word[1:])
