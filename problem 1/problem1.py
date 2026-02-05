def solve():
    # Open input file
    with open("input.txt", "r") as infile:
        t = int(infile.readline().strip())  # number of test cases
        results = []

        for case in range(1, t + 1):
            n = int(infile.readline().strip())
            A = list(map(int, infile.readline().strip().split()))

            # Calculate minimum required ladder height
            max_diff = 0
            for i in range(n - 1):
                diff = abs(A[i + 1] - A[i])
                max_diff = max(max_diff, diff)

            results.append(f"Case #{case}: {max_diff}")

    # Write output to file
    with open("output.txt", "w") as outfile:
        outfile.write("\n".join(results))


# Run the function
if __name__ == "__main__":
    solve()
