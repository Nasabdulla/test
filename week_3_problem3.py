def vowel(words):

    vowels = "AEIOUaeiou"
    # remove vowals for the user input
    return ''.join(char for char in words if char not in vowels)

user = input("Enter a text:")
result = vowel( user )
print(result)
