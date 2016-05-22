#!/bin/python
import matplotlib.pyplot as plt;
from gmm import *;

def visualization_data(gmm):
    y   = gmm.generate_samples(10000);

    d          = dict();
    total_step = 2000;
    x1         = range(0,total_step);
    x1[0]      = -10;
    for i in xrange(1,len(x1)):
        x1[i]    = x1[i-1] + (abs(x1[0]) - x1[0]) / 1.0 / total_step;
        d[int(x1[i] * 100 + 10000)] = i;

    y1  = [ 0.0 for i in xrange(len(x1))];
    for i in xrange(len(y)):
        f  = y[i];
        f  = int(f * 100+ 10000);
        if f in d:
            y1[d[f]] += 1.0;

    for i in xrange(len(y1)):
        y1[i] /= len(y);


    return x1, y1;

if __name__ == "__main__":
    gmm    = GMM(4);

    gmm.output();    
    x1, y1 = visualization_data(gmm);

    plt.figure(figsize=(12,6))
    plt.plot(x1, y1);        
    plt.legend()
    plt.show();
