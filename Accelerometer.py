from pykalman import KalmanFilter
from reader2 import *


# Get the list of RunData instances
run_data_list = run_data()

# Loop through the linearAcceleration_x column
linear_acceleration_x_values = [data.linearAcceleration_x for data in run_data_list]
linear_acceleration_y_values = [data.linearAcceleration_y for data in run_data_list]

merged_values = []

# Loop through the arrays and push values to the merged array
for x, y in zip(linear_acceleration_x_values, linear_acceleration_y_values):
    val = [float(x), float(y)]
    merged_values.append(val)

print(merged_values)

kf = KalmanFilter(initial_state_mean=0, n_dim_obs=2)

# measurements = [merged_values]
#
# a = kf.em(measurements).smooth([[2, 0], [2, 1], [2, 2]])[0]

# print(a)
