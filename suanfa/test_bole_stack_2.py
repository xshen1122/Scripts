# test_bole_stack_2.py
# coding: utf-8
'''
maze = [[0]*7 for _ in range(5+2)]
产生一个7×7的二维数组，且每个元素均为0
每一个为1的点的坐标存在walls内。
di，dj是方向，分别有4个方向，[(0,-1),(0,1),(-1,0),(1,0)]
这种枚举法只适用于迷宫格子较少的情况。
'''
def init_Maze():
	maze = [[0]*7 for _ in range(5+2)]
	walls = [(1,3),(2,1),(2,5),(3,3),(3,4),(4,2),(5,4)]
	for i in range(7):
		maze[i][0]=maze[i][-1]=1
		maze[0][i]=maze[-1][i]=1
	for item in walls:
		maze[item[0]][item[1]]=1
	return maze
def path(maze, start, end):
	i, j = start
	ei, ej = end
	stack = [(i,j)]
	maze[i][j]=1
	while stack:
		i,j = stack[-1]
		if (i,j)==(ei,ej):
			break
		for di, dj in [(0,-1),(0,1),(-1,0),(1,0)]:
			if maze[i+di][j+dj]==0:
				maze[i+di][j+dj]=1
				stack.append((i+di, j+dj))
				break
		else:
			stack.pop()
	return stack



if __name__ == '__main__':
	result = path(init_Maze(),start =(1,1),end=(5,5))
	print result