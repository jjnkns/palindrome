#write a function to determine whether a word is a palindrome or not

def is_palindrome(word):
    '''determine whether word is spelled same way forward as backwards
    returns boolean'''
    word_len = len(word)
    
    last_index = -1 
    first_index = 0

    while first_index < word_len:
        if word[first_index]!=word[last_index]:
            return False
        last_index-=1
        first_index+=1

    return True

print(is_palindrome('hannah'))
print(is_palindrome('haxnah'))
print(is_palindrome('a'))
print(is_palindrome('aa'))
print(is_palindrome('aba'))
print(is_palindrome('abax'))


        
   

# is_palindrome('abcdef')
