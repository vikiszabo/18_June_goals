import ast


fruits = "['alma', 'korte', 'banan', 'eper']"

fruits = ast.literal_eval(fruits)

print(fruits[0])

'''convert string ot list'''

str1 = "hello"
str1 = str1.replace('l', 'd')

li = list(str1.split("-"))

print(li)

movies = ["Giant", "Alma", "Go", "Goblin", "Ebe", "Z"]

gmovies = [title for title in movies if title.startswith('G')]

print(gmovies)

movies2 = [("Giant", 2001), ("Alma", 1999), ("Go", 2017), ("Goblin", 2014), ("Ebe", 2013), ("Z", 2012)]

pre2k = [title for (title, year) in movies2 if year < 2000]

print(pre2k)

nums = [ 1, 2, 3]

multip4 = [4*num for num in nums]

print(multip4)


A = [1, 3, 5, 7]

B = [2, 4, 6, 8]

cart_pro = [(a, b) for a in A for b in B]

print(cart_pro)