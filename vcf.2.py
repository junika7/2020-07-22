"""
with open("070.vcf", 'r') as handle: #파일을 열어서
    for line in handle: #각 줄에 대해
     if line.startswith("#"): #만약 #로 시작하면
            continue #넘어가라
     splitted = line.strip().split("\t") ##로 시작하지 않는 줄에 대해서 strip하고 탭으로 split > 리스트로 저장됨
     if splitted[2] != ".": #만약 splitted 리스트에서 2번 index인 ID열의 값이 .이 아니라면
            print(splitted[0], "\t", splitted[1], "\t", splitted[3], "\t", splitted[4], "\t", splitted[2]) #각 정보를 출력
"""
#위에는 내가 한 것
#아래는 강사님이 한 것

with open("070.vcf", 'r') as handle: #파일을 열어서
    for line in handle: #각 줄에 대해
        if line.startswith("##"): #만약 ##로 시작하면
            continue #넘어가라
        if line.startswith("#"): #만약 #로 시작하면
            header = line.strip().split("\t") #해당 줄을 strip하고 탭으로 split해서 header로 저장 > 리스트로 저장됨
            id_idx = header.index("ID") #header 리스트에서 ID에 해당하는 index를 찾아서 id_idx로 저장
        splitted = line.strip().split("\t") ##로 시작하지 않는 줄을 strip하고 탭으로 split > 리스트로 저장됨
        chrom = splitted[0] #chrom열에 해당하는 원소의 index는 0
        pos = splitted[1] #pos열에 해당하는 원소의 index는 1
        id_ = splitted[2] #id열에 해당하는 원소의 index는 2(id는 내장함수라서 변수로 사용할 수 없어서 id_로 설정)
        ref = splitted[3] #ref열에 해당하는 원소의 index는 3
        alt = splitted[4] #alt열에 해당하는 원소의 index는 4
        if splitted[id_idx] != ".": #만약 id열에 해당하는 원소가 .이 아니라면
            print(f"{chrom}\t{pos}\t{ref}\t{alt}\t{id_}") #각 항목을 출력
