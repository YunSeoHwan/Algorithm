import sys

n, m = map(int, sys.stdin.readline().split())
min_num = 0
for i in range(n):
    array = list(map(int, sys.stdin.readline().split()))
    if min_num < min(array):
        min_num = min(array)
print(min_num)

def sol_card():
    n, m = map(int, sys.stdin.readline().split())

    result = 0
    # 한 줄씩 입력받아 확인
    for i in range(n):
        data = list(map(int, sys.stdin.readline().split()))
        
        # 현재 줄에서 가장 작은 수 찾기
        min_value = min(data)

        # 가장 작은 수들 중에서 가장 큰 수 찾기
        result = max(result, min_value)
    print(result)

# 비교연산이 아닌 max를 이용해보자!