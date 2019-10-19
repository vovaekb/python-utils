## calc_sparseness
### Description
Utility for calculating sparseness of a vector of data (number of zeros). This utility can be useful in scientific work for experimental data analysis.

### Usage 
Create a file with numbers like this
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.11 6163 0 0 0 0 0.109525 0 0 0
```

To calculate the sparseness of a data vector in the file run the script calc_sparseness.py:
```
python calc_sparseness.py -f \<data_file>
```

Output of script:
```
data file: data.txt

zeros  55  in total  58
```
