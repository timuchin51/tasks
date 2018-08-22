#!/usr/bin/env python3

import re
import operator
from sys import argv


def most_common_words(argv):
    file_name = argv[1]
    if len(argv) < 3:
        number_of_words = 1
    else:
        number_of_words = int(argv[2])
    with open(file_name, 'r') as text_file:
        text = re.findall('(?i)[a-z\'?a-z]+', text_file.read())

    words = set(text)
    counted_words = [(key, text.count(key)) for key in words]
    sorted_words = sorted(counted_words, key=operator.itemgetter(1))
    output = sorted_words[-int(number_of_words):]
    for i in output:
        print('the word "{0}" in the text occurs {1} times'.format((i[0]), i[1]))


if __name__ == '__main__':
    try:
        most_common_words(argv)
    except IndexError:
        print('We need more gold, master')
    except FileNotFoundError:
        print('File not found or wrong path. Try again')
    except ValueError:
        print('The second argument must be a number')
