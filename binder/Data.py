#!/usr/bin/env python3

"""
   Data.py 

   Usage: ./Data.py -L L... [-i Inf] [-S STEP] [-Q Nsteps] [-t THERMA] [-n NMC] [-s START] [-D OutDir]

   Options:

       -h --help             Display this help
       -L L                  Lattice size (option can be repeated)
       -i Inf                Estreni inferiore Beta [default: 0.42]
       -S STEP               DeltaBeta [default: 0.005]
       -Q Nsteps             Numero Step [default: 12]
       -t THERMA             THERMA [DEFAULT: 1000]
       -n NMC                SWEEPS [DEFAULT: 1000]
       -s START              START [DEFAULT: c]
       -D OutDir             Output Directory [DEFAULT: data/]

"""


import docopt
import numpy as np
from pprint import pformat
from matplotlib import pyplot as plt
from ising import Ising
from kurt import bootstrap_jacknife
import os




argv = docopt.docopt(__doc__,version="1.0")
L = [int(L_) for L_ in argv["-L"]]
bi = float(argv["-i"])
STEP=float(argv["-S"])
Nsteps=int(argv["-Q"])
beta=[bi+k*STEP for k in range(Nsteps)]
THERMA = int(argv["-t"])
NMC = int(argv["-n"])
START = argv["-s"]
OutDir= argv["-D"]

if not os.path.isdir(OutDir):
    print('Your directory seems not to exist :-( ')
    exit()

if os.listdir(OutDir):
    goon=input('Your directory is not empty! (~_^) Run anyway? (y/n) ')
    if not goon=='y':
        exit()
    


for i in beta:
    for j in L:
        ising = Ising(j,i,THERMA,NMC,START)
        #ising.run(OutDir, i==beta[len(beta)-1] and j==L[len(L)-1] )
        ising.run(OutDir,False)

