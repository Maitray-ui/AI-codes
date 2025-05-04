from queue import PriorityQueue

start = (0, 0)
goal = (2, 2)
grid = [[0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]]  # walls in middle row

# Manhattan Distance as Heuristic
def h(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            print("Path:", path[::-1])
            return

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < 3 and 0 <= neighbor[1] < 3 and grid[neighbor[0]][neighbor[1]] == 0:
                temp_g = g_score[current] + 1
                if temp_g < g_score.get(neighbor, float('inf')):
                    g_score[neighbor] = temp_g
                    f = temp_g + h(neighbor, goal)
                    open_set.put((f, neighbor))
                    came_from[neighbor] = current

astar(start, goal)
