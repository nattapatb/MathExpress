# -*- coding: utf-8 -*-
from lexicalAnal import *
import sys

def gen_mreading(latex, verbosity = 'brief'):
    tokens = []
    try:
        tokens = cleanTokens(lexAnal(latex, verbosity))
    except:
        print('invalid terms')
        return

    return ' '.join([x[1] for x in tokens])

if __name__ == '__main__':
    filename = sys.argv[1]
    if len(sys.argv) == 2:
        verbosity = 'brief'
    else:
        verbosity = sys.argv[2]

    f = open(filename)
    exp_list = f.readlines()
    f.close()
    for latex_exp in exp_list:
        print(gen_mreading(latex_exp[:-1]))
