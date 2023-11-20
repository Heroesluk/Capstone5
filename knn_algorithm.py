from math import *
from typing import Dict
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


# can work poorly if error is big or path is close to another
def distance_from_path(position:(float,float), path_points:List[(float,float)]) -> float:
    distance:float = 0.0
    for point in path_points:
        distance = max((point[0] - position[0])**2 (point[1] - position[1])**2, distance)
    return sqrt(distance)
    
    