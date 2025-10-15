# search_algorithms.py
from collections import deque
import heapq
import random
import math

# -----------------------
# BFS
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

# -----------------------
# DFS
# -----------------------
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

# -----------------------
# UCS (uniform cost, here cost = depth)
# -----------------------
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

# -----------------------
# DLS
# -----------------------
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

# -----------------------
# IDS
# -----------------------
def ids_n_rooks_all(n=8):
    for limit in range(1, n+1):
        yield from dls_n_rooks_all(n, depth_limit=limit)

def ids_n_rooks_steps(n=8):
    for limit in range(1, n+1):
        yield from dls_n_rooks_steps(n, depth_limit=limit)

# -----------------------
# Greedy (simple heuristic)
# -----------------------
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

# -----------------------
# A*
# -----------------------
def astar_n_rooks_all(n=8):
    heap = []
    heapq.heappush(heap, (0 + n, 0, []))  # f, g, state
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
    heapq.heappush(heap, (0 + n, 0, []))
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
# Hill Climbing (greedy build)
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
# Genetic Algorithm (simple)
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
def sa_n_rooks_all(n=8, max_steps=1000, start_temp=100.0, cooling=0.95):
    def cost(state):
        # số xung đột = n - số cột khác nhau (vì mỗi hàng có 1 con)
        return n - len(set(state))

    state = random.sample(range(n), n)
    T = float(start_temp)
    for step in range(max_steps):
        yield state
        if cost(state) == 0:
            break
        new_state = state[:]
        i, j = random.sample(range(n), 2)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        dE = cost(state) - cost(new_state)
        if dE > 0 or random.random() < math.exp(dE / T):
            state = new_state
        T *= cooling

def sa_n_rooks_steps(n=8, max_steps=1000, start_temp=100.0, cooling=0.95):
    def cost(state):
        return n - len(set(state))

    state = random.sample(range(n), n)
    T = float(start_temp)
    for step in range(max_steps):
        yield state
        if cost(state) == 0:
            break
        new_state = state[:]
        i, j = random.sample(range(n), 2)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        dE = cost(state) - cost(new_state)
        if dE > 0 or random.random() < math.exp(dE / T):
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
# AND-OR Search
# -----------------------
def and_or_n_rooks_all(n=8):
    """
    Trả về tất cả kế hoạch giải quyết (dạng AND-OR tree).
    Ở đây ta mô phỏng đơn giản: 
    - OR node: chọn một vị trí đặt xe tiếp theo
    - AND node: phải đặt được tất cả quân còn lại
    """
    def and_or(state):
        if len(state) == n:
            return [state]  # đã đủ n quân
        plans = []
        for col in range(n):
            if col not in state:
                # OR: chọn col
                subplans = and_or(state + [col])
                for sp in subplans:
                    plans.append(sp)
        return plans
    
    return and_or([])


def and_or_n_rooks_steps(n=8):
    """
    Duyệt step-by-step cho GUI. 
    Sinh ra trạng thái trung gian để vẽ.
    """
    stack = [([], "OR")]
    while stack:
        state, node_type = stack.pop()
        if state:
            yield state  # cho GUI hiển thị
        if len(state) == n:
            continue
        if node_type == "OR":
            # chọn 1 hành động => sinh AND node
            for col in range(n-1, -1, -1):
                if col not in state:
                    stack.append((state + [col], "AND"))
        else:
            # AND: tất cả kết quả con phải thỏa
            for col in range(n-1, -1, -1):
                if col not in state:
                    stack.append((state + [col], "OR"))
                    