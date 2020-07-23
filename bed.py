"""
import sys

if len(sys.argv) != 2: #파일명 입력하라는 문구
    print(f"#usage: python {sys.argv[0]} [.bed]")
    sys.exit()

f = sys.argv[1] #입력받은 파일명을 f로 저장

length = 0 #각 bed의 구간 길이를 저장할 변수 설정
whole_length = 0 #전체 길이를 저장할 변수 설정

with open(f, 'r') as handle: #f 를 열어서
    for line in handle: #각 줄에 대해서
        splitted = line.strip().split("\t") #strip하고 탭으로 split > list로 저장됨
        length = int(splitted[2]) - int(splitted[1]) #index 2가 end, index 1이 start이므로 end-start로 길이를 구하고 각 길이를 length에 저장
        whole_length += length #length들을 whole_length에 합쳐서 총 길이를 저장
    print(f"whole length: {whole_length}") #총 길이를 출력
"""
#위에는 내가 한 것
#아래는 강사님이 한 것
total = 0 #전체 길이를 저장할 변수 설정

with open("077.bed", 'r') as handle:
    for line in handle:
        splitted = line.strip().split("\t")
        start = int(splitted[1])
        end = int(splitted[2])
        total += end - start #length를 따로 안구하고 한번에 total에 합침

print(total)

