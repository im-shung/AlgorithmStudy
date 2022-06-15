# SW Expert Academy 
# 파이썬 SW문제해결 기본 - LIST1 8차시 

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input()))
    
    # 카드가 0 - 9 까지만 존재하니까 0부터 9까지를 담을 수 있는 크기가 10인 리스트를 만든다.
    mid = [0] * 10
    for a in arr:
        mid[a] += 1
        
    max = 0
    for i in range(len(mid)):
        if mid[i] >= mid[max]:
            max = i
    print("#"+str(test_case),max,mid[max])