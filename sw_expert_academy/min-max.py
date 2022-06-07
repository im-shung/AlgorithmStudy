# SW Expert Academy 
# 파이썬 SW문제해결 기본 - LIST1 6차시 

T = int(input())
result = list()

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    min = arr[0]
    max = arr[0]
    for a in arr:
        if a < min:
            min = a
        if a > max:
            max = a
    result.append(max-min)

for idx in range(len(result)):
    print("#"+str(idx+1),result[idx])