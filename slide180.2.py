import json #json을 import

d = {} #염기의 수를 count하는 과정을 slide180.1.py와 동일

with open("059.fasta", 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        splitted = line.strip()
        for i in splitted:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

with open("slide180.2.json", 'w') as handle: #slide180.2.json이라는 파일을 만들면서 그 파일에 다음에 나오는 내용을 작성
    json.dump(d, handle, indent=4) #d 딕셔너리를 indent=4 형태의 json 파일로 작성 > cat slide180.2.json으로 저장된 파일 확인 가능
