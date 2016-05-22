#!/bin/python
#coding:utf-8
import matplotlib.pyplot as plt;
import random            as rn;
import math;
from gmm           import *;
from visualization import *;
   
def st_normal(u):
    '''标准正态分布'''
    x=abs(u)/math.sqrt(2)
    T=(0.0705230784,0.0422820123,0.0092705272,
       0.0001520143,0.0002765672,0.0000430638)
    E=1-pow((1+sum([a*pow(x,(i+1))
                    for i,a in enumerate(T)])),-16)
    p=0.5-0.5*E if u<0 else 0.5+0.5*E
    
    return(p)
 
def normal(a,sigma,x):
    '''一般正态分布'''
    u=(x-a)/sigma
    return(st_normal(u))

def E_step(y, gmm):
    n = len(y);
    K = len(gmm.pi);
    w = [[0.0 for j in xrange(K)] for i in xrange(n)];
    
    for i in xrange(n):
        sum1 = 0.0;
        for j in xrange(K):
            sum1 += gmm.pi[j] * normal(gmm.u[j], gmm.d[j], y[i]);
#            print j, gmm.pi[j] * normal(gmm.u[j], gmm.d[j], y[i]);
#        print "sum1=",sum1;
#        print ""
        for j in xrange(K):
            w[i][j]  = gmm.pi[j] * normal(gmm.u[j],gmm.d[j], y[i]);
            w[i][j] /= sum1;
    return w; 
    
    
def M_step(y, gmm, w):
    n = len(y);
    K = len(gmm.pi);
    N_k = [0.0 for i in xrange(K)];
    N   = 0.0;
    for j in xrange(K):
        for i in xrange(n):
            N_k[j] += w[i][j];
        N += N_k[j];

    for j in xrange(K):
        gmm.pi[j] = N_k[j] / N;
        gmm.u[j]  = 0.0;
        gmm.d[j]  = 0.0;
        for i in xrange(n):
            gmm.u[j] += w[i][j] * y[i];
            gmm.d[j] += w[i][j] * math.pow(y[i] - gmm.u[j],2)
        gmm.u[j] /= N_k[j];
        gmm.d[j] /= N_k[j];
        gmm.d[j]  = math.sqrt(gmm.d[j]);

    return gmm;


    
def GMM_EM(y,k, n_iters):
    gmm = GMM(k);
    l   = [];

    for i in xrange(n_iters):
        w     = E_step(y, gmm); 
        gmm = M_step(y, gmm, w);
        l.append(loglikelihood(y,gmm));
        
        if (i+1)%100 == 0:
            print "complete the %d iterations"%(i+1);

    return gmm,l;    

def loglikelihood(y, gmm):
    n = len(y);
    K = len(gmm.pi);
    likelihood = 0.0;
    for i in xrange(n):
        max1 = -100000000;
        for j in xrange(K):
            log = gmm.pi[j] * normal(gmm.u[j],gmm.d[j],y[i]);
            if max1 < log:
                max1 = log;
        likelihood += math.log(max1);
    return likelihood;
        

if __name__ == "__main__":
    gmm1   = GMM(4);
    y      = gmm1.generate_samples(1000);
    
    gmm2,l = GMM_EM(y, k = 5, n_iters = 500);
    gmm2.output();
    
    plt.figure(figsize=(12,6));
    plt.plot(l,label="loglikelihood");
    plt.legend()
    plt.show();
