#a function that checks whether a given string is a palindrome - a string that reads the same forward and backward.
#Ignore case and non-alphanumeric characters

def is_palindrome(s):
    #Step 1: Create an empty string to store cleaned characters
    cleaned = ''

    #Step 2: Loop through each character in the original string
    for char in s:
        #Step 3: Kepp only alphanumeric characters and convert to lowercase
        if char.isalnum():
            cleaned += char.lower()
        
    #Step 4: Reverse the cleaned string
    reversed_cleaned = cleaned[::-1]

    #Step 5: Compare the cleaned string with its reversed version
    if cleaned == reversed_cleaned:
        return True
    else:
        return False


print(is_palindrome("A man, a plan, a canal: Panama"))