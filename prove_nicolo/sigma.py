import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment

X=[]
S=[]
c05=0
c1=0
c2=0
c3=0

NN=1000    #repeat the program NN times --> get NN bootstram distributions

Nboot=40   #bootstram sample dimensin (on 1000 data points)

datapoints=100



teo=1  #theoretical result


for j in range(NN):
    print("----->j=",j)

    VV=np.random.normal(0,1,datapoints)
           
    v = []
    
    for k in range(Nboot):
        if (k%1000==0):
            print((Nboot-k)/1000)
        
        indici=np.random.randint(datapoints,size=datapoints)
       
        


        boots=[VV[z] for z in indici]

        #curt=(moment(boots,4)/moment(boots,2)**2)-3
        curt=moment(boots,2)


        v.append(curt)

        
    
        
    x=np.mean(v)
    s=np.std(v)
    #### plotting gaussian
    if (j==0):
        nbin=int(np.sqrt(Nboot))
        plt.hist(v,nbin,normed=True)
        minbin=x-4*s
        maxbin=x+4*s
        bins=[minbin+(maxbin-minbin)*ii/nbin for ii in range(nbin)]
        plt.plot(bins,1/(s*np.sqrt(2*np.pi))*np.exp(-(bins-x)**2/(2*s**2)),linewidth=2,color='r')
        fx , fy = [teo,teo],[0,4]
        plt.plot(fx,fy,color='g')
    X.append(x)
    S.append(s)
    if (abs(x-teo)<0.5*s):
        c05+=1
    if (abs(x-teo)<s):
        c1+=1
    if (abs(x-teo)<2.*s):
        c2+=1
    if (abs(x-teo)<3.*s):
        c3+=1

#plt.hist(x,30)

print("Media dei",NN,"esperimenti:",np.mean(X))
print("RMS dei",NN,"esperimenti:",np.std(X))
print("\n")
print("Media delle varianze dei",NN,"esperimenti:",np.mean(S))
print("RMS delle varianze dei",NN,"esperimenti:",np.std(S))
print("\n\n")
print("In s/2: ",c05,"\nIn s: ",c1,"\nIn 2s:",c2,"\nIn 3s:",c3)
plt.show()