'''
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none.
'''

arr = ["abba", "kata", "fefef", "baba"]
str1 = "abbb"

str2 = "adbca"
str3 = "baaa"

def anagram(str, arr):
    new_arr = []
    for word in arr:
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

print(is_anagram(str1, str3))

def anaggrams(word, words):

    sorted_word = sorted(word)
    return [item for item in words if sorted(item)==sorted_word]


def anag(word, words):
    lst = []

    word_len = len(word)
    sorted_word = sorted(word)
    for item in words:
        if len(item) != word_len:
            continue
        if sorted(item) == sorted_word:
            lst.append(item)
    return lst

    #return [item for item in words if sorted(item) == sorted_word]

