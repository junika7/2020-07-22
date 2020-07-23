comp = '' #각 줄의 상보적인 서열을 저장할 빈 string 설정
comp_total_seq = '' #각 줄의 상보적인 서열을 하나로 합칠 빈 string 설정

with open("059.fasta", 'r') as handle: #파일을 열어서
    for line in handle: #각 줄에 대해
        if line.startswith(">"): #만약 줄이 >로 시작하면
            continue #넘어가라
        stripped = line.strip() #각 줄을 strip하고 splitted로 저장 > string으로 저장됨
        comp = stripped.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper() #stripped string에서 상보적인 서열을 만들고 comp로 저장 > string으로 저장됨
        comp_total_seq += comp #comp들을 하나로 합쳐서 comp_total_seq에 저장 > string으로 저장됨

print(comp_total_seq[::-1]) #comp_total_seq string을 역순으로 출력
