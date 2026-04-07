import heapq

graph = { 
    "Arad":           [("Zerind", 75), ("Timisoara", 118), ("Sibiu", 140)],  
    "Zerind":         [("Arad", 75), ("Oradea", 71)], 
    "Oradea":         [("Zerind", 71), ("Sibiu", 151)],
    "Timisoara":      [("Arad", 118), ("Lugoj", 111)],
    "Lugoj":          [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia":        [("Lugoj", 70), ("Dobreta", 75)],
    "Dobreta":        [("Mehadia", 75), ("Craiova", 120)],
    "Craiova":        [("Dobreta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Sibiu":          [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
    "Fagaras":        [("Sibiu", 99), ("Bucharest", 211)],
    "Pitesti":        [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest":      [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)],
    "Giurgiu":        [("Bucharest", 90)],
    "Urziceni":       [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)],
    "Hirsova":        [("Urziceni", 98), ("Eforie", 86)],
    "Eforie":         [("Hirsova", 86)],
    "Vaslui":         [("Urziceni", 142), ("Lasi", 92)],
    "Lasi":           [("Vaslui", 92), ("Neamt", 87)],
    "Neamt":          [("Lasi", 87)],
}

heuristic = {
    "Arad": 366, "Bucharest": 0, "Craiova": 160, "Dobreta": 242,
    "Eforie": 161, "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151,
    "Lasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
    "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193, "Sibiu": 253,
    "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374,
}

def greedy(start, goal):  
    current = start  
    path    = [start]  
    visited = set([start])  

    while current != goal: 
        best_city, best_h = None, float("inf")  

        for city, dist in graph[current]:
            if city not in visited and heuristic[city] < best_h: 
                best_h = heuristic[city]
                best_city = city 

        if best_city is None: 
            return None, 0  

        visited.add(best_city) 
        path.append(best_city)  
        current = best_city 

        cost = 0
        for i in range(len(path) - 1):
            for neighbor, dist in graph[path[i]]:
                if neighbor == path[i+1]:
                    cost += dist
                    break 

    return path, cost 

def astar(start, goal):
    counter = 0
    heap = [(heuristic[start], counter, 0, [start])]
    visited = set()

    while heap:
        f, counter, g, path = heapq.heappop(heap)
        current = path[-1]

        if current == goal:
            return path, g

        if current in visited:
            continue

        visited.add(current)

        for neighbor, dist in graph[current]:
            if neighbor not in visited:
                new_g = g + dist
                counter += 1
                
                new_f = new_g + heuristic[neighbor]
                new_path = path + [neighbor]
                heapq.heappush(heap, (new_f, counter, new_g, new_path))

    return None, 0

start, goal = "Arad", "Bucharest"

greedy_path, greedy_cost = greedy(start, goal) 
astar_path,  astar_cost  = astar(start, goal)  

print(f"Greedy Path: {greedy_path}")
print(f"Greedy Total Cost: {greedy_cost}")  
print() 

print(f"A* Path: {astar_path}")  
print(f"A* Total Cost: {astar_cost}")  
print()

results = {"Greedy": greedy_cost, "A*": astar_cost}  
best = min(results, key=results.get)  
print(f"Least cost path: {best} ({results[best]})")