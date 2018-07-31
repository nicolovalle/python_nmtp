#! /usr/bin/env python3

"""
   MAIN.py

   Usage: ./MAIN.py -L Size... -i FirstBeta -f FinalBeta -S Step -t NTHERMA -N NMC [-D InDir] [-T Method] [-B Nboot] [--old] [--nobeta]

   Options:

      -h --help          This help
      -L Size            Lattice Size (can be repeated)
      -i FirstBeta       First beta value
      -f FinalBeta       Sup of beta values
      -S Step            Delta Beta
      -t NTHERMA         As in Data.py
      -N NMC             As in Data.py
      -D InDir           Directory with data [default: data/]
      -T Method          boot/jack/jackran [default: boot]
      -B Nboot           Bootstrap sample dimension [default: 1000]
      --old              Use old conventions for file text name
      --nobeta           w/o interception
"""

import FranciProva
import get_val
import numpy as np
import matplotlib.pyplot as plt
import docopt

argv = docopt.docopt(__doc__,version="1.0")

Size=[L_ for L_ in argv["-L"]]
NTHERMA = int(argv["-t"])
NMC = int(argv["-N"])
InDir= argv["-D"]
Method=argv["-T"]
Nboot=int(argv["-B"])
oldc=bool(argv["--old"])
wantint=not bool(argv["--nobeta"])

mol=(float(argv["-f"])-float(argv["-i"]))/float(argv["-S"])
xt=[float(argv["-i"])+ k*float(argv["-S"])  for k in range(int(mol)+10)]
x=[B for B in xt if B<=float(argv["-f"])]
X=[int(B*1000+0.5) for B in xt if B<=float(argv["-f"])]

if (Method=='boot'):
    corr_fac=1
else:
    corr_fac=np.sqrt(NMC-1.)



if oldc:
    for i in range(len(X)):
        if X[i]%10==0:
            X[i]/=10
            X[i]=int(X[i])



# Nboot non ha senso se si sceglie il jacknife. Ma il controllo viene già fatto
# in bootstrap_jacknif perciò il valore settato qui è ininfluente

#y=np.zeros((len(Size),len(X)))
#E=np.zeros((len(Size),len(X)))

Y1=[]
Y2=[]


i,j = 0, 0

for L in Size:
    y=[]
    E=[]
    for B in X:
        print(B," --- ",L)
        if oldc:
            B=str(B)
            B='0.'+B
        C,mb,El = get_val.bootstrap_jacknife(InDir,L,B,NTHERMA,NMC,Method,Nboot,NMC,'from_file',corr_fac,False)
        y.append(C)
        if (i==0):
            Y1.append(C)
        if (i==1):
            Y2.append(C)
        
        E.append(El)
        #y[i][j]=C
        #E[i][j]=El
        j+=1
        
    i+=1
    lab='Lattice '+str(L)+'x'+str(L)
    plt.errorbar(x,y,yerr=E,label=lab)
    print(L,'Errors: ',E)
    




plt.grid()
fplotdir=InDir+'/img.png'

plt.title(r'Critical $\beta$ from Binder Cumulants interception')
if (wantint):
    xc,yc=FranciProva.interpolated_intercept(np.asarray(x),np.asarray(Y1),np.asarray(Y2))
    plt.text(x[1],Y1[1],r'$\beta$=%7.4f'%(xc))
plt.legend(frameon=False, fontsize=10, numpoints=1, loc='lower left')
plt.savefig(fplotdir)
plt.show()    
    
