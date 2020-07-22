import sys

class FASTA: #FASTA 형식에 적용할 class 설정
    def __init__(self, file_name): #초기화 메소드
        self.file_name = file_name #속성 3개 지정
        self.count = {}
        self.length = 0
    def count_base(self): #염기 개수 세는 메소드
        with open(self.file_name, 'r') as handle:
            for line in handle: #line을 받아서
                if line.startswith(">"): #만약 >로 시작하면
                    continue #그냥 넘어가라 > header이므로
                line = line.strip() #header가 아닌 line에 대해서 strip()하고
                for s in line: #line에 있는 문자 하나하나에 대해서
                    if s in self.count: #만약 self.count라는 딕셔너리에 있으면 
                        self.count[s] += 1 #해당 문자에 대한 value 값에 1을 더하고
                    else: #만약 해당 문자가 딕셔너리에 없으면
                        self.count[s] = 1 #1을 value로 설정 > 처음 값이 1로 설정되는 원리
    def __len__(self): #염기 서열의 총 길이를 세는 메소드. import tool > t = tool.FASTA("059.fasta") > t.count_base() >  len(t) 가능
        for k, v in self.count.items(): #self.count 딕셔너리에 있는 key, value들에 대해서
            self.lenght += v #self.length는 value들의 합으로 설정 > 총 염기 개수가 self.length에 설정됨
        return self.length #반환값으로 self.length를 설정

class FASTQ: #FASTQ 형식에 적용할 class 설정
    def __init__(self, file_name): #초기화 메소드
        self.file_name = file_name #속성 2개 지정
        self.read_num = 0
    def count_read_num(self): #read 수를 계산하는 메소드
        cnt = 0 #cnt 변수를 0으로 설정
        with open(self.file_name, 'r') as handle:
            for line in handle: #line을 한줄 씩 받아서 cnt=0으로 시작
                if cnt % 4 == 0: #cnt를 4로 나눈 나머지가 0이면 
                    header = line.strip() #line을 strip해서 header로 저장하고
                    self.read_num += 1 #self.read_num에 1을 더함
                elif cnt % 4 == 1: #만약 cnt를 4로 나눈 나머지가 1이면
                    seq = line.strip() #line을 strip해서 seq으로 저장(sequence에 해당하는 줄이므로)
                elif cnt % 4 == 3: #만약 cnt를 4로 나눈 나머지가 3이면
                    qual = line.strip() #line을 strip해서 qualfh 저장(quality에 해당하는 줄이므로)
                cnt += 1 #cnt에 1을 더하고 for문 반복(나머지가 2인것은 +(구분자)이므로 의미없어서 버림)

if __name__ == "__main__": #import해서 사용시 이 밑으로는 실행되지 않음
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [fasta]")
        sys.exit()
    file_name = sys.argv[1]
    t = FASTQ(file_name)
    t.count_read_num()
    print(t.read_num)
