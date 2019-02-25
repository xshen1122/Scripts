# test_ch06_1.py
# coding: utf-8
'''
graph
'''

'''
show the whole graph. dict in dict
1. 将图形转换为数据结构，这里是转换成了3个字典。
字典1 - graph，代表了整个图（在运算过程中不变）
字典2 - costs， 代表了路线值（在运算过程中变化）
字典3 - parents， 代表了父节点（在运算过程中变化）

2. 找路线的思路
找最短路线，并且会更新costs和parents表。

3. 通过循环来做，知道节点为Null

'''
graph = {}
graph['start'] = {}
graph['start']['a']=5
graph['start']['b']=2
graph['a'] = {}
graph['a']['c']=4
graph['a']['d']=2
graph['b']={}
graph['b']['a']=8
graph['b']['d']=7
graph['c']={}
graph['c']['d']=6
graph['c']['fin']=3
graph['d']={}
graph['d']['fin']=1
graph['fin']={}

# infinity = float('inf')
infinity = 1000000000

costs ={}
costs['a']=5
costs['b']=2
costs['c']=infinity
costs['d']=infinity
costs['fin']=infinity

parents = {}
parents['a']='start'
parents['b']='start'
parents['c']=None
parents['d']=None
parents['fin']=None


processed = []

#=======================================
def find_lowest_cost_node(costs):
	lowest_cost = 1000000000
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost<lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node


node = find_lowest_cost_node(costs)
route_list = []
neighbors = graph[node]
while node is not None :
	route_list.append(node)
	cost = costs[node]
	
	
	neighbors = graph[node]
	
	for n in neighbors.keys():
		new_cost=cost + neighbors[n]
		if costs[n] > new_cost:
			costs[n]=new_cost
			parents[n]=node
	processed.append(node)
	node = find_lowest_cost_node(costs)
	
print costs
print parents
print 'min route length if ', costs['fin']
for 
#we can see the route : b->a->fin

# total_route = 0
# next = 'start'
# for item in route_list:
# 	print next,'->',item
# 	total_route += graph[next][item]
# 	next = item

# print total_route
	

