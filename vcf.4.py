#강사님이 하신 것
import pandas as pd #pandas는 python에서 dataframe을 사용하기 위해서 만든 기능
from matplotlib import pyplot as plt

d = {"snp":0, "ins":0, "del":0}

with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        splitted = line.strip().split("\t")

        ref = splitted[3]
        alts = splitted[4].split(",")
        for alt in alts:
            if len(ref) == len(alt): #snp
                d["snp"] += 1
            elif len(ref) > len(alt): #deletion
                d["del"] += 1
            elif len(ref) < len(alt): #insertion
                d["ins"] += 1
            else: #방어적 코딩
                raise #방어적 코딩
print(d)
df = pd.DataFrame([d]) #딕셔너리를 dataframe 형식으로 바꿈
print(df)
df.plot.bar() #bar 그래프가 그려짐
plt.savefig("v.png") #그래프를 파일로 저장
