import math

def closest_pair(points):
    def dist(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def brute_force(points, n):
        min_dist = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                d = dist(points[i], points[j])
                if d < min_dist:
                    min_dist = d
        return min_dist

    def strip_closest(strip, size, d):
        min_dist = d
        for i in range(size):
            j = i + 1
            while j < size and (strip[j][1] - strip[i][1]) < min_dist:
                min_dist = dist(strip[i], strip[j])
                j += 1
        return min_dist

    def closest_util(points_x, points_y, n):
        if n <= 3:
            return brute_force(points_x, n)

        mid = n // 2
        mid_point = points_x[mid]
        points_y_left = [point for point in points_y if point[0] <= mid_point[0]]
        points_y_right = [point for point in points_y if point[0] > mid_point[0]]

        dl = closest_util(points_x[:mid], points_y_left, mid)
        dr = closest_util(points_x[mid:], points_y_right, n - mid)
        d = min(dl, dr)

        strip = [point for point in points_y if abs(point[0] - mid_point[0]) < d]
        return min(d, strip_closest(strip, len(strip), d))

    points.sort(key=lambda x: x[0])
    points_x = sorted(points, key=lambda x: x[0])
    points_y = sorted(points, key=lambda x: x[1])

    return closest_util(points_x, points_y, len(points))
