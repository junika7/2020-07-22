"""
cnt = 0
l = []

with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().split("\t")
            alt_idx = header.index("ALT")
            continue
        splitted = line.strip().split("\t")
        l.append(splitted[alt_idx])
        for i in l:
            if "," in i:
                l.remove(i)
                j = i.split(",")
                l += j
print(l)
print(len(l))
"""
#위에는 내가 한 것
#아래는 강사님이 한 것

cnt = 0

with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue

        splitted = line.strip().split("\t")
        alts = splitted[4].split(",")
        for alt in alts:
            cnt += 1
print(cnt)
