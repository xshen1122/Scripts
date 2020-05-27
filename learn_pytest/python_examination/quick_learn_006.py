# quick_learn_006.py
# coding:utf-8
'''

BFS
'''
import Queue
def bfs(adj, start):
	visited = set()
	q=Queue.Queue()
	q.put(start)
	while not q.empty():
		print '.....',q.qsize()
		u=q.get()
		print u
		for v in adj.get(u,[]):
			# print ',xxxx',v
			if v not in visited:
				visited.add(v)
				q.put(v)

if __name__ == '__main__':
	graph={1:[4,2],2:[3,4],3:[4],4:[5]}
	bfs(graph,1)