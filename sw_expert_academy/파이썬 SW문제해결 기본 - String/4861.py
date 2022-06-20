# SW Expert Academy 
# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문 D2

# 문제
# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
# 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.


# 입력
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

# 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

# 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

# 출력
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    #배열 입력 받기
    arr = []
    for i in range(N):
        arr.append(input()) # arr = ['WPMACSIBIK', 'STWASDCOBQ', 'AMOUENCSOG', 'XTIIGBLRCZ', 'WXVSWXYYVU', 'CJVAHRZZEM', 'NDIEBIIMTX', 'UOOGPQCBIW', 'OWWATKUEUY', 'FTMERSSANL']

    # 가로 검색
    for r in range(N): 
        for c in range(N - M + 1):
            # 회문이 맞는지 확인
            if arr[r][c : c + M] == arr[r][c : c + M][ : : -1]: # [start : end : step] step만큼 문자를 건너뛰면서, start오프셋부터 end-1 오프셋(인덱스)까지 추출
                print(f"#{test_case} {''.join(arr[r][c : c + M])}")
    
    # 세로 검색
    for r in range(N - M + 1):
        for c in range(N):
            arr2 = [] # 세로 열 리스트 만들기
            for i in range(M):
                arr2.append(arr[r+i][c])
            if arr2 == arr2[ : : -1]: # [start : end : step] step만큼 문자를 건너뛰면서, start오프셋부터 end-1 오프셋(인덱스)까지 추출
                print(f"#{test_case} {''.join(arr2)}")