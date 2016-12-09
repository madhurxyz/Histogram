import time
import sys

def remove_punctuation(word_string):
    punctuations = '!()-[]{};:"\,<>./?@#$%^&*_~\x80\x98\x99\x94'
    no_punctuation = word_string
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
    print words_list




if __name__ == '__main__':
    my_app()
