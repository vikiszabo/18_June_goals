'''

1.3. URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.

Example

Input: "Mr John Smith          ", 13

Output: "Mr%20John%20Smith

'''

def replace_spaces_to_string(str, n):
    str = str.strip()
    new_string = str.replace(' ', '%20')

    return new_string


str1 = "Mr John Smith          "
n1 = 13

print(replace_spaces_to_string(str1, n1))


def replace_spaces(str):
    res = []
    start = False
    str = str.strip()
    for char in reversed(str):
        if(char == ' '):
            res += '02%'
        else:
            res += char
    res = ''.join(res[::-1])
    return res

print(replace_spaces(str1))

