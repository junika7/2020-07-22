def mer(l1, l2, n):
    if n == 1:
        return l2
    ltmp = []
    for i in l1:
        for j in l2:
            ltmp.append(i+j)
    return mer(l1, ltmp, n-1)

l1 = ['A', 'T', 'G', 'C']
l2 = ['A', 'T', 'G', 'C']

cnt = 0 #cnt 변수를 0으로 설정

for i in mer(l1, l2, 7): #7mer에 속하는 i에 대해서
    if i == i[::-1]: #만약 i와 i를 거꾸로 읽은 것이 같다면
        cnt += 1 #cnt에 1을 더함

print(cnt) #cnt를 출력

