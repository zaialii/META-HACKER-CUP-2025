# scaling_solution.py
# Meta "Scaling Up" problem - guaranteed valid general solution

def solve():
    with open("input.txt", "r") as f:
        data = list(map(int, f.read().strip().split()))
    t = data[0]
    idx = 1
    output_lines = []

    for case in range(1, t + 1):
        N, A, B = data[idx], data[idx + 1], data[idx + 2]
        idx += 3

        seq = []

        # Strategy:
        # 1. First N multipliers keep product <= A
        # 2. Final product must equal B

        # Start with product = 1
        first_part = [1] * (N - 1)
        # Choose last of first N so product = min(A, B)
        first_part.append(min(A, B))

        current = 1
        for x in first_part:
            current *= x

        # remaining N multipliers
        remaining = []
        needed = B // current
        remainder = B % current

        # If B not divisible, adjust
        if remainder != 0:
            needed = B  # fallback
            first_part = [1] * N
            current = 1

        # Fill last N multipliers
        if N == 1:
            remaining = [needed]
        else:
            remaining = [1] * (N - 1) + [needed]

        seq = first_part + remaining

        output_lines.append("Case #{}: {}".format(case, " ".join(map(str, seq))))

    with open("output.txt", "w") as f:
        f.write("\n".join(output_lines))


if __name__ == "__main__":
    solve()
