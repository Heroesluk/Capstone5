import csv


class RunData:
    def __init__(self, row):
        self.index = row[0]
        self.unnamed_0 = row[1]
        self.version = row[2]
        self.alive = row[3]
        self.tagId = row[4]
        self.success = row[5]
        self.timestamp = row[6]
        self.gyro_x = row[7]
        self.gyro_y = row[8]
        self.gyro_z = row[9]
        self.magnetic_x = row[10]
        self.magnetic_y = row[11]
        self.magnetic_z = row[12]
        self.quaternion_x = row[13]
        self.quaternion_y = row[14]
        self.quaternion_z = row[15]
        self.quaternion_w = row[16]
        self.linearAcceleration_x = row[17]
        self.linearAcceleration_y = row[18]
        self.linearAcceleration_z = row[19]
        self.pressure = row[20]
        self.maxLinearAcceleration = row[21]
        self.acceleration_x = row[22]
        self.acceleration_y = row[23]
        self.acceleration_z = row[24]
        self.orientation_yaw = row[25]
        self.orientation_roll = row[26]
        self.orientation_pitch = row[27]
        self.metrics_latency = row[28]
        self.metrics_rates_update = row[29]
        self.metrics_rates_success = row[30]
        self.reference_x = row[31]
        self.bran = row[32]


def run_data():
    file_path = 'przejazd_01 - Sheet1.csv'

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        return [RunData(row) for row in reader]




class Runs():
    def __init__(self):
        self.coords = [(2, 0), (3, 0), (3.707, 0.292), (4, 1), (4, 2), (4.292, 2.707), (5, 3), (6, 3), (6, 4), (5, 4),
                       (4, 4),
                       (3, 4), (2, 4), (1, 3.866), (0.134, 3), (0, 2), (0.134, 1), (1, 0.134)]
        self.rssi = [[[-45, -47, -48, -56, -58, -58, -57, -64, -55, -61, -57, -63, -50, -52, -51, -44, -54, -36],
                      [-39, -48, -51, -55, -54, -45, -53, -63, -58, -61, -56, -62, -47, -48, -52, -41, -50, -36],
                      [-48, -45, -52, -54, -58, -56, -57, -64, -50, -53, -59, -55, -54, -51, -39, -44, -44, -41],
                      [-44, -48, -54, -50, -55, -59, -54, -58, -58, -57, -54, -52, -50, -49, -46, -40, -45, -43]],

                     [[-57, -47, -46, -50, -42, -58, -47, -52, -55, -49, -48, -51, -52, -58, -58, -54, -58, -58],
                      [-60, -53, -51, -43, -54, -54, -39, -52, -51, -53, -51, -49, -53, -53, -51, -54, -56, -51],
                      [-50, -46, -41, -49, -44, -46, -49, -48, -44, -49, -39, -55, -54, -56, -61, -55, -59, -50],
                      [-48, -55, -48, -45, -42, -47, -41, -40, -36, -49, -53, -56, -53, -58, -56, -53, -58, -50]],

                     [[-56, -60, -59, -53, -54, -48, -50, -63, -57, -53, -48, -56, -41, -45, -37, -48, -42, -52],
                      [-59, -54, -50, -49, -52, -49, -55, -56, -58, -53, -56, -58, -47, -40, -34, -48, -51, -52],
                      [-54, -56, -56, -49, -52, -56, -50, -55, -52, -56, -54, -51, -47, -40, -50, -46, -45, -46],
                      [-58, -56, -50, -50, -52, -58, -61, -60, -58, -50, -56, -42, -49, -40, -42, -48, -50, -46]]]

    # returns value based on specified device (1-3), lap(1-4) and point (x,y) list
    # ie getRSSI((2,0),1,1) should yield -45
    def getRSSI(self, xy: tuple, device: int, lap: int):
        if xy not in self.coords or device > 3 or device < 1 or lap > 4 or lap < 1:
            raise Exception("Incorrect Input")

        return self.rssi[device - 1][lap - 1][self.coords.index(xy)]
