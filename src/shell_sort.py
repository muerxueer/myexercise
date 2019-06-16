#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:   21:10
# @Autor: LILIYING
# @Site: 
# @File: shell_sort.py 
# @Software:PyCharm
from tqdm import tqdm,trange
import ipdb
import random

def shell_sort(A):
    len_A = len(A)
    gap = int(len_A/2)

    while gap > 0:
        print(gap)
        for i in range(gap,len_A):
            num = i

            while num >= gap and A[num-gap]>A[num]:
                A[num-gap],A[num] = A[num],A[num-gap]
                num = num - gap
        gap = int(gap/2)
    return A
if __name__=='__main__':
    A = []
    for i in range(0,1000):
        num = random.randint(0,1000)
        A.append(num)
    B = shell_sort(A)
    print(B)
