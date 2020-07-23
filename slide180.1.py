d = {} #빈 딕셔너리 설정

with open("059.fasta", 'r') as handle: #파일을 열어서
    for line in handle: #각 줄에 대해
        if line.startswith(">"): #만약 >로 시작한다면 header이기 때문에
            continue #넘어가라
        line = line.strip() #>로 시작하지 않는 줄에 대해서 strip하고 다시 line으로 저장 > string으로 저장됨
        for i in line: #line에 있는 각 i(letter)에 대해서
            if i in d: #만약 d 딕셔너리에 i가 있으면
                d[i] += 1 #d 딕셔너리의 i key의 value에 1 추가
            else: #만약 d 딕셔너리에 i가 없으면
                d[i] = 1 #d 딕셔너리의 i key의 value에 1 설정(처음 나오는 염기의 개수가 1로 설정됨)
print(d) #딕셔너리를 출력
