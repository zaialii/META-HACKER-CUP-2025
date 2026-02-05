
def check_height(L, vals):
    n = len(vals)
    if n == 0:
        return True

    got_low = (vals[0] <= L)
    for i in range(n - 1):
        if abs(vals[i+1] - vals[i]) > L:
            if not got_low:
                return False
            got_low = (vals[i+1] <= L)
        else:
            if vals[i+1] <= L:
                got_low = True
    return got_low


def shortest_ladder(arr):
    if not arr:
        return 0
    hi = max(max(arr), max(abs(arr[i+1]-arr[i]) for i in range(len(arr)-1)) if len(arr)>1 else 0)
    lo = 0

    while lo < hi:
        mid = (lo + hi)//2
        if check_height(mid, arr):
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
   
    try:
        data = open("input.txt","r").read().strip().split()
    except:
        return
    if not data: return

    t = int(data[0])
    idx = 1
    out = []
    for cs in range(1, t+1):
        n = int(data[idx]); idx += 1
        vals = list(map(int, data[idx:idx+n])); idx += n
        ans = shortest_ladder(vals)
        out.append("Case #{}: {}".format(cs, ans))
    try:
        open("output.txt","w").write("\n".join(out))
    except:
        pass


if __name__ == "__main__":
    main()
