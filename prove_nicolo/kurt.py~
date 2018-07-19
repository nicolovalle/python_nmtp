#!/usr/bin/env python3

"""
    kurt_bootstrap.py 

  Usage: ./ising.py [-M <method>] [-I <NN>] [-N <Nboot>] -P <datapoints> [-d <distr>]

  Arguments:

  Options:
    -h --help         Display this help and exit
    -M <method>       Method: boot/jack [default: boot]
    -I <NN>           Repear the experiment NN times [default: 1]
    -N <Nboot>        Bootstrap sample dimension [default: 5000]
    -P <datapoints>   Number of data points
    -d <distr>        Distribution (gaus/unif/uniuni) [default: gaus]
    
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment
import docopt
import progressbar as pbar

X=[]
S=[]
c05=0
c1=0
c2=0
c3=0
quantile=[]
Teo={'gaus':0., 'unif':(-6./5), 'uniuni':(-6./7)}


############# settings ####################
argv = docopt.docopt(__doc__,version="1.0")
NN=int(argv["-I"])    #repeat the program NN times --> get NN bootstram distributions
Nboot=int(argv["-N"])   #bootstrap sample dimension (on 1000 data points)
datapoints=int(argv["-P"])
distr=str(argv["-d"])
method=str(argv["-M"])
###########################################



teo=Teo[distr]
if (method=="boot"):
    namefig='images/'+str(NN)+'volte_'+str(Nboot)+'bootstrap_su'+str(datapoints)+'dati_'+distr+'.png'
    corr_fac=1
    TT='Bootstrap'
elif (method=="jack"):
    namefig='images/'+str(NN)+'volte_'+str(datapoints)+'dati_jacknife'+distr+'.png'
    corr_fac=np.sqrt(datapoints-1)
    Nboot=datapoints
    TT='Jacknife'

def get_vector(s,n):
    if (s=='gaus'):
        return np.random.normal(0,1,n)
    if (s=='unif'):
        return np.random.random(n)
    if (s=='uniuni'):
        return np.power(np.random.random(n),2)
        



def bootstrap_jacknife(T,Nboot_,datapoints_,distr_,want_vector):
    VV=get_vector(distr_,datapoints_)
    v=[]
    for k in range(Nboot_):
        if (k%1000==0):
            print((Nboot_-k)/1000)
            
        if (T=="boot"):
            indici=np.random.randint(datapoints_,size=datapoints_)
            boots=[VV[z] for z in indici]
            
        elif (T=="jack"):
            boots=np.delete(VV,k)
                  
            
        curt=(moment(boots,4)/moment(boots,2)**2)-3
        

        v.append(curt)

    if (want_vector):
        return v, np.mean(v), np.std(v)*corr_fac
    else:
        return np.mean(v), np.std(v)*corr_fac


    
   

for j in range(NN):
    print("----->j=",j)

    
    #### plotting gaussian only if j=0
    if (j==0):
        v,x,s=bootstrap_jacknife(method,Nboot,datapoints,distr,True)
        s=s/corr_fac
        nbin=int(np.sqrt(Nboot))
        if (NN>9):
            plt.subplot(2,1,1)
        plttitle=TT+' distribution '+str(NN)+' '+str(Nboot)+' '+str(datapoints)+' '+distr
        plt.title(plttitle)
        plt.hist(v,nbin,normed=True)
        minbin=x-4*s
        maxbin=x+4*s
        bins=[minbin+(maxbin-minbin)*ii/nbin for ii in range(nbin)]
        plt.plot(bins,1/(s*np.sqrt(2*np.pi))*np.exp(-(bins-x)**2/(2*s**2)),linewidth=2,color='r')
        fx, fy = [teo,teo], [0,1.05/(s*np.sqrt(2*np.pi))]
        plt.plot(fx,fy,color='g')
        textt=str(x)+"$\pm$"+str(s)
        textt='%7.4f'%(x)+' +/- '+'%7.4f'%(s) 
        #plt.text(teo-3.*s,1./(s*np.sqrt(2*np.pi)),textt)
        s=s*corr_fac
    else:
        x,s=bootstrap_jacknife(method,Nboot,datapoints,distr,False)
    X.append(x)
    S.append(s)
    quant=abs(x-teo)/s
    quantile.append(quant)
    c05+=(quant<0.5); c1+=(quant<1);
    c2+=(quant<2); c3+=(quant<3)
    
    print("In s/2: ",100.*c05/(j+1),"%\nIn s: ",100.*c1/(j+1),"%\nIn 2s:",100.*c2/(j+1),"%\nIn 3s:",100.*c3/(j+1),"%")





#####plotting quantiles
if (NN>9):
    plt.subplot(2,1,2)
    #plt.text(1.5,0.7,'Quantiles vs Standard \n Gaussian')
    summary='Teorico: %7.4f \nSingolo esperimento: %7.4f +/- %7.4f \nMedia delle medie %s: %7.4f \nRMS delle medie %s: %7.4f \nMedia delle varianze %s: %7.4f \nRMS delle varianze %s: %7.4f'%(teo,X[0],S[0],TT,np.mean(X),TT,np.std(X),TT,np.mean(S),TT,np.std(S))
    plt.text(1.5,0.25,summary)   
    plt.hist(quantile,int(np.sqrt(NN)),normed=True,color='g')
    xq=[k/100. for k in range(400)]
    yq=[2/(np.sqrt(2*np.pi))*np.exp(-(QQ)**2/2) for QQ in xq]
    plt.plot(xq,yq,linewidth=2,color='b')

plt.savefig(namefig)
plt.show()
