"""
l = [] #각 행을 저장할 빈 list 설정

with open("070.vcf", 'r') as handle: #파일을 열어서
    for line in handle: #각 줄에 대해
        if line.startswith("#"): #만약 줄이 #로 시작하면(vcf파일은 데이터 줄 빼고 전부 ##로 시작하고, column 항목은 #로 시작함)
            continue #넘어가라
        splitted = line.strip().split("\t") ##로 시작하는 줄이 아니면 strip하고 탭으로 split > 리스트로 저장됨
        l.append(splitted) #splitted를 l 리스트에 추가하고
print(len(l)) #l 리스트의 길이를 통해서 행의 개수를 출력(각 행이 리스트이지만 l 리스트는 리스트를 원소로 하는 리스트이므로)
"""
#위에는 내가 한 것
#아래는 강사님이 한 것

cnt = 0 #행의 개수를 추가할 cnt 변수 설정

with open("070.vcf", 'r') as handle: #파일을 열어서
    for line in handle: #각 줄에 대해
        if line.startswith("#"): #만약 줄이 #로 시작하면
            continue #넘어가라
        else: #만약 줄이 #로 시작하는게 아니면
            cnt += 1 #cnt에 1을 더함 > 전체 줄에 대해서 반복됨
print(cnt) #cnt를 출력
