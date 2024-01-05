import numpy as np
import matplotlib.pyplot as plt
from reader2 import run_data

def rotate_vector(x, y, angle):
    """Rotate a vector (x, y) by the specified angle."""
    x_rotated = x * np.cos(angle) - y * np.sin(angle)
    y_rotated = x * np.sin(angle) + y * np.cos(angle)
    return x_rotated, y_rotated

def calculate_velocity_from_run_data(run_data_list):
    timestamps = np.array([float(data.timestamp) for data in run_data_list])
    acceleration_x = np.array([float(data.acceleration_x) for data in run_data_list], dtype=float)
    acceleration_y = np.array([float(data.acceleration_y) for data in run_data_list], dtype=float)
    quaternion_w = np.array([float(data.quaternion_w) for data in run_data_list])
    quaternion_x = np.array([float(data.quaternion_x) for data in run_data_list])
    quaternion_y = np.array([float(data.quaternion_y) for data in run_data_list])
    quaternion_z = np.array([float(data.quaternion_z) for data in run_data_list])

    # Calculate yaw angles
    yaw_angles = np.arctan2(2 * (quaternion_w * quaternion_z + quaternion_x * quaternion_y),
                            1 - 2 * (quaternion_y**2 + quaternion_z**2))

    # Rotate vectors based on yaw angle
    rotated_acceleration_x, rotated_acceleration_y = rotate_vector(acceleration_x, acceleration_y, yaw_angles)

    # Convert timestamps to seconds
    timestamps_seconds = timestamps - timestamps[0]

    # Integrate rotated acceleration to obtain velocity
    velocity_x = np.cumsum(rotated_acceleration_x) * 0.012
    velocity_y = np.cumsum(rotated_acceleration_y) * 0.012

    # Calculate the magnitude of velocity
    velocity_magnitude = np.sqrt(velocity_x**2 + velocity_y**2) / 100

    # Print average velocity in m/s
    avg_velocity = np.mean(velocity_magnitude)
    print('Average velocity: {:.2f} m/s'.format(avg_velocity))

    # Plot velocity over time
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps_seconds, velocity_magnitude, label='Velocity Magnitude')
    plt.xlabel('Timestamp')
    plt.ylabel('Velocity (m/s)')
    plt.title('Device Velocity Over Time After Yaw Rotation')
    plt.legend()

    # Add text annotation for average velocity
    plt.text(0.5, 0.9, f'Average Velocity: {avg_velocity:.2f} m/s', transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', alpha=0.5))

    plt.grid(True)
    plt.show()

# Example usage:
run_data_list = run_data()
calculate_velocity_from_run_data(run_data_list)
