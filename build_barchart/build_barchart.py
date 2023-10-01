
#!/usr/bin/python
# Filename: build_barchart.py

import os
import sys, getopt
import numpy as np
import matplotlib.pyplot as plt

y_lim = 20 #
x_label = ""
y_label = ""

def build_chart(file_name, x_label, y_label, y_lim=20):
    '''
    Build chart using data from file
    :param file_name:
    :param x_label:
    :param y_label:
    :param y_lim: the number of data items
    :return:
    '''
    values = []
    for line in open(file_name, 'r'):
        if line != '':
            value_strs = line.split(':')
            value = int(value_strs[1])
            values.append(value)

    N = len(values)
    x = range(N)
    width = 1
    
    plt.bar(x, values, width, color="blue")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.ylim(0,y_lim)
    barchart_file = file_name+'.png'
    plt.savefig(barchart_file)
    print('Barchart was saved in file ',barchart_file)

def main(argv):
    file_name = ""
    try:
        opts, args = getopt.getopt(argv,"h:f:m:x:y:")
    except getopt.GetoptError:
        print('Unknown arguments!\nUsing: python build_histogram.py -f <file> -m <y_max> -x <x_label> -y <y_label>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Using: python build_histogram.py -f <file> -m <y_max> -x <x_label> -y <y_label>')
            sys.exit()
        elif opt == '-f':
            file_name = arg
        elif opt == '-m':
            y_lim = int(arg)
        elif opt == '-x':
            x_label = arg
        elif opt == '-y':
            y_label = arg

    build_chart(file_name, x_label, y_label, y_lim)


if __name__ == '__main__':
    main(sys.argv[1:])
