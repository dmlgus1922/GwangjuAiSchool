a_l = [] #문자를 담을 리스트 선언

i = 0 #for문을 돌며 인덱스 확인을 위한 i 선언, 매번 for문을 돌 때마다 0부터 다시 시작하면 비효율적이므로 반복문 밖에서 따로 초기화함
while True: # 무한루프. 대문자 알파벳 외의 문자가 들어오지 않는 한 계속 입력받는 형태
    a = input().split() #사용자에게 입력받는 문자를 리스트로 저장
    a_l.extend(a)  # 저장할 리스트에 원소를 저장
    for _ in range(i, len(a_l)):  # 초기화한 i부터 a_l 리스트 끝까지 순회
        if a_l[i] < 'A' or a_l[i] > 'Z':  # 각 원소가 대문자 알파벳 범위 내에 있지 않을 때
            a_l = a_l[:i+1]    # 대문자가 아닌 그 원소까지 포함하여 슬라이싱하고 for문 종료
            break
        i += 1   #원소가 대문자 알파벳이라면 i를 증가시켜 다음 원소를 확인할 수 있도록 해줌.
                 #i는 for문을 나가도 값이 유지되어 사용자에게 다음 번 입력받은 문자부터 다시 순회할 수 있게 해준다.

    if a_l[-1] < 'A' or a_l[-1] > 'Z':  # 위에서 대문자 알파벳 외의 문자가 입력되었을 때 그 문자까지 포함하여 슬라이싱했으므로 마지막 원소는 다른 문자.
        a_l.pop()   #확인용으로 포함시켰던 그 다른 문자를 pop해주고 무한루프 탈출.
        break

set_a = list(set(a_l))  #a_l리스트에 저장된 원소를 중복 없이 출력하기 위해 중복제거한 리스트 하나 생성
for i in sorted(set_a):  # 중복제거한 리스트를 정렬시켜 순회하며 각 대문자의 개수 출력
    print(f'{i} : {a_l.count(i)}')
