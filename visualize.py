import matplotlib.pyplot as plt
import numpy as np
from reader2 import Runs, run_data, RunData
from typing import List  # Add this line to import List


def visualize_rssi_2d_matplotlib_all_runs(device: int):
    runs = Runs()
    num_runs = 4

    num_rows = (num_runs + 1) // 2
    num_cols = 2

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))

    for run in range(1, num_runs + 1):
        if num_runs > 1:
            ax = axes[(run - 1) // num_cols, (run - 1) % num_cols]
        else:
            ax = axes

        x, y, rssi = [], [], []
        for coord in runs.coords:
            x.append(coord[0])
            y.append(coord[1])
            rssi_val = runs.get_rssi(coord, device, run)
            rssi.append(rssi_val)

        x, y, rssi = np.array(x), np.array(y), np.array(rssi)

        sc = ax.scatter(x, y, c=rssi, cmap='viridis', alpha=0.7, label='RSSI Strength')
        ax.set_title(f"Run {run}")
        ax.set_xlabel('X-coordinate')
        ax.set_ylabel('Y-coordinate')
        ax.set_aspect('equal')
        ax.grid(True)

        if run == 1:
            ax.legend()

    plt.suptitle(f"RSSI Strength for Device {device}")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.colorbar(sc, ax=axes, orientation='vertical', label='RSSI Strength')
    plt.show()

if __name__ == "__main__":
    visualize_rssi_2d_matplotlib_all_runs(device=1)
    visualize_rssi_2d_matplotlib_all_runs(device=2)
    visualize_rssi_2d_matplotlib_all_runs(device=3)