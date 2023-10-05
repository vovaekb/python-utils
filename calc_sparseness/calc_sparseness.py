#!/usr/bin/python
# Filename: calc_sparseness.py

import sys, getopt


class SparsenessCalculator():
    """Class for calculating sparseness"""
    def __init__(self, file_path):
        """Constructor for SparsenessCalculator"""
        self.file_path = file_path
        self.data = ''

    def read_data(self,):
        """read data from file"""
        print('read_data: %s' % self.file_path)

        with open(self.file_path, 'r') as f:
            self.data = f.readline()

    def calculate(self,):
        """calculate sparseness"""
        self.read_data()
        values = [float(v) for v in self.data.split(' ') if len(v)]
        data_len = len(values)

        zero_vals = [v for v in values if v == 0]
        zeros = len(zero_vals)

        print('zeros ', zeros, ' in total ', data_len, '\n')


def calc_sparseness(argv):
    print(argv)
    data_file = ''
    try:
        opts, args = getopt.getopt(argv,"f:")
    except getopt.GetoptError:
        print('python calc_sparseness.py -f <data_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-f':
            data_file = arg
    
    print('data file:', data_file,'\n')
    calculator = SparsenessCalculator(data_file)
    calculator.calculate()


if __name__ == "__main__":
    calc_sparseness(sys.argv[1:])
