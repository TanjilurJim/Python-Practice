#pangram =  a sentence containing a-z english alphabets
#write a function that checks if all the alphabets are present in the passed phrase
#if not mention which letters are not present

def pangram(phrase):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')  # Set of all lowercase letters
    phrase = set(phrase.lower())
    missing_letters = alphabet - phrase

    if not missing_letters:
        return "The phrase is pangram"

    else:
        missing = ''.join(sorted(missing_letters))
        return f'The phrase is not pangram. Missing letters: {missing}'


phrase = input("Please enter whatever you feel like: ")
print(pangram(phrase))

