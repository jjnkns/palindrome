#write a function to determine whether a word is a palindrome or not

def is_palindrome(word):

    word_len = len(word)
    
    last_index = -1 
    first_index = 0

    while first_index < word_len:
        if word[first_index]!=word[last_index]:
            return False
        last_index-=1
        first_index+=1

    return True

#alternate method - fewer steps
def is_palindrome2(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

