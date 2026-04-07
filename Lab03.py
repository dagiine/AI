from collections import deque
import heapq

romania_map = {
    'Arad':      {'Zerind':75, 'Sibiu':140, 'Timisoara':118},
    'Zerind':    {'Arad':75, 'Oradea':71},
    'Oradea':    {'Zerind':71, 'Sibiu':151},
    'Sibiu':     {'Arad':140, 'Oradea':151, 'Fagaras':99, 'Rimnicu':80},
    'Timisoara': {'Arad':118, 'Lugoj':111},
    'Lugoj':     {'Timisoara':111, 'Mehadia':70},
    'Mehadia':   {'Lugoj':70, 'Drobeta':75},
    'Drobeta':   {'Mehadia':75, 'Craiova':120},
    'Craiova':   {'Drobeta':120, 'Rimnicu':146, 'Pitesti':138},
    'Rimnicu':   {'Sibiu':80, 'Craiova':146, 'Pitesti':97},
    'Fagaras':   {'Sibiu':99, 'Bucharest':211},
    'Pitesti':   {'Rimnicu':97, 'Craiova':138, 'Bucharest':101},
    'Bucharest': {'Fagaras':211, 'Pitesti':101}
}

def bfs(graph, start, goal):
    queue = deque([(start, [start], 0)])
    while queue:
        city, path, cost = queue.popleft()
        if city == goal:
            return path, cost
        for neighbor, distance in graph[city].items():
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor], cost + distance))

def dfs(graph, start, goal):
    stack = [(start, [start], 0)]
    while stack:
        city, path, cost = stack.pop()
        if city == goal:
            return path, cost
        for neighbor, distance in graph[city].items():
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor], cost + distance))

def ucs(graph, start, goal):
    queue = [(0, start, [start])]
    while queue:
        cost, city, path = heapq.heappop(queue)
        if city == goal:
            return path, cost
        for neighbor, distance in graph[city].items():
            if neighbor not in path:
                heapq.heappush(queue, (cost + distance, neighbor, path + [neighbor]))

results = {}
for name, search in [('BFS', bfs), ('DFS', dfs), ('UCS', ucs)]:
    path, cost = search(romania_map, 'Arad', 'Bucharest')
    results[name] = (path, cost)
    print(f"{name} Path: {path}")
    print(f"{name} Total Cost: {cost}\n")

least_cost = min(results, key=lambda n: results[n][1])
print(f"Least cost path: {least_cost} ({results[least_cost][1]})")