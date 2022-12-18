import sys

n, k = map(int, sys.stdin.readline().split())
cnt = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n = n // k
        cnt +=1
    else:
        n -= 1
        cnt +=1
print(cnt)

# n = 1이 될때까지 진행
# 1. n에서 -1 함
# 2. n을 k로 나눔 (단, 나누어 떨어질때만 가능)
# 최소의 횟수