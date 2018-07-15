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

Nboot=5000   #bootstram sample dimensin (on 1000 data points)

datapoints=500

teo=-6./5

for j in range(NN):
    print("----->j=",j)

    VV=np.random.random(datapoints)
    
    
       
    v = []
    
    for k in range(Nboot):
        if (k%1000==0):
            print((Nboot-k)/1000)
        
        indici=np.random.randint(datapoints,size=datapoints)
       
        #print(s)


        boots=[VV[z] for z in indici]
        

        curt=(moment(boots,4)/moment(boots,2)**2)-3
        #print(curt)
        

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
        fx, fy = [teo,teo], [0,10]
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
    print("In s/2: ",100.*c05/(j+1),"%\nIn s: ",100.*c1/(j+1),"%\nIn 2s:",100.*c2/(j+1),"%\nIn 3s:",100.*c3/(j+1),"%")

#plt.hist(x,30)

print(np.mean(X))
print(np.std(X))
print(np.mean(S))
print("\n\n")
print("In s/2: ",c05,"\nIn s: ",c1,"\nIn 2s:",c2,"\nIn 3s:",c3)
plt.show()
