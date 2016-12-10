import time
import sys

def create_histogram(words_list):
    histogram = {}
    for word in words_list:
        if word in histogram:
            count = histogram[word]
            histogram[word] = count + 1
        else:
            histogram[word] = 1
    return histogram


def remove_punctuation(word_string):
    punctuations = '!()-[]{};:"\,<>./?@#$%^&*_~\x80\x98\x99\x94'
    no_punctuation = ''
    for character in word_string:
        if character not in punctuations:
            no_punctuation += character
    return no_punctuation

def get_words_list(file_name):
  f= open(file_name)
  lines = f.readlines()
  word_string = ' '.join(lines)
  no_punctuation = remove_punctuation(word_string)
  words_list = no_punctuation.split()
  return words_list

def my_app():
    words_list = get_words_list('holmes.txt')
    histogram = create_histogram(words_list)
    print histogram




if __name__ == '__main__':
    my_app()
