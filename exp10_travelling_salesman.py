from itertools import permutations

def travelling_salesman(distance):
    n = len(distance)

    start_city = 0
    cities = list(range(1, n))

    minimum_cost = float("inf")
    best_route = None

    for perm in permutations(cities):
        route = [start_city] + list(perm) + [start_city]

        current_cost = 0

        for i in range(len(route) - 1):
            current_cost += distance[route[i]][route[i + 1]]

        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_route = route

    return best_route, minimum_cost


# Distance matrix
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Main program
route, cost = travelling_salesman(distance)

print("Best Route:")

for city in route:
    print(city, end=" ")

print("\nMinimum Distance:", cost)