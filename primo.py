import math as mt
import sys

def eprimo(N):
     
    n=mt.floor(mt.sqrt(N))+1
    tag = 0
    for i in  range (2,n):
        if (N%i==0):
            return False
    return True
    

def nesimo(n):
    i=1
    count=1
    if (n==1 or n==2):
        return n
       
    while count <= n:
        if eprimo(i):
            count+=1
        i+=2
    return i-2



for i in range (1,1000000):
    print(i,") ",nesimo(i),"\n")



