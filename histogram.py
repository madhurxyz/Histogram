import time
import sys

def get_words_list(file_name):
  f= open(file_name)
  lines = f.readlines()
  word_string = ' '.join(lines)
  return word_string

def my_app():
    words_list = get_words_list('holmes.txt')
    print words_list




if __name__ == '__main__':
    my_app()
