import torch
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
