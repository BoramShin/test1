#! /usr/bin/env/python
"""
import sys
import jason

def read_txt(file_name: str) -> str:
    ret = ""
    with  open(file_name,'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            ret += line.strip()
    return ret

def read_tsv(file_name: str) -> list:
    ret = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

def to_json(l:list,file_name: str) -> None:
    with open("file_name",'w') as handle:
        json.dump(l,handle,indent=4)

def read_json(file_name: str) -> list:
    with open(file_name, 'r') as handle:
        l=json.load(handle)
    return l

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv[0]}[txt]")
        sys.exit()

    file_name = sys.argv[1]
    #txt =  read_txt(file_name)
    #print(txt)
    #ret = read_csv(file_name)
    ret = read_tsv(file_name)
    #print(ret)
    to_jason(ret,"result.json")
"""
"""
## txt 파일 파이썬으로 읽기

import sys

def read_txt(file_name: str) -> str:       
    ret = ""
    with open(file_name,'r') as handle:
        for line in handle:         
            if line.startswith(">"):    #header 제거
                continue
            ret += line.strip()         # 여러줄 txt를 한줄로 연결
    return ret

if __name__ == "__main__":      #파일 불러오기
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv[0]}[txt]")
        sys.exit()

    file_name = sys.argv[1] # txt file
    ret = read_txt(file_name)
    print(ret)

# 실행 :python readtxt.py read_sample.txt
# CGTACGTAAAATTTAAAGGAAA

"""
"""
## csv 파일 파이썬으로 읽기

import sys

def read_csv(file_name:str) -> list:               #list로 받기
    ret = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):                
                header = line.strip().split(",")    #header split
                continue
            splitted = line.strip().split(",")      #데이터 split
            d = dict(zip(header, splitted))         #header와 데이터를 k와 v로 dict
            ret.append(d)
    return ret                                      #dic을 list로 받기

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv[0}] [csv]")
        sys.exit()
    
    file_name = sys.argv[1]     # csv file
    ret = read_csv(file_name)
    print(ret)

# 실행 :python readtxt.py read_sample.csv
# [{'#id': '1', 'sequencce': 'ACAGGGTTA', 'species': 'Influenza'}, {'#id': '2', 'sequencce': 'TTAACCAAG', 'species': 'Herpes'}, {'#id': '3', 'sequencce': 'GCGAATGAC', 'species': 'Epstein-bar'}]
"""

# tsv 파일 파이썬으로 읽기

import sys

def read_tsv(file_name: str) -> list:
    ret = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usageL python {sys,argv[0]}[tsv]")
        sys.exit()
 
    file_name = sys.argv[1]     # tsv file
    ret = read_tsv(file_name)
    print(ret)

# 실행 :python readtxt.py read_sample.tsv
# [{'#id': '1', ' sequencce': ' ACAGGGTTA', ' species': ' Influenza'}, {'#id': '2', ' sequencce': ' TTAACCAAG', ' species': ' Herpes'}, {'#id': '3', ' sequencce': ' GCGAATGAC', ' species': ' Epstein-barr'}]

# csv, tsv를 list형태로 만든 결과값을 불러와야 가능
# jason파일로 내보내기

# import sys
import json

def to_json(l:list) -> None:
    with open("read_sample.json",'w')as handle:
        json.dump(l, handle, indent = 4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python {sys.argv[0]} [txt]")
        sys.exit()

    file_name = sys.argv[1]
    ret = read_tsv(file_name)       # or = read_csv(file_name)
    to_json(ret)

# 실행 :python readtxt.py read_sample.tsv   (or read_sample.csv)
# [{'#id': '1', ' sequencce': ' ACAGGGTTA', ' species': ' Influenza'}, {'#id': '2', ' sequencce': ' TTAACCAAG', ' species': ' Herpes'}, {'#id': '3', ' sequencce': ' GCGAATGAC', ' species': ' Epstein-barr'}]

