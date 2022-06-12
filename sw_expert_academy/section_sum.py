# SW Expert Academy 
# 파이썬 SW문제해결 기본 - LIST1 9차시

T = int(input())
result = list()

for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    sum_list = list()
    for i in range(0, N - M+1):
        sum = 0
        for j in range(0,M):
            sum+=arr[i+j]
        sum_list.append(sum)
    
    max=sum_list[0]
    min=sum_list[0]
    for idx in range(len(sum_list)):
        if min > sum_list[idx]:
            min = sum_list[idx]
        if max < sum_list[idx]:
            max = sum_list[idx]
    result.append(max-min)
    
for idx in range(len(result)):
    print("#"+str(idx+1),result[idx])