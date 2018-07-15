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

NN=30    #repeat the program NN times --> get NN bootstram distributions

Nboot=5000   #bootstrap sample dimensin (on 1000 data points)
datapoints=500




#teo=-6./5 #uniforme
teo=-6./7 #uniforme**2

for j in range(NN):
    print("----->j=",j)

    V_V=np.random.random(datapoints)
    VV=[v_v**2 for v_v in V_V]
    
       
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
        if (NN>9):
            plt.subplot(2,1,1)
        plt.title('Bootstrap distribution')
        plt.hist(v,nbin,normed=True)
        minbin=x-4*s
        maxbin=x+4*s
        bins=[minbin+(maxbin-minbin)*ii/nbin for ii in range(nbin)]
        plt.plot(bins,1/(s*np.sqrt(2*np.pi))*np.exp(-(bins-x)**2/(2*s**2)),linewidth=2,color='r')
        fx, fy = [teo,teo], [0,4]
        plt.plot(fx,fy,color='g')
        textt=str(x)+"$\pm$"+str(s)
        plt.text(-1.2,.025,textt)
    #######################
    X.append(x)
    S.append(s)
    quant=abs(x-teo)/s
    quantile.append(quant)
    c05+=(quant<0.5); c1+=(quant<1);
    c2+=(quant<2); c3+=(quant<3)
    
    print("In s/2: ",100.*c05/(j+1),"%\nIn s: ",100.*c1/(j+1),"%\nIn 2s:",100.*c2/(j+1),"%\nIn 3s:",100.*c3/(j+1),"%")

## X è il vettore delle medie di Bootstrap
## S è il vettore degli errori di Bootstrap
print("\n")
print("Teorico:",teo)
print("Singolo esperimento:",X[0]," pm ",S[0])
print("Media delle medie Bootstrap:",np.mean(X))
print("RMS delle medie Bootstrap:",np.std(X))
print("Media delle varianze Bootstrap:",np.mean(S))
print("RMS delle varianze Bootstrap:",np.std(S))


#####plotting quantiles
if (NN>9):
    plt.subplot(2,1,2)
    plt.title('Quantiles vs Standard Gaussian')
    plt.hist(quantile,int(np.sqrt(NN)),normed=True)
    xq=[k/100. for k in range(400)]
    yq=[2/(np.sqrt(2*np.pi))*np.exp(-(QQ)**2/2) for QQ in xq]
    plt.plot(xq,yq,linewidth=2,color='b')


plt.show()
