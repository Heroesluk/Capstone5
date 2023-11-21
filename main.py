import statistics

from plotly.subplots import make_subplots

from reader import loadData
import plotly.express as px
import plotly.graph_objects as go

import plotly.express as px

import pandas as pd

from reader2 import Runs, run_data

# Calling DataFrame constructor after zipping
# both lists, with columns specified


runs = Runs()

run_data = run_data()
df = px.data.gapminder().query("continent=='Europe'")


def what_is_this_exactly():
    data = runs.coords

    df2 = pd.DataFrame(data, columns=['x', 'y'])

    fig = px.scatter(df2, x="x", y="y", color_discrete_sequence=['red'], title="Points from runs 1-4 table where rssi "
                                                                               "is measured")
    fig.update_traces(marker={'size': 50})

    return fig


def reference():
    x = [run.reference_x for run in run_data]
    y = [run.reference_y for run in run_data]

    data = {
        "x": x,
        "y": y
    }

    df = pd.DataFrame(data)
    fig = px.scatter(df, x="x", y="y")

    return fig


def getMedianValues(device):
    median_rssi = []
    for cords in runs.coords:
        m = statistics.median(
            [runs.get_rssi(cords, device, 1), runs.get_rssi(cords, device, 2), runs.get_rssi(cords, device, 3),
             runs.get_rssi(cords, device, 4)])
        median_rssi.append(m)

    return median_rssi


def data_frame_for_xy_rssi_mapping(device: int, lap: int):
    run1_dev_1 = [runs.get_rssi(cords, device, lap) for cords in runs.coords]
    x_y_rssi1 = [(f"device: {device}, lap: {lap}", runs.coords[i][0], runs.coords[i][1], run1_dev_1[i]) for i in
                 range(len(run1_dev_1))]
    return pd.DataFrame(x_y_rssi1, columns=['run', 'x', 'y', 'rssi'])


def rssi_strenght_for_device(device):
    df1 = data_frame_for_xy_rssi_mapping(device, 1)
    df2 = data_frame_for_xy_rssi_mapping(device, 2)
    df3 = data_frame_for_xy_rssi_mapping(device, 3)
    df4 = data_frame_for_xy_rssi_mapping(device, 4)

    df3 = pd.concat([df1, df2, df3, df4])

    return px.line_3d(df3, x="x", y="y", z="rssi", color='run')


def rssi_median_strenght_for_access_point():
    run1_dev_1 = getMedianValues(1)
    x_y_rssi1 = [(f"device: {1}", runs.coords[i][0], runs.coords[i][1], run1_dev_1[i]) for i in
                 range(len(run1_dev_1))]
    df1 = pd.DataFrame(x_y_rssi1, columns=['run', 'x', 'y', 'rssi'])

    run1_dev_2 = getMedianValues(2)
    x_y_rssi1 = [(f"device: {2}", runs.coords[i][0], runs.coords[i][1], run1_dev_2[i]) for i in
                 range(len(run1_dev_1))]
    df2 = pd.DataFrame(x_y_rssi1, columns=['run', 'x', 'y', 'rssi'])

    run1_dev_3 = getMedianValues(3)
    x_y_rssi1 = [(f"device: {3}", runs.coords[i][0], runs.coords[i][1], run1_dev_3[i]) for i in
                 range(len(run1_dev_1))]
    df3 = pd.DataFrame(x_y_rssi1, columns=['run', 'x', 'y', 'rssi'])

    df4 = pd.concat([df1, df2, df3])

    return px.line_3d(df4, x="x", y="y", z="rssi", color='run')


def rssi_strenght_for_access_points():
    df1 = data_frame_for_xy_rssi_mapping(1, 1)
    df2 = data_frame_for_xy_rssi_mapping(2, 1)
    df3 = data_frame_for_xy_rssi_mapping(3, 1)

    df3 = pd.concat([df1, df2, df3])

    return px.line_3d(df3, x="x", y="y", z="rssi", color='run')




# fig1 = what_is_this_exactly()
# fig2 = reference()
# fig2.show()
# fig = go.Figure(data=fig1.data + fig2.data)


r = rssi_strenght_for_device(1)
r.show()
