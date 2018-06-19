'''
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none.
'''

arr = ["abba", "kata", "fefe", "baba"]
str1 = "abab"

str2 = "adbca"


def anagram(str, arr):
    new_arr = []
    for word in arr:
        if len(word) != len(str):
            return False
        if(is_anagram(str, word)):
            new_arr.append(word)
    return new_arr

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    for ch1 in str1:
        for ch2 in str2:
            if ch1 not in str2:
                return False
            elif ch2 not in str1:
                return False

    return True

print(anagram(str1, arr))

def anaggrams(word, words): return [item for item in words if sorted(item)==sorted(word)]