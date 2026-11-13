def min_max(x: list[float]) -> list[float]:
    
    m = max(x)
    n = min(x)
    if m == n:
        return 0.0
    t = []

    for i in range(len(x)):
        x[i] = (x[i]-n) / (m - n)
    return x
