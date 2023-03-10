# 리스트 컴프리헨션
# 배열 안에서 조건, 반복문으로 배열 값 할당 가능
list = [i+1 for i in range(10) if (i+1) % 2 == 0]         #[2, 4, 6, 8, 10]

# 2차원 배열 컴프리헨션 주의
array = [[0] * 4 for _ in range(3)]             # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
array[1][1] = 2                                 # [[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]]

n_array = [[0] * 4] * 3                         # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
n_array[1][1] = 2                               # [[0, 2, 0, 0], [0, 2, 0, 0], [0, 2, 0, 0]]

# 전역 변수 사용하기
a = 10
def func():
    global a
    a+=1
    print(a)                                    # 11

# 람다식 사용하기
array = [('홍길동', 30), ('이순신', 40), ('유관순', 10)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))                    # [('유관순', 10), ('홍길동', 30), ('이순신', 40)]
print(sorted(array, key=lambda x:x[1]))             # [('유관순', 10), ('홍길동', 30), ('이순신', 40)]