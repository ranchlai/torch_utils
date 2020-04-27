import numpy as np
import torch
import tqdm

def random_choice(a):
    if len(a)== 0 or type(a) not in [list,tuple]:
        raise Exception("input a is not a list or tuple or the lenght is 0")
    n = len(a)
    idx = int(torch.randint(0,n,(1,)))
    return a[idx]

def random_int(n):
    if n == 0 or type(n) not in [int]:
        raise Exception('input n is 0 or not int')
    return int(torch.randint(0,n,size=(1,)))
def rand():   
    return float(torch.rand(size=(1,)))
def randn():   
    return float(torch.randn(size=(1,)))
def compute_data_stat(dataloader):
    bar = tqdm.tqdm(total=len(dataloader))
    mu = 0
    std = 0
    for i,data in enumerate(dataloader):
        X = data[0]
        mu = (mu*i+torch.mean(X))/(i+1)
        std = (std*i+torch.std(X))/(i+1)
        bar.set_description_str('mu:{},sigma:{}'.format(mu,std))
        bar.update(1)
    return mu,std
        
def pad_1d(s,n,random=True):
    if len(s) < n:
        while len(s) < n:
            s = np.concatenate([s,s])
        return s[:n]    
    
    if len(s) == n:
        return s
    
    if random:
        idx = random_int(len(s)-n)
    else:
        idx = 0
    return s[idx:idx+n]            
def random_uniform(low=0,high=1.0):
    return rand()*(high-low)+low

def random_binomial(prob):
    return int(rand()<prob)

def random_shuffle(mylist):
    n = len(mylist)
    for i in range(n):
        j = random_int(n)
        #swap i,j
        t = mylist[i]
        mylist[i] = mylist[j]
        mylist[j] = t
    return mylist
        
        
        
    
    
