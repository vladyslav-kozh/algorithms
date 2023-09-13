import matplotlib.pyplot as plt

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def convex_hull(points):
    n = len(points)
    if n < 3:
        return points

    hull = []
    leftmost = min(points, key=lambda x: x[0])

    p = points.index(leftmost)
    q = None

    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for r in range(n):
            if orientation(points[p], points[r], points[q]) == 2:
                q = r
        p = q

        if p == points.index(leftmost):
            break

    return hull
