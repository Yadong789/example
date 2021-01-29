# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:43:11 2021

@author: 13yd
"""

# following are for question 7
#########################################################
# A = []
# for i in range(1, 1001):
#     f = []
#     for j in range(1, i):
#         if i%j == 0:
#             f.append(j)
#     if sum(f) == i:
#         A.append(i)
# print(A)

# for i in range(1, 1001):
#    s = 0   # pay attention to the position 
#    for j in range(1, i):
#        if i%j == 0:
#             s += j
#    if s == i:
#        print("\n", i, " ", end = "")
#        print("its factors are ", end = "")
#        for j in range(1, i):
#           if i%j == 0:
#               print(j, end = " ")



# following are solution for question 8
A = [] # get all prime values from 4 to 2000
A.append(2) 
for i in range(3, 2001):
    j = 2
    while j < i:
        if i % j == 0:
            # print(i, ' is not a prime number')
            break
        j += 1
    else:
        A.append(i)
B = []
for k in range(4, 2001):
    for a in A:
        if (k - a) in A:
            B.append(k)
            break
    else: 
        print('Goldbach conjecture is wrong')
print('the prime numbers are:', A)
print('the numbers can be decomposed are', B)

            
        