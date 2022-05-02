# 백준 2829번 이진수 덧셈

# 조건: 숫자의 앞에 불필요한 0이 붙으면 안 된다.
# 이진법의 표시로 0b가 앞에 붙어있으니 제거해서 출력한다.

for _ in range(int(input())) :
    A,B = map(lambda x: int(x,2),input().split())
    print(bin(A+B)[2:])
