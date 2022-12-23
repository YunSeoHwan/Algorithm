# DFS 깊이 우선 탐색
# 재귀구조와, stack으로 구현

graph = [[], [2,3,4], [5], [5], [], [6,7], [], [3]]
visited = []

# 재귀DFS
def recursive_dfs(v):

    # 시작노드 삽입
    visited.append(v)
    print(v, end=' ')

    # 시작노드 위치에서 깊이 순서로 방문
    for i in graph[v]:
        if i not in visited:
            recursive_dfs(i)

# Stack DFS
def stack_dfs(v):
    stack = [v]
    
    # stack이 빌때까지 반복
    while stack:

        # stack에서 pop
        v = stack.pop()

        # v가 방문되지 않았으면 삽입하고, 그 위치에서 다시 검색
        if v not in visited:
            visited.append(v)
            print(v, end=' ')
            for w in graph[v]:
                stack.append(w)

recursive_dfs(1)                    # 1 2 5 6 7 3 4
stack_dfs(1)                        # 1 2 5 6 7 3 4