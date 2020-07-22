import sys
import json

def read_txt(file_name: str) -> str: #여러 line으로 이루어진 문서를 하나의 line으로 출력
    ret = "" #빈 string 설정
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith(">"): #만약 line이 >로 시작한다면 header이기 때문에
                continue #그냥 넘어가라
            ret += line.strip() #>로 시작하지 않는 line들은 strip후 빈 string인 ret에 추가
    return ret #반환값을 ret으로 설정

def read_csv(file_name: str) -> list:
    ret = [] #빈 list 설정
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"): ##로 시작하는 line은
                header = line.strip().split(",") #line을 strip하고 ,로 split해서 header로 지정
                continue #넘어가라
            splitted = line.strip().split(",") ##로 시작하지 않는 line들에 대해서 똑같이 가공해서 splitted로 지정하고
            ret.append(splitted) #가공한 splitted를 빈 list인 ret에 추가
    return ret #반환값을 ret으로 설정

def read_tsv(file_name: str) -> list:
    ret = [] #빈 list 설정
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
#            print(header) #header 출력
#            print(splitted) #splitted 출력 > for문이므로 header-splitted-header-splitted-... 순서로 출력됨
#            print(type(header)) #header와 splitted의 type이 list인 것 알 수 있음
#            print(type(splitted))
            d = dict(zip(header, splitted)) #zip으로 두 리스트를 하나의 list로 합치고, 그 list를 딕셔너리로 만들어줌
            ret.append(d) #빈 list에 생성되는 딕셔너리를 원소로서 추가
    return ret #반환값을 ret으로 설정

def to_json(l: list, file_name: str) -> None: #list를 json 파일로 만드는 함수를 정의
    with open(file_name, 'w') as handle: #입력하는 파일명의 파일을 만들면서 아래 내용을 작성
        json.dump(l, handle, indent = 4) #입력받는 list를 indent 4의 json 형식으로 작성

def read_json(file_name: str) -> list: #다른 스크립트에서 import readtext 후 readtxt.read_json("~~~") 하면 사용 가능
    with open(file_name, 'r') as handle:
        l = json.load(handle)
    return l

if __name__ == "__main__": #import해서 사용할 때 이 밑으로는 실행되지 않음
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [txt]")
        sys.exit()

    file_name = sys.argv[1]
    #result1 = read_txt(file_name)
    #print(result1)
    #result2 = read_csv(file_name)
    #print(result2)
    #result3 = read_tsv(file_name)
    #print(result3)
    #csv_list = read_csv(file_name)
    #to_json(csv_list, "csv_to_json_result.json")
    #tsv_list = read_tsv(file_name)
    #to_json(tsv_list, "tsv_to_json_result.json")
    result_slide139 = read_csv(file_name)
    print(result_slide139)
    to_json(result_slide139, "slide139_to_json_result.json")
