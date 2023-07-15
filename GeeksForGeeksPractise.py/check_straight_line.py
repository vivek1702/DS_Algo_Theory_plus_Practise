# check if the coordinate in straight line

def checkStraightLine(coordinates):

#@actual method 

    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    dx = x1-x0 
    dy = y1 - y0 

    for x,y in coordinates[2:]:
        #formula is 
        if (x-x0) * dy != (y-y0) * dx:
            return False
    return True




# coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

# coordinates = [[2,1],[4,2],[6,3]]    # failing for this third test case
print(checkStraightLine(coordinates))