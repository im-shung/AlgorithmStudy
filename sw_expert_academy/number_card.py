# SW Expert Academy 
# 파이썬 SW문제해결 기본 - LIST1 8차시 

T = int(input())
result = list()

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input()))
    
    mid = [0,0,0,0,0,0,0,0,0,0]
    for a in arr:
        mid[a]+=1
        
    max = 0
    for idx in range(len(mid)):
        if mid[idx] > mid[max]:
            max = idx
        elif mid[idx] == mid[max]:
            if idx > max:
                max = idx
    result.append(str(max)+" "+str(mid[max]))

for idx in range(len(result)):
    print("#"+str(idx+1),result[idx])