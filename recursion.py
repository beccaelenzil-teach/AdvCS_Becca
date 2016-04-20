__author__ = 'becca.elenzil'

def find_palindrome(word):
    if len(word) < 2:
        return True
    elif word[0] == word[-1]:
        return find_palindrome(word[1:-1])
    else:
        return False

print find_palindrome('becca')



