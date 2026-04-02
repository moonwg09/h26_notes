# 그래프 만들기 ()

graph = [[] for _ in range(8)]
graph[1] = [2,3]
graph[2] = [4,5]
graph[4] = [5,7]
graph[3] = [4,6]
graph[5] = [7]
graph[6] = [7]


visited_list = []

def dfs(node):
    # 방문했다고 표시 => 방문한 노드를 모아놓는 리스트 활용
    visited_list.append(node)
    # 할 일 하기
    print(node)
    # 순회
    for adj_node in graph[node]:
        if adj_node not in visited_list:
            dfs(adj_node)

dfs(1)

