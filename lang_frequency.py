from collections import Counter
from sys import argv
import string 

filepath = argv[1]

def load_data(filepath):
    textfile = open(filepath, "r")
    text = textfile.read()
    textfile.close()
    return text

def get_most_frequent_words(text):
	# remove punctuation marks
    clean = text.translate(str.maketrans("", "", string.punctuation))
    words = clean.split()
    #create collection
    category = Counter(words)
    print("10 самых популярных слов в файле:\n{}".format(filepath))
    for value, count in category.most_common(10):
        print(count, value)


if __name__ == '__main__':
    text = load_data(filepath)
    get_most_frequent_words(text)
