from collections import deque
graph = [[] for _ in range(8)]
graph[1] = [2,3]
graph[2] = [4,5]
graph[4] = [5,7]
graph[3] = [4,6]
graph[5] = [7]
graph[6] = [7]


visited_list = []
queue = deque()

def bfs(start):

    #시작 노드에 대해서 할 일 처리
    print(start)
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        for adj_node in graph[node]:
            if adj_node not in visited_list:
                visited_list.append(adj_node)       # 방문했다고 표시
                print(adj_node)                     # 할 일 하기
                queue.append(adj_node)              # 순회시킬 노드로 등록하기

bfs(1)
