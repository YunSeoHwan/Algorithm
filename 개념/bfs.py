from collections import deque

graph = [[], [2,3,4], [5], [5], [], [6,7], [], [3]]
visited = []

# list로 queue 구현
def bfs(v):
    visited = [v]
    queue = [v]

    # queue가 다 비워질때 까지
    while queue:
        # 가장 먼저 들어간 원소 pop
        v = queue.pop(0)
        print(v, end=' ')

        # 너비 우선으로 탐색
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)

def queue_bfs(v):
    visited = [v]
    queue = deque([v])
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    
queue_bfs(1)                        # 1 2 3 4 5 6 7 
bfs(1)                              # 1 2 3 4 5 6 7 

# BFS는 queue를 이용하여 구현 (deque 사용)
# BFS로 재귀 구현시, 시간초과 발생! -> queue로 접근해서 풀 것!