import numpy as np
from reader2 import run_data

def calculate_average_velocity_from_run_data(run_data_list):
    timestamps = np.array([float(data.timestamp) for data in run_data_list])
    x_mm = np.array([float(data.reference_x) for data in run_data_list])
    y_mm = np.array([float(data.reference_y) for data in run_data_list])

    # Convert millimeters to meters
    x = x_mm / 1000.0
    y = y_mm / 1000.0

    # Calculate the differences in position
    dx = np.diff(x)
    dy = np.diff(y)

    # Sum all the differences in position to get the total displacement
    total_displacement = np.sum(np.sqrt(dx**2 + dy**2))

    # Calculate the time duration
    time_duration = timestamps[-1] - timestamps[0]

    # Calculate the average velocity
    average_velocity = total_displacement / time_duration

    # print total displacement and time duration
    print(f"Total displacement: {total_displacement} m")
    print(f"Time duration: {time_duration} s")

    return average_velocity

# Example usage:
run_data_list = run_data()
average_velocity = calculate_average_velocity_from_run_data(run_data_list)

print(f"Average velocity: {average_velocity} m/s")