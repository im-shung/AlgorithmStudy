# SW Expert Academy 
# 파이썬 SW문제해결 기본 - LIST1 6차시 

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))

    print("#"+str(test_case),max(arr)-min(arr))
