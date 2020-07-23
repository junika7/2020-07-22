"""
cnt = 0 #cnt 변수를 설정
l = [] #빈 리스트 설정

with open("070.vcf", 'r') as handle: #파일을 열어서
    for line in handle: #각 줄에 대해
        if line.startswith("##"): #만약 ##로 시작하면
            continue #넘어가라
        if line.startswith("#"): #만약 #로 시작하면
            header = line.strip().split("\t") #줄을 해당 줄을 strip하고 탭으로 split해서 header로 저장 > 리스트로 저장됨
            alt_idx = header.index("ALT") #header 리스트에서 ALT에 해당하는 index를 찾아서 alt_idx로 저장하고
            continue #넘어가라(이거 안넣으면 ALT가 count되어서 15로 결과가 나옴)
        splitted = line.strip().split("\t") ##로 시작하지 않는 줄에 대해서 strip하고 탭으로 split해서 splitted로 저장 > 리스트로 저장됨
        l.append(splitted[alt_idx]) #l 리스트에 splitted 리스트에서 alt_idx에 해당하는 원소들을 추가
        for i in l: #l 리스트의 원소에 해당하는 i에 대해서
            if "," in i: #만약 ,가 있다면(multi alt인 경우)
                l.remove(i) #일단 i 항목을 제거하고
                j = i.split(",") #i를 ,로 split한 것을 j 리스트로 저장하고
                l += j #l 리스트에 j의 원소들을 추가
print(l) #alt가 포함된 리스트를 출력
print(len(l)) #l 리스트의 길이를 통해서 alt의 개수를 출력
"""
#위에는 내가 한 것
#아래는 강사님이 한 것

cnt = 0 #ALT 개수를 추가할 cnt 변수 설정

with open("070.vcf", 'r') as handle: #파일을 열어서
    for line in handle: #각 줄에 대해
        if line.startswith("#"): #만약 #로 시작하면
            continue #넘어가라
        splitted = line.strip().split("\t") ##로 시작하지 않는 줄에 대해서 strip하고 탭으로 split해서 splitted로 저장 > 리스트로 저장됨
        alts = splitted[4].split(",") #***splitted 리스트의 4번 index가 ALT 항목인데, 이 리스트를 받으면서 ,로 split하면 split된 원소가 각각의 원소로 alts 리스트에 저장됨***
        for alt in alts: #alts 리스트의 원소에 해당하는 alt에 대해서
            cnt += 1 #각 alt에 대해서 cnt에 1을 추가 > alt의 개수 count
print(cnt) #cnt를 출력
