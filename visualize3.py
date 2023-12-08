import matplotlib.pyplot as plt
import numpy as np
from reader2 import Runs, run_data, RunData

def visualize_acceleration_vectors(run_data_list):
    num_rows = 1
    num_cols = 1

    fig, ax = plt.subplots(num_rows, num_cols, figsize=(8, 8))

    x, y, acceleration_x, acceleration_y = [], [], [], []

    for run_data in run_data_list:
        x.append(run_data.reference_x)
        y.append(run_data.reference_y)
        acceleration_x.append(run_data.acceleration_x)
        acceleration_y.append(run_data.acceleration_y)

    x, y, acceleration_x, acceleration_y = (
        np.array(x),
        np.array(y),
        np.array(acceleration_x, dtype=float),
        np.array(acceleration_y, dtype=float),
    )

    ax.quiver(x, y, acceleration_x, acceleration_y, color='red', scale=5000, label='Acceleration Vectors')

    ax.set_title("Acceleration Vectors")
    ax.set_xlabel('X-coordinate')
    ax.set_ylabel('Y-coordinate')
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()

    plt.show()

def integrate_gyroscope_z_angle(gyro_z_data):
    time_interval = 0.0012
    angle_z = np.cumsum(gyro_z_data) * time_interval
    return angle_z

def visualize_gyroscope_z_angle(run_data_list):
    num_rows = 1
    num_cols = 1

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(8, 8))

    x, y, gyro_z = [], [], []

    for run_data in run_data_list:
        x.append(run_data.reference_x)
        y.append(run_data.reference_y)
        gyro_z.append(run_data.gyro_z)

    x, y, gyro_z = (
        np.array(x),
        np.array(y),
        np.array(gyro_z, dtype=float),
    )

    angle_z = integrate_gyroscope_z_angle(gyro_z)

    # Subtract the initial angle correctly
    initial_angle_z = angle_z[0]
    angle_z -= initial_angle_z

    ax = axes

    ax.quiver(x, y, np.cos(angle_z), -np.sin(angle_z),
              scale=10, label='Gyroscope Z')

    ax.set_title('Gyroscope Z Angle Vectors (Subtracting initial angle, 0.0012 time interval)')
    ax.set_xlabel('X-coordinate')
    ax.set_ylabel('Y-coordinate')
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()

    plt.tight_layout()
    plt.show()

def visualize_yaw(run_data_list):
    num_rows = 1
    num_cols = 1

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(8, 8))

    x, y, yaw_angles = [], [], []

    for run_data in run_data_list:
        x.append(run_data.reference_x)
        y.append(run_data.reference_y)
        yaw_angles.append(run_data.orientation_yaw)

    x, y, yaw_angles = (
        np.array(x),
        np.array(y),
        np.array(yaw_angles, dtype=float),
    )

    initial_angle = yaw_angles[0]
    yaw_angles -= initial_angle

    ax = axes

    ax.quiver(x, y, np.cos(yaw_angles), np.sin(yaw_angles),
              scale=10, label='Yaw')

    ax.set_title('Yaw Angle Vectors (Subtracting Initial Angle)')
    ax.set_xlabel('X-coordinate')
    ax.set_ylabel('Y-coordinate')
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()

    plt.tight_layout()
    plt.show()

def visualize_magnetometer(run_data_list):
    x, y, magnetic_x, magnetic_y, yaw_angles = [], [], [], [], []

    for run_data in run_data_list:
        x.append(run_data.reference_x)
        y.append(run_data.reference_y)
        magnetic_x.append(run_data.magnetic_x)
        magnetic_y.append(run_data.magnetic_y)
        yaw_angles.append(run_data.orientation_yaw)

    x, y, magnetic_x, magnetic_y, yaw_angles = (
        np.array(x),
        np.array(y),
        np.array(magnetic_x, dtype=float),
        np.array(magnetic_y, dtype=float),
        np.array(yaw_angles, dtype=float),
    )

    initial_yaw = yaw_angles[0]
    yaw_angles -= initial_yaw

    fig1, ax1 = plt.subplots(figsize=(8, 8))
    ax1.quiver(x, y, magnetic_x, magnetic_y,
               color='orange', scale=100, label='Unmodified Magnetometer')
    ax1.set_title('Unmodified Magnetometer Vectors')
    ax1.set_xlabel('X-coordinate')
    ax1.set_ylabel('Y-coordinate')
    ax1.set_aspect('equal')
    ax1.grid(True)
    ax1.legend()
    plt.show()

    rotated_magnetic_x = magnetic_x * np.cos(yaw_angles) - magnetic_y * np.sin(yaw_angles)
    rotated_magnetic_y = magnetic_x * np.sin(yaw_angles) + magnetic_y * np.cos(yaw_angles)

    fig2, ax2 = plt.subplots(figsize=(8, 8))
    ax2.quiver(x, y, rotated_magnetic_x, rotated_magnetic_y,
               color='purple', scale=100, label='Rotated Magnetometer')
    ax2.set_title('Magnetometer Vectors with Yaw Rotation')
    ax2.set_xlabel('X-coordinate')
    ax2.set_ylabel('Y-coordinate')
    ax2.set_aspect('equal')
    ax2.grid(True)
    ax2.legend()
    plt.show()

    mask = ((yaw_angles >= np.pi / 2) & (yaw_angles <= 3 * np.pi / 2)) | \
           ((yaw_angles <= -np.pi / 2) & (yaw_angles >= -3 * np.pi / 2))
    magnetic_x[mask] *= -1
    magnetic_y[mask] *= -1

    fig3, ax3 = plt.subplots(figsize=(8, 8))
    ax3.quiver(x, y, magnetic_x, magnetic_y,
               color='purple', scale=100, label='Combined Magnetometer (Yaw Adjusted)')
    ax3.set_title('Combined Magnetometer Vectors with Yaw Adjustment')
    ax3.set_xlabel('X-coordinate')
    ax3.set_ylabel('Y-coordinate')
    ax3.set_aspect('equal')
    ax3.grid(True)
    ax3.legend()
    plt.show()

if __name__ == "__main__":
    run_data_list = run_data()
    visualize_acceleration_vectors(run_data_list)
    visualize_magnetometer(run_data_list)
    visualize_yaw(run_data_list)
    visualize_gyroscope_z_angle(run_data_list)
