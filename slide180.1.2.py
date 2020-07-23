A = 0 #각 염기의 총 개수를 더할 변수 지정
T = 0
G = 0
C = 0

with open("059.fasta", 'r') as handle: #파일을 열어서
    for line in handle: #각 줄에 대해
        if line.startswith(">"): #만약 >로 시작한다면 header이기 때문에
            continue #넘어가라
        line = line.strip() #>로 시작하지 않는 줄에 대해서 strip하고 다시 line으로 저장 > string으로 저장됨
        a = line.count("A") #line이라는 string에서 A의 개수를 세서 a로 저장
        t = line.count("T") #line이라는 string에서 T의 개수를 세서 t로 저장
        g = line.count("G") #line이라는 string에서 G의 개수를 세서 g로 저장
        c = line.count("C") #line이라는 string에서 C의 개수를 세서 c로 저장
        A += a #A에 a를 더함 > A의 총 개수
        T += t #T에 t를 더함 > T의 총 개수
        G += g #G에 g를 더함 > G의 총 개수
        C += c #C에 c를 더함 > C의 총 개수

print(f"A: {A}, T: {T}, G: {G}, C: {C}") #결과를 출력
