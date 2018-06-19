'''
list
dictionary
list comprehension
string manipulation
string to list
list to string
'''

str1 = "hello-bello-world"

def remove_c(string):
    ns = string
    for i in range(0, len(ns)):
        if (ns[i] == '-'):
            ns = ns[:i+1] + ns[i+1].upper() + ns[i+2:]
    nns = ns.replace('-', '')
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

#print(rem(str1))