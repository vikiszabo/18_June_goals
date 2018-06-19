'''Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized.'''



import itertools


def to_camel_case(text):
    for index in range(0, len(text)):
        if text[index] == '-':
            str = text[:index+1] + text[index+1].upper() + text[index+2:]
            strr = text.replace('-', '')
    return strr



print(to_camel_case("the-stealth-warrior"))


szo = 'hello'

print(szo.upper())
print(szo.capitalize())

horses = [1, 2]

print(list(itertools.permutations(horses)))