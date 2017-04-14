from collections import Counter
from sys import argv
import string 

filepath = argv[1] 

def load_data(filepath):
    with open(filepath, "r") as textfile:
        text = textfile.read()
    return text

def get_most_frequent_words(text, count):
	# remove punctuation marks
    clean_text = text.translate(str.maketrans("", "", string.punctuation))
    words = clean_text.split()
    collection = Counter(words)
    return collection.most_common(count)


if __name__ == '__main__':
    text = load_data(filepath)    
    top_number = 10
    print("{} самых популярных слов в файле:\n{}".format(top_number, filepath))
    for value, count in get_most_frequent_words(text, top_number):
        print(count, value)