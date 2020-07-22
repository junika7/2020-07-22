"""
with open("070.vcf", 'r') as handle:
    for line in handle:
     if line.startswith("#"):
            continue
     splitted = line.strip().split("\t")
     if splitted[2] != ".":
            print(splitted[0], "\t", splitted[1], "\t", splitted[3], "\t", splitted[4], "\t", splitted[2])
"""
#위에는 내가 한 것
#아래는 강사님이 한 것

with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().split("\t")
            id_idx = header.index("ID")

        splitted = line.strip().split("\t")
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alt = splitted[4]
        if splitted[id_idx] != ".":
            print(f"{chrom}\t{pos}\t{ref}\t{alt}\t{id_}")
