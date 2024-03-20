def is_palindrome(word):
    if(word == ''.join(reversed(word))):
        return 1
    elif(word != ''.join(reversed(word))):
        return 0

word = input()
print(is_palindrome(word))