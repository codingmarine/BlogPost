INF = float("inf")
graph = [[(2,5),(3,4),(4,11)],[(1,5),(4,3),(5,7)],[(1,4),(4,3)],[(1,11),(2,3),(3,3),(5,3)],[(2,7),(4,3)]]
distance = [INF]*6
visited = [False]*6
#변수초기화

start = int(input())
#시작 노드 결정

distance[start] = 0
visited[start] = True
#시작노드의 값 초기화 

for node in graph[start-1]:
    distance[node[0]]=node[1]
# 시작노드의 인접노드 값 업데이트 

for i in range(1,len(graph)):
    temp = INF
    now = 0
    for j in range(1,len(graph)):
        if distance[j] < temp and not visited[j]:
            temp = distance[j]
            now = j
 #====현재 방문하지 않은 값들 중 최단 거리인 노드를 결정====
    visited[now] = True
    for x in graph[now-1]:
        distance[x[0]] = min(distance[x[0]],distance[now]+x[1])
#결정된 노드에 대해서 최단거리 업데이트

print(distance,visited)
# 출력 : [inf, 0, 5, 4, 7, 10] [True, True, True, True, True, False]

