import argparse
from config import conf

#Parsing arguments from CLI: algorithm and file with marks
def pars_arguments():
    parser = argparse.ArgumentParser(description ='Marking Evolution', 
                                     version = '0.0.1')
    parser.add_argument ('-algorithm', choices = ('1','2','3'), 
                         help = "Choose your destiny (or algorithm): 1, 2, 3")
    parser.add_argument ('-file', 
                         help = "Name of the file with marks")
    results = parser.parse_args()
    conf['algorithm'] = results.algorithm
    conf['file'] = results.file
    print results
    return conf