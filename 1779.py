def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
    validPoints = False
    dist = {}
    i = 0

    for x1, y1 in points:
        if x1 == x or y1 == y:
            validPoints = True
            dist[i] = int(abs(x1 - x) + abs(y1 - y))
        i += 1

    minDist = float("inf")
    index = -1

    for key, val in dist.items():
        if val < minDist:
            minDist = val
            index = key

    return -1 if not validPoints else index
