from collections import deque
import time


def print_jug_visual(x, y):
    """Fungsi untuk menggambar visualisasi ember secara sederhana"""
    print(f"  [ 5L ]     [ 3L ]")
    # Visualisasi ember 5L (kapasitas 5) dan 3L (kapasitas 3)
    for i in range(5, 0, -1):
        # Ember 5L
        water_5 = "████" if i <= x else "    "
        # Ember 3L (hanya setinggi 3 baris)
        water_3 = "████" if i <= y and i <= 3 else ("    " if i <= 3 else "")

        line_5 = f"|{water_5}|" if i <= 5 else "      "
        line_3 = f"|{water_3}|" if i <= 3 else "      "

        if i <= 3:
            print(f"  {line_5}     {line_3}")
        else:
            print(f"  {line_5}")
    print(f"  +----+     +----+")
    print(f"   ({x}L)       ({y}L)\n")


def solve_water_jug_bfs():
    CAP_5L = 5
    CAP_3L = 3
    initial_state = (0, 0)

    queue = deque([(initial_state, [initial_state])])
    visited = set([initial_state])

    while queue:
        (x, y), path = queue.popleft()

        if x == 4:
            return path

        possible_actions = [
            (CAP_5L, y),
            (x, CAP_3L),
            (0, y),
            (x, 0),
            (x - min(x, CAP_3L - y), y + min(x, CAP_3L - y)),
            (x + min(y, CAP_5L - x), y - min(y, CAP_5L - x)),
        ]

        for next_state in possible_actions:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None


# Run program
solution_path = solve_water_jug_bfs()

if solution_path:
    # Warna teks ANSI escape codes
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    print(f"{CYAN}========================================{RESET}")
    print(f"{CYAN}   WATER JUG PROBLEM SOLVER (BFS)       {RESET}")
    print(f"{CYAN}========================================{RESET}")
    print(
        f"{YELLOW}Target: Mendapatkan tepat 4 Liter di ember 5L{RESET}\n"
    )
    print(f"Total Langkah Optimal: {len(solution_path) - 1} Langkah\n")
    print("-" * 40)

    for step, state in enumerate(solution_path):
        print(f"Langkah ke-{step}:")
        print_jug_visual(state[0], state[1])

        if step < len(solution_path) - 1:
            print(
                f"{GREEN}---------------- ( Lanjut ) ----------------{RESET}"
            )
            # Opsional: beri jeda 1 detik per langkah ala animasi
            time.sleep(0.8)

    print(f"{CYAN}========================================{RESET}")
    print(f"{GREEN}   SOLUSI SELESAI! BERHASIL DAPAT 4L!   {RESET}")
    print(f"{CYAN}========================================{RESET}")
else:
    print("Solusi tidak ditemukan.")