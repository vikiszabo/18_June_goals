'''
list
dictionary
list comprehension
string manipulation
string to list
list to string
'''

str1 = "hello-world"

def remove_c(string):
    for i in range(0, len(string)):
        if (string[i] == '-') or (string[i] == '_'):
            ns = string[:i+1] + string[i+1].upper() + string[i+2:]
            nns = ns.replace('-', ' ')
    return nns


print(remove_c(str1))

def rem(str):
    res = []
    for i in range(0, len(str)):
        if str[i] == '-':
            c = str[i+1].upper()

            res.append(c)
        else:
            res.append(str[i])

    return ''.join(res)


print(rem(str1))