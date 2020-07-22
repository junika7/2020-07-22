"""
count = 0
l = []

with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        splitted = line.strip().split("\t")
        l.append(splitted)
print(len(l))
"""
#위에는 내가 한 것
#아래는 강사님이 한 것

cnt = 0
cnt_pass = 0

with open("070.vcf", 'r') as handle:
    for line in handle: #line을 하나씩 받음
        if line.startswith("#"):
            continue
        cnt += 1
#        if "PASS" in line: #내가 한 것
#            cnt_pass += 1 #내가 한 것
        splitted = line.strip().split("\t")
        if splitted[6] == "PASS":
            cnt_pass += 1
print(cnt)
print(cnt_pass)
