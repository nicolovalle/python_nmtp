#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment

X=[]
S=[]
c05=0
c1=0
c2=0
c3=0
quantile=[]
Teo={'gaus':0., 'unif':(-6./5), 'uniuni':(-6./7)}

############# settings ####################
NN=1    #repeat the program NN times --> get NN bootstram distributions
Nboot=1000000   #bootstrap sample dimension (on 1000 data points)
datapoints=500
distr='uniuni'
###########################################

teo=Teo[distr]
namefig='images/'+str(NN)+'volte_'+str(Nboot)+'bootstrap_su'+str(datapoints)+'dati_'+distr+'.png'

def get_vector(s,n):
    if (s=='gaus'):
        return np.random.normal(0,1,n)
    if (s=='unif'):
        return np.random.random(n)
    if (s=='uniuni'):
        return np.power(np.random.random(n),2)
        



def bootstrap(Nboot_,datapoints_,distr_,want_vector):
    VV=get_vector(distr_,datapoints_)
    v=[]
    for k in range(Nboot_):
        if (k%1000==0):
            print((Nboot_-k)/1000)
        indici=np.random.randint(datapoints_,size=datapoints_)
        boots=[VV[z] for z in indici]
        curt=(moment(boots,4)/moment(boots,2)**2)-3

        v.append(curt)

    if (want_vector):
        return v, np.mean(v), np.std(v)
    else:
        return np.mean(v), np.std(v)
    
   

for j in range(NN):
    print("----->j=",j)

    
    #### plotting gaussian only if j=0
    if (j==0):
        v,x,s=bootstrap(Nboot,datapoints,distr,True)
        nbin=int(np.sqrt(Nboot))
        if (NN>9):
            plt.subplot(2,1,1)
        plttitle='Bootstrap distribution '+str(NN)+' '+str(Nboot)+' '+str(datapoints)+' '+distr
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
        plt.text(teo-3.*s,1./(s*np.sqrt(2*np.pi)),textt)
    else:
        x,s=bootstrap(Nboot,datapoints,distr,False)
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
    summary='Teorico: %7.4f \nSingolo esperimento: %7.4f +/- %7.4f \nMedia delle medie Bootstrap: %7.4f \nRMS delle medie Bootstrap: %7.4f \nMedia delle varianze bootstrap: %7.4f \nRMS delle varianze Bootstrap: %7.4f'%(teo,X[0],S[0],np.mean(X),np.std(X),np.mean(S),np.std(S))
    plt.text(1.5,0.25,summary)   
    plt.hist(quantile,int(np.sqrt(NN)),normed=True,color='g')
    xq=[k/100. for k in range(400)]
    yq=[2/(np.sqrt(2*np.pi))*np.exp(-(QQ)**2/2) for QQ in xq]
    plt.plot(xq,yq,linewidth=2,color='b')

plt.savefig(namefig)
plt.show()
