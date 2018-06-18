'''1.2 Check permutation: Given two strings, write a method to decide if one is a permutation of the other.'''

def is_permutation(str1, str2):
    if(len(str1) != len(str2)):
        return False

    array1 = []
    for ch1 in str1:
        array1.append(ch1)

    for ch2 in str2:
        if ch2 not in array1:
            return False

    return True

print(is_permutation("haho", "hhao"))