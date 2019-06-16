#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:   19:14
# @Autor: LILIYING
# @Site: 
# @File: choose_sort.py 
# @Software:PyCharm

from tqdm import tqdm,trange
import ipdb
import random

def selection_sort(A):
    for i in tqdm(range(0,len(A)-1),desc='1st loop'):
        max_index = i
        for j in trange(i+1,len(A)-1,desc='2nd loop',leave = False):
            if A[max_index] < A[j]:
                max_index = j
        if max_index!=i:
            A[i],A[max_index]= A[max_index],A[i]
    return(A)
if __name__=='__main__':
    A = []
    for i in range(0,1000):
        num = random.randint(0,1000)
        A.append(num)
    B = selection_sort(A)
    print(B)

    