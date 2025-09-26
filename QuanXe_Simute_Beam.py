import tkinter as tk
from collections import deque
import heapq
import random

# -----------------------
# Thuật toán
# -----------------------

def bfs_n_rooks_all(n=8):
    queue = deque([[]])
    while queue:
        state = queue.popleft()
        if len(state) == n:
            yield state
        else:
            for col in range(n):
                if col not in state:
                    queue.append(state + [col])

def bfs_n_rooks_steps(n=8):
    queue = deque([[]])
    while queue:
        state = queue.popleft()
        if state:
            yield state
        if len(state) == n:
            continue
        for col in range(n):
            if col not in state:
                queue.append(state + [col])

def dfs_n_rooks_all(n=8):
    stack = [[]]
    while stack:
        state = stack.pop()
        if len(state) == n:
            yield state
        else:
            for col in range(n-1, -1, -1):
                if col not in state:
                    stack.append(state + [col])

def dfs_n_rooks_steps(n=8):
    stack = [[]]
    while stack:
        state = stack.pop()
        if state:
            yield state
        if len(state) == n:
            continue
        for col in range(n-1, -1, -1):
            if col not in state:
                stack.append(state + [col])

def ucs_n_rooks_all(n=8):
    heap = []
    heapq.heappush(heap, (0, []))
    while heap:
        cost, state = heapq.heappop(heap)
        if len(state) == n:
            yield state
        else:
            for col in range(n):
                if col not in state:
                    new = state + [col]
                    heapq.heappush(heap, (len(new), new))

def ucs_n_rooks_steps(n=8):
    heap = []
    heapq.heappush(heap, (0, []))
    visited = set()
    while heap:
        cost, state = heapq.heappop(heap)
        t = tuple(state)
        if t in visited:
            continue
        visited.add(t)
        if state:
            yield state
        if len(state) == n:
            continue
        for col in range(n):
            if col not in state:
                new = state + [col]
                heapq.heappush(heap, (len(new), new))

def dls_n_rooks_all(n=8, depth_limit=8):
    stack = [([], 0)]
    while stack:
        state, depth = stack.pop()
        if len(state) == n:
            yield state
        elif depth < depth_limit:
            for col in range(n-1, -1, -1):
                if col not in state:
                    stack.append((state + [col], depth + 1))

def dls_n_rooks_steps(n=8, depth_limit=8):
    stack = [([], 0)]
    while stack:
        state, depth = stack.pop()
        if state:
            yield state
        if len(state) == n:
            continue
        if depth < depth_limit:
            for col in range(n-1, -1, -1):
                if col not in state:
                    stack.append((state + [col], depth + 1))

def ids_n_rooks_all(n=8):
    for limit in range(1, n+1):
        yield from dls_n_rooks_all(n, depth_limit=limit)

def ids_n_rooks_steps(n=8):
    for limit in range(1, n+1):
        yield from dls_n_rooks_steps(n, depth_limit=limit)

def greedy_n_rooks_all(n=8):
    heap = []
    heapq.heappush(heap, (n, []))
    while heap:
        h, state = heapq.heappop(heap)
        if len(state) == n:
            yield state
        else:
            for col in range(n):
                if col not in state:
                    new = state + [col]
                    heuristic = n - len(new)
                    heapq.heappush(heap, (heuristic, new))

def greedy_n_rooks_steps(n=8):
    heap = []
    heapq.heappush(heap, (n, []))
    visited = set()
    while heap:
        h, state = heapq.heappop(heap)
        t = tuple(state)
        if t in visited:
            continue
        visited.add(t)
        if state:
            yield state
        if len(state) == n:
            continue
        for col in range(n):
            if col not in state:
                new = state + [col]
                heuristic = n - len(new)
                heapq.heappush(heap, (heuristic, new))

def astar_n_rooks_all(n=8):
    heap = []
    heapq.heappush(heap, (0+n, 0, []))  # f, g, state
    while heap:
        f, g, state = heapq.heappop(heap)
        if len(state) == n:
            yield state
        else:
            for col in range(n):
                if col not in state:
                    new = state + [col]
                    g2 = g + 1
                    h2 = n - len(new)
                    f2 = g2 + h2
                    heapq.heappush(heap, (f2, g2, new))

def astar_n_rooks_steps(n=8):
    heap = []
    heapq.heappush(heap, (0+n, 0, []))
    visited = set()
    while heap:
        f, g, state = heapq.heappop(heap)
        t = tuple(state)
        if t in visited:
            continue
        visited.add(t)
        if state:
            yield state
        if len(state) == n:
            continue
        for col in range(n):
            if col not in state:
                new = state + [col]
                g2 = g + 1
                h2 = n - len(new)
                f2 = g2 + h2
                heapq.heappush(heap, (f2, g2, new))

# -----------------------
# Hill Climbing
# -----------------------
def hill_n_rooks_all(n=8):
    state = []
    while len(state) < n:
        best = None
        best_h = float("inf")
        for col in range(n):
            if col not in state:
                new = state + [col]
                h = n - len(new)
                if h < best_h:
                    best = new
                    best_h = h
        if best is None:
            break
        state = best
    if len(state) == n:
        yield state

def hill_n_rooks_steps(n=8):
    state = []
    while len(state) < n:
        yield state
        best = None
        best_h = float("inf")
        for col in range(n):
            if col not in state:
                new = state + [col]
                h = n - len(new)
                if h < best_h:
                    best = new
                    best_h = h
        if best is None:
            break
        state = best
    yield state

# -----------------------
# Genetic Algorithm
# -----------------------
def ga_n_rooks_all(n=8, population_size=20, generations=50):
    population = [random.sample(range(n), n) for _ in range(population_size)]
    for _ in range(generations):
        for indiv in population:
            yield indiv
        selected = random.sample(population, population_size // 2)
        children = []
        while len(children) < population_size // 2:
            p1, p2 = random.sample(selected, 2)
            cut = random.randint(1, n-1)
            child = p1[:cut] + [c for c in p2 if c not in p1[:cut]]
            children.append(child)
        for child in children:
            if random.random() < 0.2:
                i, j = random.sample(range(n), 2)
                child[i], child[j] = child[j], child[i]
        population = selected + children

def ga_n_rooks_steps(n=8, population_size=20, generations=50):
    population = [random.sample(range(n), n) for _ in range(population_size)]
    for _ in range(generations):
        for indiv in population:
            yield indiv
        selected = random.sample(population, population_size // 2)
        children = []
        while len(children) < population_size // 2:
            p1, p2 = random.sample(selected, 2)
            cut = random.randint(1, n-1)
            child = p1[:cut] + [c for c in p2 if c not in p1[:cut]]
            children.append(child)
        for child in children:
            if random.random() < 0.2:
                i, j = random.sample(range(n), 2)
                child[i], child[j] = child[j], child[i]
        population = selected + children

# -----------------------
# Simulated Annealing
# -----------------------
def sa_n_rooks_all(n=8, max_steps=1000, start_temp=100, cooling=0.95):
    def cost(state):
        return n - len(set(state))  # số xung đột

    state = random.sample(range(n), n)
    T = start_temp
    for step in range(max_steps):
        yield state
        if cost(state) == 0:
            break
        new_state = state[:]
        i, j = random.sample(range(n), 2)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        dE = cost(state) - cost(new_state)
        if dE > 0 or random.random() < pow(2.718, dE / T):
            state = new_state
        T *= cooling

def sa_n_rooks_steps(n=8, max_steps=1000, start_temp=100, cooling=0.95):
    def cost(state):
        return n - len(set(state))

    state = random.sample(range(n), n)
    T = start_temp
    for step in range(max_steps):
        yield state
        if cost(state) == 0:
            break
        new_state = state[:]
        i, j = random.sample(range(n), 2)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        dE = cost(state) - cost(new_state)
        if dE > 0 or random.random() < pow(2.718, dE / T):
            state = new_state
        T *= cooling

# -----------------------
# Beam Search
# -----------------------
def beam_n_rooks_all(n=8, beam_width=3):
    beam = [[]]
    while beam:
        new_beam = []
        for state in beam:
            if len(state) == n:
                yield state
            else:
                for col in range(n):
                    if col not in state:
                        new_state = state + [col]
                        h = n - len(new_state)
                        new_beam.append((h, new_state))
        new_beam.sort(key=lambda x: x[0])
        beam = [s for _, s in new_beam[:beam_width]]

def beam_n_rooks_steps(n=8, beam_width=3):
    beam = [[]]
    while beam:
        new_beam = []
        for state in beam:
            yield state
            if len(state) == n:
                continue
            for col in range(n):
                if col not in state:
                    new_state = state + [col]
                    h = n - len(new_state)
                    new_beam.append((h, new_state))
        new_beam.sort(key=lambda x: x[0])
        beam = [s for _, s in new_beam[:beam_width]]

# -----------------------
# Vẽ bàn cờ
# -----------------------
def draw_board(canvas, solution=None):
    canvas.delete("all")
    n = 8
    cell_size = 50
    for r in range(n):
        for c in range(n):
            x1 = c * cell_size
            y1 = r * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            color = "white" if (r + c) % 2 == 0 else "gray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
    if solution:
        for r, c in enumerate(solution):
            x = c * cell_size + cell_size // 2
            y = r * cell_size + cell_size // 2
            canvas.create_text(x, y, text="♖", font=("Arial", 28), fill="black")

# -----------------------
# Step-by-step
# -----------------------
def run_step_by_step():
    global algo_gen, running
    if not running:
        return
    try:
        state = next(algo_gen)
        draw_board(canvas_right, state)
        delay = int(speed_var.get())
        root.after(delay, run_step_by_step)
    except StopIteration:
        running = False
        return

def start_algorithm():
    global algo_gen, solutions, current_index, running
    algo = selected_algo.get()
    n = 8
    running = True
    current_index = 0

    if algo == "BFS":
        algo_gen = bfs_n_rooks_steps(n)
        solutions = list(bfs_n_rooks_all(n))
    elif algo == "DFS":
        algo_gen = dfs_n_rooks_steps(n)
        solutions = list(dfs_n_rooks_all(n))
    elif algo == "UCS":
        algo_gen = ucs_n_rooks_steps(n)
        solutions = list(ucs_n_rooks_all(n))
    elif algo == "DLS":
        limit = int(dls_var.get())
        algo_gen = dls_n_rooks_steps(n, depth_limit=limit)
        solutions = list(dls_n_rooks_all(n, depth_limit=limit))
    elif algo == "IDS":
        algo_gen = ids_n_rooks_steps(n)
        solutions = list(ids_n_rooks_all(n))
    elif algo == "Greedy":
        algo_gen = greedy_n_rooks_steps(n)
        solutions = list(greedy_n_rooks_all(n))
    elif algo == "A*":
        algo_gen = astar_n_rooks_steps(n)
        solutions = list(astar_n_rooks_all(n))
    elif algo == "Hill":
        algo_gen = hill_n_rooks_steps(n)
        solutions = list(hill_n_rooks_all(n))
    elif algo == "GA":
        algo_gen = ga_n_rooks_steps(n)
        solutions = list(ga_n_rooks_all(n))
    elif algo == "SA":
        algo_gen = sa_n_rooks_steps(n)
        solutions = list(sa_n_rooks_all(n))
    elif algo == "Beam":
        algo_gen = beam_n_rooks_steps(n)
        solutions = list(beam_n_rooks_all(n))
    else:
        algo_gen = iter([])
        solutions = []

    if not hasattr(algo_gen, "__next__"):
        algo_gen = iter(algo_gen)

    run_step_by_step()

def stop_algorithm():
    global running
    running = False

def reset_board():
    global current_index, running
    running = False
    current_index = 0
    draw_board(canvas_right)

def next_solution():
    global current_index, solutions, running
    running = False
    if not solutions:
        return
    current_index = (current_index + 1) % len(solutions)
    draw_board(canvas_right, solutions[current_index])

# -----------------------
# UI
# -----------------------
root = tk.Tk()
root.title("8 Quân Xe")

canvas_left = tk.Canvas(root, width=400, height=400)
canvas_left.grid(row=0, column=0, padx=10, pady=10)
draw_board(canvas_left)

canvas_right = tk.Canvas(root, width=400, height=400)
canvas_right.grid(row=0, column=2, padx=10, pady=10)
draw_board(canvas_right)

frame_algo = tk.LabelFrame(root, text="Thuật toán", padx=10, pady=10)
frame_algo.grid(row=0, column=1)

selected_algo = tk.StringVar(value="BFS")
tk.Radiobutton(frame_algo, text="BFS", variable=selected_algo, value="BFS").pack(anchor="w")
tk.Radiobutton(frame_algo, text="DFS", variable=selected_algo, value="DFS").pack(anchor="w")
tk.Radiobutton(frame_algo, text="UCS", variable=selected_algo, value="UCS").pack(anchor="w")
tk.Radiobutton(frame_algo, text="DLS", variable=selected_algo, value="DLS").pack(anchor="w")
tk.Radiobutton(frame_algo, text="IDS", variable=selected_algo, value="IDS").pack(anchor="w")
tk.Radiobutton(frame_algo, text="Greedy", variable=selected_algo, value="Greedy").pack(anchor="w")
tk.Radiobutton(frame_algo, text="A*", variable=selected_algo, value="A*").pack(anchor="w")
tk.Radiobutton(frame_algo, text="Hill Climbing", variable=selected_algo, value="Hill").pack(anchor="w")
tk.Radiobutton(frame_algo, text="Genetic", variable=selected_algo, value="GA").pack(anchor="w")
tk.Radiobutton(frame_algo, text="Simulated Annealing", variable=selected_algo, value="SA").pack(anchor="w")
tk.Radiobutton(frame_algo, text="Beam Search", variable=selected_algo, value="Beam").pack(anchor="w")

frame_action = tk.Frame(root, pady=10)
frame_action.grid(row=1, column=0, columnspan=3)

btn_font = ("Arial", 12, "bold")
btn_start = tk.Button(frame_action, text="Bắt đầu", command=start_algorithm, font=btn_font, width=10)
btn_start.pack(side="left", padx=6, pady=6)
btn_stop = tk.Button(frame_action, text="Stop", command=stop_algorithm, font=btn_font, width=10)
btn_stop.pack(side="left", padx=6, pady=6)
btn_reset = tk.Button(frame_action, text="Reset", command=reset_board, font=btn_font, width=10)
btn_reset.pack(side="left", padx=6, pady=6)
btn_next = tk.Button(frame_action, text="Phương án tiếp theo", command=next_solution, font=btn_font, width=18)
btn_next.pack(side="left", padx=6, pady=6)

frame_spin = tk.Frame(root, pady=10)
frame_spin.grid(row=2, column=0, columnspan=3)

tk.Label(frame_spin, text="Tốc độ (ms):").pack(side="left", padx=6)
speed_var = tk.StringVar(value="500")
speed_spin = tk.Spinbox(frame_spin, from_=50, to=2000, textvariable=speed_var, width=6)
speed_spin.pack(side="left", padx=6)

tk.Label(frame_spin, text="Giới hạn DLS:").pack(side="left", padx=6)
dls_var = tk.StringVar(value="8")
dls_spin = tk.Spinbox(frame_spin, from_=1, to=8, textvariable=dls_var, width=4)
dls_spin.pack(side="left", padx=6)

root.mainloop()














