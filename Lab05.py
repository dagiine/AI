import random
import math

nodes = ['Ulaanbaatar', 'Erdenet', 'Darkhan', 'Choibalsan', 'Moron', 'Khovd', 'Olgii', 'Bayankhongor', 'Dalanzadgad', 'Altai']

edges = [
    ('Ulaanbaatar', 'Erdenet', 231),
    ('Ulaanbaatar', 'Darkhan', 142),
    ('Ulaanbaatar', 'Choibalsan', 198),
    ('Ulaanbaatar', 'Moron', 96),
    ('Ulaanbaatar', 'Khovd', 199),
    ('Ulaanbaatar', 'Olgii', 218),
    ('Ulaanbaatar', 'Bayankhongor', 210),
    ('Ulaanbaatar', 'Dalanzadgad', 140),
    ('Ulaanbaatar', 'Altai', 297),
    ('Erdenet', 'Darkhan', 290),
    ('Erdenet', 'Choibalsan', 185),
    ('Erdenet', 'Moron', 253),
    ('Erdenet', 'Khovd', 262),
    ('Erdenet', 'Olgii', 242),
    ('Erdenet', 'Bayankhongor', 264),
    ('Erdenet', 'Dalanzadgad', 246),
    ('Erdenet', 'Altai', 186),
    ('Darkhan', 'Choibalsan', 151),
    ('Darkhan', 'Moron', 93),
    ('Darkhan', 'Khovd', 85),
    ('Darkhan', 'Olgii', 229),
    ('Darkhan', 'Bayankhongor', 157),
    ('Darkhan', 'Dalanzadgad', 221),
    ('Darkhan', 'Altai', 152),
    ('Choibalsan', 'Moron', 56),
    ('Choibalsan', 'Khovd', 137),
    ('Choibalsan', 'Olgii', 99),
    ('Choibalsan', 'Bayankhongor', 130),
    ('Choibalsan', 'Dalanzadgad', 126),
    ('Choibalsan', 'Altai', 55),
    ('Moron', 'Khovd', 111),
    ('Moron', 'Olgii', 299),
    ('Moron', 'Bayankhongor', 290),
    ('Moron', 'Dalanzadgad', 260),
    ('Moron', 'Altai', 231),
    ('Khovd', 'Olgii', 150),
    ('Khovd', 'Bayankhongor', 115),
    ('Khovd', 'Dalanzadgad', 296),
    ('Khovd', 'Altai', 130),
    ('Olgii', 'Bayankhongor', 232),
    ('Olgii', 'Dalanzadgad', 299),
    ('Olgii', 'Altai', 229),
    ('Bayankhongor', 'Dalanzadgad', 195),
    ('Bayankhongor', 'Altai', 262),
    ('Dalanzadgad', 'Altai', 263),
]

n = len(nodes)

dist = []
i = 0
while i < n:
    dist.append([0] * n)
    i = i + 1

for edge in edges:
    city_a = edge[0]
    city_b = edge[1]
    km = edge[2]
    i = nodes.index(city_a)
    j = nodes.index(city_b)
    dist[i][j] = km
    dist[j][i] = km

def tour_length(tour):
    total = 0
    i = 0
    while i < n:
        curr = tour[i]
        next = tour[(i + 1) % n]  
        total = total + dist[curr][next]
        i = i + 1
    return total

def random_tour(start):
    others = []
    i = 0
    while i < n:
        if i != start:
            others.append(i)
        i = i + 1

    random.shuffle(others)

    tour = [start] + others
    return tour

def swap(tour, i, k):
    new_tour = []

    # 1. i hurtelh heseg
    pos = 0
    while pos < i:
        new_tour.append(tour[pos])
        pos = pos + 1

    # 2. i-k urvuugaar
    pos = k
    while pos >= i:
        new_tour.append(tour[pos])
        pos = pos - 1

    # 3. k hoish heseg
    pos = k + 1
    while pos < n:
        new_tour.append(tour[pos])
        pos = pos + 1

    return new_tour

def hill_climbing(start):
    tour = random_tour(start)
    length = tour_length(tour)
    improved = True

    while improved:
        improved = False

        i = 0
        while i < n - 1:
            k = i + 1
            while k < n:
                new_tour = swap(tour, i, k)
                new_length = tour_length(new_tour)

                if new_length < length:
                    tour = new_tour
                    length = new_length
                    improved = True

                k = k + 1
            i = i + 1

    return tour, length

def simulated_annealing(start):
    tour = random_tour(start)
    length = tour_length(tour)
    best_tour = new = tour.copy()       
    best_length = length

    temp = 5000.0  
    cooling  = 0.9995  
    min_temp = 0.01    

    while temp > min_temp:
        i = random.randint(0, n - 1)
        k = random.randint(0, n - 1)

        if i > k:
            i, k = k, i

        if i == k:
            temp = temp * cooling
            continue

        new_tour = swap(tour, i, k)
        new_length = tour_length(new_tour)
        delta = new_length - length

        if delta < 0:
            tour = new_tour
            length = new_length
        else:
            probability = math.exp(-delta / temp)
            if random.random() < probability:
                tour = new_tour
                length = new_length

        if length < best_length:
            best_tour = tour.copy()
            best_length = length

        temp = temp * cooling

    return best_tour, best_length


start_index = nodes.index('Ulaanbaatar')

print("HILL CLIMBING:")
hc_tour, hc_length = hill_climbing(start_index)
print([nodes[i] for i in hc_tour])
print("Niit zam:", hc_length, "km")
print()

print("SIMULATED ANNEALING:")
sa_tour, sa_length = simulated_annealing(start_index)
print([nodes[i] for i in sa_tour])
print("Niit zam:", sa_length, "km")