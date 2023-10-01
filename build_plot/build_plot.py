#!/usr/bin/python
# Filename: build_plot.py
#
# Utility for building plot from data stored in file
# Usage: python build_plot.py -f <data_file>
#
# Data format in file
#
# x_axis_data: 0.5, 0.25, 0.31
# y_axis_data: 100, 200, 500
# Axis: 0, 1.05, 0, 500   ## y_min, y_max, x_min, x_max


import sys, getopt
import numpy as np
from matplotlib import pyplot as plt

def read_data(file):
    x_values = []
    y_values = []
    x_label = ''
    y_label = ''
    plot_axis = []
    line_n = 0
    for line in open(file, 'r'):
        if line != '':
            strs = line.split(':')
            if strs[0] != "Axis":
                axis_label = strs[0]
                values_str = strs[1]
                #values_arr = values_str.split(',')
                values = [float(v) for v in values_str.split(',')]
                print('%s values count: %s\n',(axis_label, len(values)))
                print(values)
                print('\n')
                
                if line_n == 0:
                    x_values = values
                    x_label = axis_label
                else:
                    y_values = values
                    y_label = axis_label

                line_n = line_n + 1

            else:
                limits_str = strs[1]
                plot_axis = [float(v) for v in limits_str.split(',')]

    plt.plot(x_values, y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.axis(plot_axis)
    plt.savefig(file+'.png')
    
    print('%s plot was successfully built\n' % file)


def main(argv):
    print('start script build_plot.py\n')
    data_file = ''
    try:
        opts, args = getopt.getopt(argv,"f:")
    except getopt.GetoptError:
        print('build_plot.py -f <data_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-f':
            data_file = arg

    print('data_file: %s\n', data_file)
    read_data(data_file)

'''
    x_values = [ 50, 100, 200, 400, 1000, 2000, 5000 ]
    y_values = [ 0.286, 0.286, 0.308, 0.308, 0.333, 0.125, 0.307 ]
    x_axis = "Vocabulary size"
    y_axis = "Precision"
    plot_name = "size_precision"

    plt.plot(x_values, y_values)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.axis([0, 5500, -0.5, 1.05])
    plt.savefig(plot_name+'.png')

    print(plot_name,' plot was successfully built\n')
'''

if __name__ == "__main__":
    main(sys.argv[1:])
