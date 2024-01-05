import numpy as np
from scipy.integrate import cumtrapz
from reader2 import run_data

def calculate_average_velocity_from_run_data(run_data_list):
    timestamps = np.array([float(data.timestamp) for data in run_data_list])
    x_mm = np.array([float(data.reference_x) for data in run_data_list])
    y_mm = np.array([float(data.reference_y) for data in run_data_list])

    # Convert millimeters to meters
    x = x_mm / 1000.0
    y = y_mm / 1000.0

    # Calculate the displacement (distance traveled) using cumulative trapezoidal integration
    displacement = cumtrapz(np.sqrt(np.diff(x)**2 + np.diff(y)**2), timestamps[:-1], initial=0)

    # Calculate the total distance traveled
    total_distance = displacement[-1]

    # Calculate the time duration
    time_duration = timestamps[-1] - timestamps[0]

    # Calculate the average velocity
    average_velocity = total_distance / time_duration

    return average_velocity

# Example usage:
run_data_list = run_data()
average_velocity = calculate_average_velocity_from_run_data(run_data_list)

print(f"Average velocity: {average_velocity} m/s")