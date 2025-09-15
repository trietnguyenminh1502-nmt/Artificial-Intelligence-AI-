import tkinter as tk
from collections import deque
import heapq

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
    stack = [([] , 0)]
    while stack:
        state, depth = stack.pop()
        if len(state) == n:
            yield state
        elif depth < depth_limit:
            for col in range(n-1, -1, -1):
                if col not in state:
                    stack.append((state + [col], depth + 1))

def dls_n_rooks_steps(n=8, depth_limit=8):
    stack = [([] , 0)]
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
    else:
        algo_gen = iter([])

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

# Canvas
canvas_left = tk.Canvas(root, width=400, height=400)
canvas_left.grid(row=0, column=0, padx=10, pady=10)
draw_board(canvas_left)

canvas_right = tk.Canvas(root, width=400, height=400)
canvas_right.grid(row=0, column=2, padx=10, pady=10)
draw_board(canvas_right)

# Nhóm thuật toán ở giữa 2 bàn cờ
frame_algo = tk.LabelFrame(root, text="Thuật toán", padx=10, pady=10)
frame_algo.grid(row=0, column=1)

selected_algo = tk.StringVar(value="BFS")
tk.Radiobutton(frame_algo, text="BFS", variable=selected_algo, value="BFS").pack(anchor="w")
tk.Radiobutton(frame_algo, text="DFS", variable=selected_algo, value="DFS").pack(anchor="w")
tk.Radiobutton(frame_algo, text="UCS", variable=selected_algo, value="UCS").pack(anchor="w")
tk.Radiobutton(frame_algo, text="DLS", variable=selected_algo, value="DLS").pack(anchor="w")

# Nhóm điều khiển ở dưới
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

# Spinbox cho tốc độ và DLS limit
frame_spin = tk.Frame(root, pady=10)
frame_spin.grid(row=2, column=0, columnspan=3)

tk.Label(frame_spin, text="Tốc độ (ms):").pack(side="left", padx=4)
speed_var = tk.Spinbox(frame_spin, from_=10, to=2000, increment=10, width=6)
speed_var.pack(side="left", padx=4)
speed_var.delete(0, "end")
speed_var.insert(0, "200")

tk.Label(frame_spin, text="DLS limit:").pack(side="left", padx=10)
dls_var = tk.Spinbox(frame_spin, from_=1, to=8, width=4)
dls_var.pack(side="left", padx=4)
dls_var.delete(0, "end")
dls_var.insert(0, "8")

# State
algo_gen = iter([])
solutions = []
current_index = 0
running = False

root.mainloop()
