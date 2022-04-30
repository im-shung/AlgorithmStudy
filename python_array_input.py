# 배열 입력 

# 3
# 1 2 3
# 4 5 6
# 7 8 9

# Good Code
MAP = [list(map(int,input().split())) for _ in range(int(input()))]

#Bad Code
for i in range(int(input())): 
    inputStr = input() 
    arr = list(inputStr) 
    MAP.append(arr)