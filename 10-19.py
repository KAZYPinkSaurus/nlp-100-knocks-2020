# https://nlp100.github.io/ja/ch02.html

#%%
# 10
file_name = "files/popular-names.txt"
with open(file_name) as f:
    print(len(f.readlines()))
# wc files/popular-names.txt

# %%
# 11
%time
# import re

# file_name = "files/popular-names.txt"
# with open(file_name) as f:
#     lines = f.readlines()
#     for line in lines:
#         re.sub(r"\t", " ", line)

import pandas as pd

df = pd.read_csv(file_name, header=None)
df.applymap(lambda x: x.replace("\t", " "))


# cat files/mini.txt | tr "\t" " "

# %%
# 12
%time
import csv

file_name = "files/popular-names.txt"
# col1 = []
# col2 = []
# with open(file_name) as f:
#     lines = csv.reader(f, delimiter="\t")
#     for row in lines:
#         col1.append([row[0]])
#         col2.append([row[1]])
# with open("col1.txt", "w") as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerows(col1)

# with open("col2.txt", "w") as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerows(col2)

import pandas as pd
# df = pd.read_table(file_name,header=None)
df = pd.read_csv(file_name,delimiter='\t',header=None)
df[0].to_csv('hoge_col1.txt',index=None)
df[1].to_csv('hoge_col2.txt',index=None)

# cut -f 1 files/popular-names.txt > col1.txt
# cut -f 2 files/popular-names.txt > col2.txt
# %%
# 13
%time
file_name = "files/popular-names.txt"

import numpy as np
pd.read_table(file_name,header=None)[0].to_csv('col1.txt',index=None)
pd.read_table(file_name,header=None)[1].to_csv('col2.txt',index=None)
col1 = pd.read_csv('col1.txt',header=None)
col2 = pd.read_csv('col2.txt',header=None)
(col1+'\t'+col2).to_csv('hoge_col12.tsv',index=None)

# paste col1.txt col2.txt

# %%
%time
# 14
file_name = "files/popular-names.txt"
N = 10
with open(file_name, "r") as f:
    for i in range(N):
        line = f.readline()
        if not line:
            break
        print(line, end="")

# pd.read_table(file_name,header=None)
# head -N files/popular-names.txt


# %%
# 15
file_name = "files/popular-names.txt"
N = 10
with open(file_name, "r") as f:
    lines = f.readlines()[-N:]
    print("".join(lines), end="")

# tail -N files/popular-names.txt


# %%
# 16
file_name = "files/mini.txt"
N = 4
with open(file_name, "r") as f:
    lines = f.readlines()
idx = 0
n_lines = len(lines)
if N <= n_lines:
    unit = n_lines // N
    for j in range(N):
        if j != N - 1:
            print("".join(lines[idx : idx + unit]))
            idx += unit
            continue
        print("".join(lines[idx:]))


# split -n N files/popular-names.txt


# %%
# 17

import csv

file_name = "files/popular-names.txt"
col1 = []
with open(file_name) as f:
    lines = csv.reader(f, delimiter="\t")
    for row in lines:
        col1.append(row[0])

print('\n'.join(set(col1)))

# cut -f 1 files/popular-nemase.txt | sort | uniq
# %%
# 18
file_name = "files/mini.txt"
col3_key_dict = {}
with open(file_name) as f:
    lines = f.readlines()
    for row in lines:
        col3_key_dict[int(row.split("\t")[2])] = row

sorted_tuples = sorted(col3_key_dict.items(), reverse=True)
for _, row in sorted_tuples:
    print(row, end="")
# sort -k 3 -r files/popular-names.txt

# %%
# 19
import csv
from collections import Counter

file_name = "files/popular-names.txt"
col1 = []
with open(file_name) as f:
    lines = csv.reader(f, delimiter="\t")
    for row in lines:
        col1.append(row[0])
# valueでソート
freq_tuplus = sorted(Counter(col1).items(), key=lambda x: x[1], reverse=True)
for name, freq in freq_tuplus:
    print(f"{name}:{freq}")


# cut -f 1 files/popular-names.txt | sort | uniq -c | sort -k 1 -r


# %%
