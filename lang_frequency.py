"""
кавычки
знаки препинания - . , ! ?

[ ] english text try
"""
from collections import Counter
import string 

filepath = '/home/ildar/Projects/DevMan/5_lang_frequency/text.txt'

def load_data(filepath):
    textfile = open(filepath, "r")
    text = textfile.read()
    # content = [x.strip() for x in lines]
    textfile.close()
    return text

text = load_data(filepath)

# print(text)
# words = text.split()

# for word in words:
# 	print(word)

clean = text.translate(str.maketrans("", "", string.punctuation))

# print(clean)

words = clean.split()

# print(words)

# print(Counter(words))

category = Counter(words)

# print (type(Counter(words)))

for value, count in category.most_common():
    print(value, count)


# for key, value in Counter(words):
# 	print(key, word, "\n")


# for item in text:
# 	# print(item)
# 	# print(item.split())
# 	for i in item:
# 		print(i)

def get_most_frequent_words(text):
    pass


if __name__ == '__main__':
    pass
