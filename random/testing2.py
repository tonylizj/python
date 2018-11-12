def isPalindrome(word):
    return word.lower() == word[::-1].lower()

print(isPalindrome(input()))