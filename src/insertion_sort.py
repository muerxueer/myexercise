#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:   19:58
# @Autor: LILIYING
# @Site: 
# @File: insertion_sort.py 
# @Software:PyCharm
from tqdm import tqdm,trange
import ipdb
import random

def insertion_sort(A):
    len_A = len(A)
    B = []
    for i in tqdm(range(1,len(A)),desc='1st loop'):
        for j in trange(i,0,-1,desc='2nd loop',leave=False):
            if A[j]<A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
    return A
def insertion_sort2(A):
    for i in range(1,len(A)):
        for j in range(i-1,-1,-1):
            if A[j] > A[i]:
                A[j+1] = A[j]
            else:
                break
        A[j]=A[i]
    return(A)

if __name__ == '__main__':
    A = []

    for i in range(0, 1000):
        num = random.randint(0, 1000)
        A.append(num)
    B = insertion_sort(A)
    C = insertion_sort2(A)
    print(B)
    print(C)