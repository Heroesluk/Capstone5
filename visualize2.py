import matplotlib.pyplot as plt
import numpy as np
from reader2 import Runs, run_data, RunData


def visualize_rssi_and_acceleration_2d_matplotlib_all_devices():
    runs = Runs()
    run_number = 1  # Display only the first run

    num_devices = 3
    num_rows = 1
    num_cols = num_devices

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5))

    for device in range(1, num_devices + 1):
        if num_devices > 1:
            ax = axes[device - 1]
        else:
            ax = axes

        x, y, rssi = [], [], []
        acceleration_x, acceleration_y = [], []

        for coord in runs.coords:
            x.append(coord[0])
            y.append(coord[1])
            rssi.append(runs.get_rssi(coord, device, run_number))
            acceleration_x.append(runs.acceleration_x[runs.coords.index(coord)])
            acceleration_y.append(runs.acceleration_y[runs.coords.index(coord)])

        x, y, rssi, acceleration_x, acceleration_y = (
            np.array(x),
            np.array(y),
            np.array(rssi),
            np.array(acceleration_x, dtype=float),
            np.array(acceleration_y, dtype=float),
        )

        # Plotting RSSI
        sc = ax.scatter(x, y, c=rssi, cmap='viridis', alpha=0.7, label='RSSI')

        # Plotting Acceleration Vectors
        ax.quiver(x, y, acceleration_x, acceleration_y, color='red', scale=5000, label='Acceleration Vectors')

        ax.set_title(f"Device {device}")
        ax.set_xlabel('X-coordinate')
        ax.set_ylabel('Y-coordinate')
        ax.set_aspect('equal')
        ax.grid(True)
        ax.legend()

    plt.suptitle(f"RSSI Strength and Acceleration Vectors for First Run (All Devices)")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


if __name__ == "__main__":
    visualize_rssi_and_acceleration_2d_matplotlib_all_devices()
