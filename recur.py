## recursive programming
"""

# 1. fibonacci numbers
import sys

def fib(n:int) -> int:
    if n==0 : 
        return 0
    elif n==1 :
        return 1
    else:
        return fib(n-1) +fib(n-2)

n = int(sys.argv[1])

print(fib(n))

# 실행 :python pibo,py n(숫자)
# input:4   ouput:3

"""
"""

# 2. k-mer generation

import sys

def mer (l1,l2,n):
    if n == 1:
        return l2
    
    ltmp = []
    for s1 in l1:   # [A,G,T,C]
        for s2 in l2:   # [A,G,T,C]
            ltmp.append(s1+s2)  #[AA,AG,AT...]
    
    return mer(l1,ltmp, n-1)

l1 = ["A","G","T","C"]
l2 = ["A","G","T","C"]
n = int(sys.argv[1])

print(mer(l1, l2, n))   

# 실행 :python recur.py n(k-mer 수)
# input : 3
# output :['AAA', 'AAG', 'AAT', 'AAC', 'AGA', 'AGG', 'AGT', 'AGC', 'ATA', 'ATG', 'ATT', 'ATC', 'ACA', 'ACG', 'ACT', 'ACC', 'GAA', 'GAG', 'GAT', 'GAC', 'GGA', 'GGG', 'GGT', 'GGC', 'GTA', 'GTG', 'GTT', 'GTC', 'GCA', 'GCG', 'GCT', 'GCC', 'TAA', 'TAG', 'TAT', 'TAC', 'TGA', 'TGG', 'TGT', 'TGC', 'TTA', 'TTG', 'TTT', 'TTC', 'TCA', 'TCG', 'TCT', 'TCC', 'CAA', 'CAG', 'CAT', 'CAC', 'CGA', 'CGG', 'CGT', 'CGC', 'CTA', 'CTG', 'CTT', 'CTC', 'CCA', 'CCG', 'CCT', 'CCC']

"""





