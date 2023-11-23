import matplotlib.pyplot as plt
import numpy as np
from reader2 import Runs, run_data

def visualize_rssi_2d_matplotlib_all_runs(device: int):
    runs = Runs()
    num_runs = 4  # number of runs

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
            rssi.append(runs.get_rssi(coord, device, run))

        x, y, rssi = np.array(x), np.array(y), np.array(rssi)

        ax.scatter(x, y, c=rssi, cmap='viridis', alpha=0.7)
        ax.set_title(f"Run {run}")
        ax.set_xlabel('X-coordinate')
        ax.set_ylabel('Y-coordinate')
        ax.set_aspect('equal')
        ax.grid(True)

    plt.suptitle(f"RSSI Strength for Device {device}")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    visualize_rssi_2d_matplotlib_all_runs(device=1)
    visualize_rssi_2d_matplotlib_all_runs(device=2)
    visualize_rssi_2d_matplotlib_all_runs(device=3)
