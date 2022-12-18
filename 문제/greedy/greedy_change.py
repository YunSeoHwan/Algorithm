def change(n):
    cnt = 0
    cnt += n // 500
    n = n % 500
    cnt += n // 100
    n = n % 100
    cnt += n // 50
    n = n % 50
    cnt += n // 10
    n = n % 10    
    return cnt

def sol_change(n):
    cnt = 0
    list = [500, 100, 50, 10]

    for coin in list:
        cnt += n // coin
        n %= coin

    return cnt

# 반복되는 작업을 for문 처리하지 못함. O(1) 복잡도
# 알고리즘 정당성을 확인하자! ex) 500 400 100 단위, 800원
# 그리디 -> 500 + 100 * 3
# 최적의 해 -> 400 * 2
# 