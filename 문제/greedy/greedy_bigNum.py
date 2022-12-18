import sys

def bigNum():
    n, m, k = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))
    result = 0
    real_k = k

    # 배열 내림차순 정렬
    array = sorted(array, reverse=True)
    while True:
        if m == 0:
            break
        if k == 0:
            # 연속된 수 다음 -> 두번째로 큰 수 더하기
            result+=array[1]
            k = real_k
            m-=1
        else:
            result += array[0]
            m-=1
            k-=1
    print(result)

def sol_bigNum():
    n, m, k = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))

    array.sort()    # 정렬
    first = array[n-1]
    second = array[n-2]

    result = 0

    while True:
        for i in range(k):      # 가장 큰 수를 k번 더하기
            if m==0:
                break
            result += first
            m-=1
        
        if m == 0:
            break
        result += second        # 두 번째로 큰 수 더하기
        m-=1
    print(result)

# 반복되는 수열로 접근 ex) m = 8, k = 3 -> 6665 + 6665 6665가 반복됨
def sol2_bigNum():
    n, m, k = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))

    array.sort()    # 정렬
    first = array[n-1]
    second = array[n-2]

    # 가장 큰 수가 더해지는 횟수 계산
    count = int(m/(k+1)) * k
    count += m % (k+1)              # 나누어 떨어지지 않는 횟수

    result = 0
    result += (count) * first       # 가장 큰 수 더하기
    result += (m-count) * second    # 두 번째로 큰 수 더하기

    print(result)