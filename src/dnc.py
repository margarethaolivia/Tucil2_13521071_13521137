import math

def euclideanDistance(p1, p2):
    """ Return euclidean distance of two points. \n
    len(p1) = len(p2)
    
    Args:
        p1 (List of double): first point
        p2 (List of double): second point

    Returns:
        double: euclidean distance

    """
    global DISTANCE_FUNCTION_CALLED
    DISTANCE_FUNCTION_CALLED += 1
    total = 0.0
    for i in range(len(p1)):
        total += (p1[i] - p2[i]) ** 2
    return math.sqrt(total)

def DnC(points, dimension):
    """ Return closest pair from points using divide and conquer

    Args:
        points (List of (int, List of double)): List of points indices and location

    Returns:
        double: closest pair distance
        int: index of first point in closest pair
        int: index of second point in closest pair
    
    """
    if len(points) == 1:
        return None, None, None
    if len(points) == 2:
        return euclideanDistance(points[0][1], points[1][1]), points[0][0], points[1][0]
    
    # Divide points
    points.sort(key=lambda x: x[1][dimension])
    mid = len(points)//2
    l_points = points[:mid]
    r_points = points[mid:]
    midpoint = l_points[-1][1][dimension]

    # Conquer each part
    nextdimension = (dimension + 1) % len(points[0][1])
    l_best, l_index1, l_index2 = DnC(l_points, nextdimension)
    r_best, r_index1, r_index2 = DnC(r_points, nextdimension)

    # Merge both part
    if l_best != None and (r_best == None or l_best < r_best):
        best, index1, index2 = l_best, l_index1, l_index2
    else:
        best, index1, index2 = r_best, r_index1, r_index2
    # l_points.sort(key=lambda x:x[1][nextdimension])
    # r_points.sort(key=lambda x:x[1][nextdimension])

    l_mid = []
    for i in range(len(l_points)):
        if midpoint - l_points[i][1][dimension] < best:
            l_mid.append(l_points[i])
            
    r_mid = []
    for i in range(len(r_points)):
        if r_points[i][1][dimension] - midpoint < best:
            r_mid.append(r_points[i])
            
    r_start = 0
    for x in l_mid:
        while r_start + 1 < len(r_mid) and x[1][nextdimension] - r_mid[r_start][1][nextdimension] > best:
            r_start += 1
        for j in range(r_start, len(r_mid)):
            if r_mid[j][1][nextdimension] - x[1][nextdimension] > best:
                break
            dist = euclideanDistance(x[1], r_mid[j][1])
            if dist < best:
                best, index1, index2 = dist, x[0], r_mid[j][0]


    return best, index1, index2

    

def getClosestPair(points):
    """ Return closest pair, distance and indices

    Args:
        points (List of (int, List of double)): List of points indices and location

    Returns:
        double: closest pair distance
        int: index of first point in closest pair
        int: index of second point in closest pair
        int: number of distance function called

    """
    global DISTANCE_FUNCTION_CALLED
    DISTANCE_FUNCTION_CALLED = 0
    closestPair = DnC(points.copy(), 0)
    return closestPair[0], closestPair[1], closestPair[2], DISTANCE_FUNCTION_CALLED

# if __name__ == "__main__":
#     dist, idx1, idx2, called = getClosestPair([(0, [0, 0, 0]), (1, [1, 2, 2]), (2, [10, 10, 10]), (3, [1, 1, 1])])
#     print(f"dist = {dist}, idx1 = {idx1}, idx2 = {idx2}, called = {called}")