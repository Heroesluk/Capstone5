from math import *
from typing import *
from reader import *

# input is 3 RSSI readings; output is position
def knn(input:(int,int,int), database:List[DatabaseEntry], k:int = 4) -> (float, float):
    
    distances:Dict[float, (float, float)] = {}

    for i in range(len(database)):
        R_A = database[i].RSSI_A - input[0]
        R_B = database[i].RSSI_B - input[1]
        R_C = database[i].RSSI_C - input[2]

        distances[sqrt(R_A**2 + R_B**2 + R_C**2)] = (database[i].x, database[i].y)

    distances = dict(sorted(distances.items()))

    k_nearest:List[float] = dict(list(distances.items())[:k])

    avarage_position_x:float = 0
    avarage_position_y:float = 0
    for i in k_nearest.values():
        avarage_position_x += i[0]
        avarage_position_y += i[1]
    avarage_position = (avarage_position_x/k, avarage_position_y/k)
 
    return avarage_position


# # can work poorly if error is big or path is close to another
# def distance_from_path_basic(position:(float,float), path_points:List[(float,float)]) -> float:
#     distance:float = 0.0
#     for point in path_points:
#         distance = max((point[0] - position[0])**2 (point[1] - position[1])**2, distance)
#     return sqrt(distance)

def distance_from_path_segment(x, y, x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    dot_product = (x - x1) * dx + (y - y1) * dy
    if dot_product < 0:
        return sqrt((x - x1) ** 2 + (y - y1) ** 2)
    if dot_product > dx ** 2 + dy ** 2:
        return sqrt((x - x2) ** 2 + (y - y2) ** 2)
    perp_distance = abs((x - x1) * dy - (y - y1) * dx) / sqrt(dx ** 2 + dy ** 2)
    return perp_distance

def distance_from_path(x, y, polygonal_chain):
    min_distance = float('inf')

    for i in range(len(polygonal_chain) - 1):
        x1, y1 = polygonal_chain[i]
        x2, y2 = polygonal_chain[i + 1]
        distance = distance_from_path_segment(x, y, x1, y1, x2, y2)
        min_distance = min(min_distance, distance)

    return min_distance

