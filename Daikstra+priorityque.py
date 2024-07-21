import heapq
INF = float("inf")
graph = [[],[(2,5),(3,4),(4,11)],[(1,5),(4,3),(5,7)],[(1,4),(4,3)],[(1,11),(2,3),(3,3),(5,3)],[(2,7),(4,3)]]
distance = [INF]*6
#변수초기화

start = int(input())

myque = []
distance[start] = 0
heapq.heappush(myque,(0,start))
#시작노드를 추가
while myque:
    d,now = heapq.heappop(myque)
    if distance[now] < d: #방문여부 검사
        continue
    for i in graph[now]: # 인접노드들에 대해 반복문 수행
        temp = d + i[1] # d = 현재까지의 거리, i[1] = 다음 노드까지의 거리
        if temp < distance[i[0]]: # 현재 저장된 값보다 작은 경우
            distance[i[0]] = temp # distance 테이블을 갱신하고
            heapq.heappush(myque,(temp,i[0],1)) # heapq에 추가함
print(distance)
# 출력 : [inf, 0, 5, 4, 7, 10] 
