#강사님이 하신 것
import pandas as pd #pandas는 python에서 dataframe을 사용하기 위해서 만든 기능
from matplotlib import pyplot as plt #pandas와 matplotlib은 pip install ~로 설치 후 사용 가능

d = {"SNP":0, "INS":0, "DEL":0} #각 변이의 수를 저장할 딕셔너리 설정

with open("070.vcf", 'r') as handle: #파일을 열어서
    for line in handle: #각 줄에 대해
        if line.startswith("#"): #만약 줄이 #로 시작한다면
            continue #넘어가라
        splitted = line.strip().split("\t") ##로 시작하지 않는 줄에 대해서 strip하고 탭으로 split 후 splitted로 저장 > 리스트로 저장됨
        ref = splitted[3] #splitted 리스트의 3번 index가 ref이므로 이 원소를 ref로 지정 > string
        alts = splitted[4].split(",") #splitted 리스트의 4번 index가 alt이므로 이 원소를 alts로 지정 > list로 저장됨(multi alt가 있을 수 있어서 ,로 split함) 
        for alt in alts: #alts 리스트의 원소에 해당하는 alt에 대해서
            if len(ref) == len(alt): #alt와 ref의 길이가 같으면 SNP
                d["SNP"] += 1 #딕셔너리의 SNP key에 1 추가
            elif len(ref) > len(alt): #alt의 길이가 ref보다 짧으면 deletion
                d["DEL"] += 1 #딕셔너리의 DEL key에 1 추가
            elif len(ref) < len(alt): #alt의 길이가 ref보다 길면 insertion
                d["INS"] += 1 #딕셔너리의 INS key에 1 추가
            else: #방어적 코딩
                raise #방어적 코딩
print(d) #딕셔너리를 출력
df = pd.DataFrame([d]) #딕셔너리를 dataframe 형식으로 바꿈
print(df) #dataframe 형식으로 바뀐 것을 출력
df.plot.bar() #dataframe 형식으로 바뀐 것을 이용해서 bar 그래프가 그려짐
plt.savefig("v.png") #그려진 bar 그래프를 파일로 저장
