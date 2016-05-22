#!/bin/python

import random as rn;



class GMM:
    def __init__(self, k):
        rn.seed(0);
        sum1    = 0.0;
        self.pi = [0.0 for i in xrange(k)];
        for i in xrange(k):
            self.pi[i] = (i+1.0) + (k+1.0) / 2;
            sum1 += self.pi[i];
        for i in xrange(k):
            self.pi[i] /= sum1;        

        self.u  = [(rn.random() * 2 -1) for i in xrange(k)];
        self.d  = [rn.random() for i in xrange(k)];
    
    def output(self):
        print "pi:",self.pi;
        print "u:",self.u;
        print "d:",self.d;
        print ""

    def generate_samples(self, n):
        y = [];

        for ins in xrange(n):
        
            r = rn.random();
            x = len(self.pi) - 1;
            sum1 = 0.0; 
            for i in xrange(len(self.pi)):
                sum1 += self.pi[i]
                if sum1 >= r:   
                    x = i;
                    break;
                       
            y.append(rn.gauss(self.u[i], self.d[i]));   
        return y;         

    
