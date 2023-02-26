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

def DnC(points):
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
    
    dimension = 0
    
    # Divide points
    points.sort(key=lambda x: x[1][dimension])
    mid = len(points)//2
    l_points = points[:mid]
    r_points = points[mid:]

    # Conquer each part
    l_best, l_index1, l_index2 = DnC(l_points)
    r_best, r_index1, r_index2 = DnC(r_points)

    # Merge both part
    if l_best != None and (r_best == None or l_best < r_best):
        best, index1, index2 = l_best, l_index1, l_index2
    else:
        best, index1, index2 = r_best, r_index1, r_index2

    midpoint = l_points[-1][1][dimension]
    l_start = len(l_points)
    for i in range(len(l_points)):
        if midpoint - l_points[i][1][dimension] < best:
            l_start = i
            break
    
    r_end = len(r_points)
    for i in range(len(r_points)):
        if r_points[i][1][dimension] - midpoint > best:
            r_end = i
            break
    
    for i in range(l_start, len(l_points)):
        for j in range(0, r_end):
            dist = euclideanDistance(l_points[i][1], r_points[j][1])
            if dist < best:
                best, index1, index2 = dist, l_points[i][0], r_points[j][0]

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
    closestPair = DnC(points.copy())
    return closestPair[0], closestPair[1], closestPair[2], DISTANCE_FUNCTION_CALLED

# if __name__ == "__main__":
#     dist, idx1, idx2, called = getClosestPair([(0, [0, 0, 0]), (1, [1, 2, 2]), (2, [10, 10, 10]), (3, [1, 1, 1])])
#     print(f"dist = {dist}, idx1 = {idx1}, idx2 = {idx2}, called = {called}")