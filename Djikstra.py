
graph=[[999,10,999,999,100],[10,999,50,999,999],[999,50,999,20,10],[999,999,20,999,60],[100,999,10,60,999]]
v=5
def print1(d):
	print("Vertex \tDistance from Source")
	for i in range(v):
		print(f"{i}\t{d[i]}")
def min1(a,b):
	m=999
	for i in range(v):
		if (a[i]<m)and(b[i]==0):
			m=a[i]
			p=i
	return p
def dijkstra(src):
	dist = [999,999,999,999,999]
	dist[src] = 0
	b=[0,0,0,0,0]
	for i in range(v):
		x = min1(dist,b)
		b[x] = 1
		for y in range(v):
			if graph[x][y] > 0 and b[y] == 0 and dist[y] > dist[x] + graph[x][y]:
				dist[y] = dist[x] + graph[x][y]

	print1(dist)

dijkstra(0)


