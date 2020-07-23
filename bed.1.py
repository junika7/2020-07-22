length = 0 #length 변수 0으로 설정
l1 = [] #빈 리스트인 l1, l2 설정
l2 = []

with open("077.1.bed", 'r') as handle: #077.1.bed 파일 열기
    for line in handle:
        splitted = line.strip().split("\t") #각 줄을 strip하고 탭으로 split해서 splitted로 저장 > splitted는 list
        chro = splitted[0] #splitted의 0번 index가 chromosome
        start = splitted[1] #splitted의 1번 index가 start 위치
        end = splitted[2] #splitted의 2번 index가 end 위치
        length = int(end) - int(start) #길이를 구하려고 end위치에서 start위치를 int로 받아서 뺌
        l1.append(chro) #l1에 chromosome을 저장
        l2.append(length) #l2에 length를 저정

d = dict(zip(l1, l2)) #dict(zip())으로 두 리스트를 합쳐서 딕셔너리로 만들고

print(d) #딕셔너리를 출력
