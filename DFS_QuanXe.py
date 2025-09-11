import tkinter as tk
N = 8  # số quân xe
#hàm dfs
def dfs(row, cols, solution, solutions):
    if row == N:
        solutions.append(solution[:])
        return

    for col in range(N):
        if col not in cols:
            solution.append((row, col))
            dfs(row + 1, cols | {col}, solution, solutions)
            solution.pop()

def solve_rooks():
    solutions = []
    dfs(0, set(), [], solutions)
    return solutions

# tính chi phí:
#- Nếu đặt xe vào (row, col), số cột trống cho các hàng còn lại giảm đi.
#- Càng hạn chế → chi phí càng cao.
def cost(row, col, remaining_rows, used_cols):
    total_free = 0
    for r in remaining_rows:
        for c in range(N):
            if c not in used_cols and c != col:
                total_free += 1

    reduced_free = total_free - len(remaining_rows)
    return max(1, (N*N - reduced_free) // 10)

#Hàm giao diện
class RookGUI:
    def __init__(self, root, solutions):
        self.root = root
        self.root.title("Bài toán 8 quân xe - DFS + Cost")
        self.solutions = solutions
        self.index = 0

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.btn_next = tk.Button(root, text="Next Solution", command=self.show_next)
        self.btn_next.pack(pady=10)

        self.label_cost = tk.Label(root, text="Tổng chi phí: 0", font=("Arial", 12))
        self.label_cost.pack()

        self.draw_board()
        self.show_next()

    def draw_board(self):
        self.canvas.delete("all")
        cell_size = 50
        for i in range(N):
            for j in range(N):
                color = "white" if (i + j) % 2 == 0 else "gray"
                self.canvas.create_rectangle(j*cell_size, i*cell_size,
                                             (j+1)*cell_size, (i+1)*cell_size,
                                             fill=color)

    def show_next(self):
        if self.index >= len(self.solutions):
            self.index = 0
        solution = self.solutions[self.index]
        self.index += 1

        self.draw_board()
        cell_size = 50
        total_cost = 0

        for k, (row, col) in enumerate(solution):
            # vẽ quân xe
            self.canvas.create_text(col*cell_size+25, row*cell_size+25,
                                    text="♖", font=("Arial", 24), fill="red")

            # tính chi phí
            remaining_rows = list(range(row+1, N))
            used_cols = {c for _, c in solution[:k]}
            total_cost += cost(row, col, remaining_rows, used_cols)

        self.label_cost.config(text=f"Tổng chi phí: {total_cost}")

#hàm chính
if __name__ == "__main__":
    solutions = solve_rooks()
    print(f"Tìm được {len(solutions)} lời giải cho bài toán 8 quân xe.")

    root = tk.Tk()
    gui = RookGUI(root, solutions)
    root.mainloop()
