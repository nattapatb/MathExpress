# -*- coding: utf-8 -*-
from lexicalAnal import *

def gen_mreading(latex, verbosity = 'brief'):
    tokens = []
    try:
        tokens = cleanTokens(lexAnal(latex, verbosity))
    except:
        print('invalid terms')
        return

    return ' '.join(tokens)
