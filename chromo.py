"""
# BED file 구간 길이 합

total = 0

with open("077.bed", 'r') as handle:
    for line in handle:
        splitted = line.strip().split()
        start = int(splitted[1])
        end = int(splitted[2])
        total += end - start

print(total)    # 29681

"""
"""
# VCF file 열 갯수

cnt = 0 
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        cnt += 1

print(cnt)      # 12

"""
"""

# VCF file에서 filter열이 PASS인 열의 개수

cnt = 0
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().slit("\t")
            filt_indx = header.index("FILTER")  #방어적 코딩

        splitted = line.strip().split("\t")
        if splitted[filt_idx] == "PASS":
            cnt += 1

print(cnt)      # 5

"""
"""
# VCF file에서 특정 값(rs값)이 있는 열의 내용 출력

with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().split("\t")
            id_idx = header.index("ID")
            continue
        
        splitted = line.strip().split("\t")
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alt = splitted[4]
        if splitted[id_idx] != ".":
            print(f"{chrom}-{pos}-{ref}-{alt}-{id_}")

# chr21-18269600-T-TGCG-rs12345
# chr21-31713271-C-T-rs12346
# chr21-45763981-C-T-rs212121

"""
"""

# VCF file에서 SNP 갯수세기

cnt = 0
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        
        splitted = line.strip().split("\t")
        alts= splitted[4].split(",")
        for alt in alts : 
            cnt += 1

print(cnt)      # 14
"""
"""
# VCF file에서 SNP, In/Del 갯수세기

import pandas as pd
from matplotlib import pyplot as plt

d= {"snp":0, "ins":0, "del":0}  # 각 값 초기화

with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        
        splitted = line.strip().split("\t")
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alts = splitted[4].split(",")
        for alt in alts:
            if len(ref) == len(alt):    # snp
                d["snp"] += 1
            elif len(ref) > len(alt):   # deletion
                d["del"] += 1
            elif len(ref) < len(alt):   # insertion
                d["ins"] += 1

            else:                       # 방어적 코딩
                raise

print(d)        # {'snp': 10, 'ins': 2, 'del': 2}
df = pd.DataFrame([d])
print(df)
#    snp  ins  del
#0   10    2    2
df.plot.bar()
plt.savefig("v.png")
"""

