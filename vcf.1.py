cnt = 0

with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().split("\t")
            filt_idx = header.index("FILTER") #FILTER cloumn의  index number를 찾아서 filt_idx로 저장

        splitted = line.strip().split("\t")
        if splitted[filt_idx] == "PASS":
            cnt += 1

print(cnt)
