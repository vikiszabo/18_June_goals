'''1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?'''

def is_unique(str):
    if(len(str) > 128):
        return False

    chars_in = set()
    for ch in str:
        if(ch in chars_in):
            return False
        chars_in.add(ch)
    return True

print(is_unique("hello"))