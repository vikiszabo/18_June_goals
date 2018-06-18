'''Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized.'''



import itertools


def to_camel_case(text):
    text.split('-')
    for index, c in enumerate(text):
        if text[index] == '-':
            str = text[:index] + text[index+1].upper() + text[index+1:]
            str = text.replace('-', '')
    return str



print(to_camel_case("the-stealth-warrior"))


szo = 'hello'

print(szo.upper())
print(szo.capitalize())

horses = [1, 2]

print(list(itertools.permutations(horses)))