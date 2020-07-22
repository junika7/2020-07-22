import sys

l1 = ['A', 'C', 'G', 'T']
l2 = ['A', 'C', 'G', 'T']

def mer(l1, l2, n): #mer라는 함수를 정의
    l_tmp = [] #빈 리스트 설정
    if n == 1: #n=1이면 그냥 l2를 반환값으로 설정
        return l2
    if n > 1: #n이 2이상이면
        for i in l1: #l1의 원소인 i와
            for j in l2: #l2의 원소인 j에 대해서
                l_tmp.append(i+j) #i+j를 l_tmp 리스트에 추가하고
    return mer(l1, l_tmp, n-1) #mer 함수에 l1, l_tmp, n-1을 인수로 넣는 것을 반환값으로 설정

"""
만약 n=3이면 아래쪽 if로 들어가고, l_tmp = ['AA', 'AC', 'AG', ..., 'TG', 'TT']로 설정됨
그 다음, 반환값을 보면 l1, l_tmp, n-1을 인수로 해서 mer 함수가 다시 돌아가도록 했음
다시 l_tmp라는 빈 리스트가 설정됨(원래의 l_tmp는 이미 인수로 받은 상황)
그러면 n-1은 2가 되므로 역시 아래쪽 if로 들어가고, l1 = ['A', 'C', 'G', 'T']의 i와
l_tmp = ['AA', 'AC', ..., 'TT']의 j에 대해서 i+j 값이 다시 l_tmp에 추가됨
그럼 l_tmp = ['AAA', 'AAC', ..., 'TTT']로 설정됨
반환값은 l1, l_tmp, n-1을 인수로 해서 mer 함수가 다시 돌아가도록 했음
이제는 n-1이 1이므로 위쪽 if로 들어가서 l2를 반환값으로 설정함
지금 상태에서 l2는 인수로 받은 항목 중 두번째 리스트를 의미하므로, l2는 l_tmp임
따라서 l_tmp가 출력되고, 모든 가능한 3mer의 리스트를 확인할 수 있음
"""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [number]")
    print(mer(l1, l2, int(sys.argv[1])))
