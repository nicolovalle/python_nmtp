import numpy as np
from scipy.stats import moment

############### returns random sample ###############
def get_vector_random(s,n):
    if (s=='gaus'):
        return np.random.normal(0,1,n)
    if (s=='unif'):
        return np.random.random(n)
    if (s=='uniuni'):
        return np.power(np.random.random(n),2)
    if (s=='dice'):
        return np.random.randint(6,size=n)
    if (s=='coin3070'):
        return np.random.binomial(1,0.3,size=n)
####################################################


#############  read sample from file ##################
def get_vector_file(filename):
    VectorRet=np.loadtxt(filename)
    Datap=len(VectorRet)
    return VectorRet, Datap
#######################################################


############ Compute quantity to plot #################
def curtosi(V,m='from_file'):
    if (m=='from_file'):
        M4=np.mean(np.power(V,4))
        M2=np.mean(np.power(V,2))
        return 1.-M4/(3.*M2*M2)
    else:
        return (moment(V,4)/moment(V,2)**2)-3

######################################################
   





############## Use Jacnkie or Bootstrap on the sample ###########################à

def bootstrap_jacknife(the_dir,size,beta,th,nmc,T, Nboot, datapoints, distr, corr_fac,want_vector):

    if (distr=='from_file'):
        filename="%sMag_%s_%s_%s_%s.dat"%(the_dir,str(size),str(beta),str(th),str(nmc))
    VV=[]
    if (distr=='from_file'):
        VV, number_of_points = get_vector_file(filename)

        ######### a little check ########################
        if not number_of_points==datapoints:
            print("Please, set the number of points properly")
            exit()
        ##################################################
    else:
        VV = get_vector_random(distr,datapoints)

    v=[]

    if (Nboot==0):
        v.append(curtosi(VV,'central'))
    
    if (T=="jack") or (T=="jackran"):
        Nboot=datapoints
       
        

    for k in range(Nboot):
        if (k%1000==0):
            print((Nboot-k)/1000)

        if (T=="boot"):
            indici=np.random.randint(datapoints,size=datapoints)
            boots=[VV[z] for z in indici]

        elif (T=="jack"):
            boots=np.delete(VV,k)

        elif (T=="jackran"):
            boots = np.delete(VV,np.random.randint(datapoints))

        curt= curtosi(boots,distr)

        v.append(curt)

    if (want_vector):
        return v, curtosi(VV,distr), np.mean(v), np.std(v)*corr_fac
    else:
        return curtosi(VV,distr), np.mean(v), np.std(v)*corr_fac
 
