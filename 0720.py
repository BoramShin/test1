#! /usr/bin/env python



import sys
# len이 2가 되도록 설정해놨는데 아닐경우 오류 메세지 출력
if len(sys.argv) != 2:
    print(f"#usage:python {sys.argv[0]} [fasta]")
    sys.exit()

f = sys.argv[1]     # hello.py covid19.fasta
d = {}

with open(f,'r') as handle:   #'r'권한으로 불러오기
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip():      # ACGTACGTAAA
            if s in d:
                d[s] += 1
            else:
                d[s] = 1

print(d)  # {'A': 8954, 'T': 9594, 'G': 5863, 'C': 5492}#dictionary 형태로 출력

total = 0
for k,v in d.items():  # dict_items([('A', 8954), ('T', 9594), ('G', 5863), ('C', 5492)])# dictionary의 key(k)와 values(v) 쌍을 tuple로 보여줌
    total += v           # total base 갯수

print(total)    # 29903 bp

with open("result.txt",'w') as handle:  #'w'권한으로 new file
    handle.write(f"A: {d['A']}\n")   # A: 8954
    handle.write(f"C: {d['C']}\n")   # C: 5492
    handle.write(f"G: {d['G']}\n")   # G: 5863
    handle.write(f"T: {d['T']}\n")   # T: 9594


