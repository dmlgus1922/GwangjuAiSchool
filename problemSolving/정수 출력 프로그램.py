n_l = [] #빈 리스트 선언
while True: #무한루프를 돌며
    n = list(map(int, input().split())) #입력 받는 값을 정수가 담기는 리스트로 바꿔준다. 구분자는 공백. 값을 하나만 받아도 문제없다.
    if 0 in n:  #사용자가 0을 입력했을 때
        n_l.extend(n[:n.index(0)][:100])  #0이 있는 인덱스를 찾고 그 앞까지 슬라이싱, 100개를 넘을 수 있으므로 또 슬라이싱해서 n리스트에 추가.
        break  
    n_l.extend(n[:100]) #0이 입력되지 않았을 때 n리스트에 저장

for i in n_l[::-1]:  #n리스트를 뒤집어 새로 생성한 리스트를 순회하며 i값에 저장
    if i == 0:  #위에서 입력한 값 중 0을 제거하지 않았으므로 0이 존재한다면 건너뛰기
        continue
    print(i, end = ' ')  #end를 공백으로 설정해줘서 한 줄로 출력되도록 함

    
n_l = []
while len(n_l) < 100:
    n = list(map(int, input().split()))
    if 0 in n:
        n_l.extend(n[:n.index(0)])
        break
    n_l.extend(n)
n_l = n_l[:100]
#매번 99인덱스까지 슬라이싱 하지 않고 while문을 나왔을 때 한번만 슬라이싱해도 된다. 0도 지워진 상태.
for n in n_l[::-1]:
    print(n, end = ' ')
