cnt = 0 #filter = PASS인 행의 개수를 추가할 cnt 변수 설정

with open("070.vcf", 'r') as handle: #파일을 열어서
    for line in handle: #각 줄에 대해
        if line.startswith("##"): #만약 ##로 시작하면
            continue #넘어가라
        if line.startswith("#"): #만약 #로 시작하면(column의 항목이 나온 줄)
            header = line.strip().split("\t") #strip하고 탭으로 split해서 header로 저장 > list로 저장됨
            filt_idx = header.index("FILTER") #header 리스트에서 FILTER cloumn의 index number를 찾아서 filt_idx로 저장

        splitted = line.strip().split("\t") ##로 시작하지 않는 줄에 대해서 strip하고 탭으로 split > list로 저장됨
        if splitted[filt_idx] == "PASS": #만약 splitted 리스트에서  filter column에 해당하는 원소가 PASS이면
            cnt += 1 #cnt에 1 추가 > 전체 줄에 대해서 반복

print(cnt) #cnt를 출력
