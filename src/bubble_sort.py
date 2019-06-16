#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:   17:45
# @Autor: LILIYING
# @Site: 
# @File: maopao.py 
# @Software:PyCharm

import ipdb
import random
import sys
import numpy
from tqdm import tqdm_notebook,tqdm
from tqdm import tnrange,trange
def bubble_sort(A):
    len_A = len(A)
    for j in tqdm(range(0,len_A-1),desc='1st loop'):
        issort = True
        print(j)
        for i in trange(0,len_A-j-1,desc='2nd loop',leave='False'):
            if A[i]>A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
                issort=False
        if issort:
            break
    return A

if __name__=='__main__':
    A = []
    for i in range(0,1000):
        num = random.randint(0,100)
        A.append(num)
    B = bubble_sort(A)
    print(B)

