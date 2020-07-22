#! /usr/bin/env/python
"""
import sys
import gzip     # gzip으로 된 binary 파일을 열기 위해 import

if len(sys.argv) != 2:
    print(f"#usage ; python {sys.argv[0]}[fasta.gz]")
    sys.exit()

f= sys.argv[1]
d = {}

with gzip.open(f, 'rb') as handle:   # 'rb':read binary
    for line in handle:
        line = line.decode("utf-8").strip()        
        #sys.exit()                              # 너무 많아서 한줄만 보려고
        if line.startswith(">"):
            continue
        for s in line :
            if s in d:
                d[s] += 1
            else:
                d[s] = 1

print(d)                #dictionary 확인
# {'A': 8954, 'T': 9594, 'G': 5863, 'C': 5492}

total = 0
for k,v in d.items():   #items ; k와 v를 tuple 쌍()을 요소로 list 형태로 보여줌
    total += v
print(total)            #29903  #total base pair확인

with open("result1.txt",'w') as handle:     #각 basepair 수 확인 및 결과저장    
    handle.write(f"A: {d['A']}\n")          #d 의 key값을 통해 value 출력
    handle.write(f"T: {d['T']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"C: {d['C']}\n")


# 실행 : python 0721.py covid19.fastq.gz

"""
"""

Seq1 = "ATGTTATAG"

for i in range(0,len(Seq1),3):
    print(i)        # 0, 3, 6
    print(i, Seq1[i])   #인덱싱 0 A, 3 T, 6 T

"""
"""
Seq1 = "ATGTTATAG"

for i in range(0,len(Seq1),3):
#    print(i)
#    print(i, Seq1[i])
    print(i, i+3, Seq1[i:i+3])

# 0 3 ATG
# 3 6 TTA
# 6 9 TAG

"""
"""
Seq1 = "ATGTTATAG"

print(Seq1)         #ATGTTATAG
print(Seq1[::-1])   #GATATTGTA

"""
"""
import sys

# solution 1
def comp1(seq:str)  -> str : 
# input:str -> output:str 임을 표시해준거. 없어도됨
    comp = ""   #str으로 받겠다(초기화)
    for s in seq:
        if s == "A":
            comp += "T"
        elif s == "C":
            comp += "G"
        elif s == "T":
            comp += "A"
        elif s == "G":
            comp += "C"
    return comp

# solution 2
def comp2(seq:str) -> str:
    d_comp = {"A":"T","T":"A","G":"C","C":"G"}
    comp = ""
    for s in seq:
        comp += d_comp[s]
    return comp

if __name__ == "__main__":  
# import할때 나오게 하는 부분 
# if __name__=="__main__"이라는 조건문을 넣어주고 그 아래는 직접 실행시켰을 때만 
# 실행되길 원하는 코드들을 넣어줌

    if len(sys.argv) != 2:  #오류 경고문
        print(f"#usage: python {sys,argv[0]} [string]")
        sys.exit()

    seq = sys.argv[1]   # seq = ATGTTATAG
    c1 = comp1(seq) 
    c2 = comp2(seq)
    print(seq)      # ATGTTATAG
    print(c1)       # TACAATATC
    print(c2)       # TACAATATC

# 실행 : python 0721.py ATGTTATAG
"""
"""
import sys

Seq1 = sys.argv[1]  # AGTTTATAG

for i in range(0,len(Seq1),1):
    if Seq1[i:i+2] == "TT":
        print(i,i+2,Seq1[i:i+2])

# 2 4 TT
# 3 5 TT 
 
# 실행 : python 0721.py AGTTTATAG
"""
"""
l=[3,1,1,2,0,0,2,3,3]

max_val = l[0]
min_val = l[0]

for elem in l:
    if elem > max_val:
        max_val = elem
    if elem < min_val:
        min_val = elem

print(f"max: {max_val}")    # max: 3
print(f"min: {min_val}")    # min: 0

#max_val = max(l)
#min_val = min(l)
"""
"""
l= [3,1,1,2,0,0,2,3,3]

d = {}

for elem in l:
    if elem in d:
        d[elem] += 1
    else : 
        d[elem] = 1
print(d)    #{3: 3, 1: 2, 2: 2, 0: 2} 
"""
"""
with open(read_sample, 'r') as handle:
    for line in handle:
        if line.startswith(">")
            continue
        for s in line.strip():
            print(f.

"""


