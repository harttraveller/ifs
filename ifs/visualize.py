import plotly.graph_objects as go
from ifs.resources.minimal_layout import minimal_template


class Animate:
    # for anything involving animation
    # - point placement
    # - moving through slice (2D slide of 3D, or 3D slice of 4D)
    # - modifying parameters
    pass


class Histogram:
    def __init__(self) -> None:
        pass

    def v1D(self):
        pass


class ColorHistogram:
    def __init__(self) -> None:
        pass

    def v2D(self):
        pass

class

class Scatterplot:
    def __init__(self) -> None:
        pass

    def v2D(self):
        pass

    def v3D(self):
        pass


class ColorScatterplot:
    def __init__(self) -> None:
        pass

    def v3D(self):
        pass

    def v4D(self):
        pass


class ColorScatterplot:
    pass


class Visualize:
    # for any non-animated visualizations
    # - 1D (histogram)
    # - 2D (2D scatterplot, 1D histogram as slice)
    # - 3D (3D scatterplot, 2D scatterplot + color, 2D scatterplot + size, 2D scatterplot as slice, 1D histogram + color as slice)
    # - 4D (3D scatterplot + color, 3D scatterplot + size, 3D scatterplot as slice, 2D scatterplot + color + size, 2D)
    # - 5D (3D scatterplot + color + size, 3D scatterplot + color + slice, 3D scatterplot + size + slice)
    def __init__(self) -> None:
        pass


def v1D(points, save):  # histogram
    pass


def v2D(points, save):  # 2D scatterplot
    pass


def v3D(points, save):
    pass


def v4D(points, save):
    a, b, c, d = list(zip(*points))
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=d,
                y=b,
                z=c,
                mode="markers",
                marker=dict(
                    size=1.5,
                    color=a,  # set color equal to a variable
                    colorscale="Viridis",  # one of plotly colorscales
                    showscale=False,
                    reversescale=True,
                ),
                hoverinfo="skip",
            )
        ]
    )
    fig.update_layout(
        template=minimal_template,
        autosize=False,
        width=480,
        height=480,
        margin=dict(l=10, r=10, b=10, t=10, pad=0),
    )
    camera = dict(
        up=dict(x=0, y=0, z=1), center=dict(x=0, y=0, z=0), eye=dict(x=0, y=2.5, z=0)
    )
    fig.update_layout(scene_camera=camera)
    if save is not None:
        fig.write_html(save)
    else:
        fig.show()


def visualize(points, save=None):
    dimensions = len(points[0])
    assert dimensions in {1, 2, 3, 4}
    if dimensions == 1:
        v1D(points, save)
    elif dimensions == 2:
        v2D(points, save)
    elif dimensions == 3:
        v3D(points, save)
    elif dimensions == 4:
        v4D(points, save)


import numpy as np


def make_chart(x, y, z):
    z = [round(i, 2) for i in z]
    xd, yd = dict(), dict()
    for i, v in enumerate(z):
        if v in xd.keys():
            xd[v].append(x[i])
        else:
            xd[v] = [x[i]]
        if v in yd.keys():
            yd[v].append(y[i])
        else:
            yd[v] = [y[i]]
    # years equivalent
    z = list(xd.keys())

    # make figure
    fig_dict = {"data": [], "layout": {}, "frames": []}

    # fill in most of layout
    fig_dict["layout"]["xaxis"] = {"range": [min(x), max(x)], "title": "x"}
    fig_dict["layout"]["yaxis"] = {"range": [min(y), max(y)], "title": "y"}
    fig_dict["layout"]["hovermode"] = "closest"
    fig_dict["layout"]["updatemenus"] = [
        {
            "buttons": [
                {
                    "args": [
                        None,
                        {
                            "frame": {"duration": 20, "redraw": False},
                            "fromcurrent": True,
                            "transition": {"duration": 10},
                        },
                    ],
                    "label": "Play",
                    "method": "animate",
                },
                {
                    "args": [
                        [None],
                        {
                            "frame": {"duration": 0, "redraw": False},
                            "mode": "immediate",
                            "transition": {"duration": 0},
                        },
                    ],
                    "label": "Pause",
                    "method": "animate",
                },
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top",
        }
    ]

    sliders_dict = {
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 20},
            "prefix": "z",
            "visible": True,
            "xanchor": "right",
        },
        "transition": {"duration": 10},
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
        "steps": [],
    }

    # make data
    fig_dict["data"].append(
        {
            "x": xd[z[0]],
            "y": yd[z[0]],
            "mode": "markers",
            "marker": {},
            "hoverinfo": "skip",
        }
    )

    # make frames
    for _z in z:
        frame = {"data": [], "name": str(_z)}
        data_dict = {
            "x": xd[_z],
            "y": yd[_z],
            "mode": "markers",
            "marker": {},
            "hoverinfo": "skip",
        }
        frame["data"].append(data_dict)

        fig_dict["frames"].append(frame)
        slider_step = {
            "args": [
                [_z],
                {
                    "frame": {"duration": 10, "redraw": False},
                    "mode": "immediate",
                    "transition": {"duration": 10},
                },
            ],
            "label": _z,
            "method": "animate",
        }
        sliders_dict["steps"].append(slider_step)

    fig_dict["layout"]["sliders"] = [sliders_dict]

    fig = go.Figure(fig_dict)

    fig.update_layout(
        template=minimal_template,
        autosize=False,
        width=480,
        height=480,
        margin=dict(l=10, r=10, b=10, t=10, pad=0),
    )

    fig.show()


def viz(a, b, c):
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=a,
                y=b,
                z=c,
                mode="markers",
                marker=dict(
                    size=1,
                    color="white",
                    showscale=False,
                    reversescale=True,
                ),
                hoverinfo="skip",
            )
        ]
    )

    fig.update_layout(template=minimal_template)
    fig.update_layout(
        autosize=False,
        width=480,
        height=480,
        margin=dict(l=0, r=0, b=0, t=0, pad=0),
        yaxis_zeroline=False,
        xaxis_zeroline=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    fig.update_yaxes(title="asdf")
    camera = dict(
        up=dict(x=0, y=0, z=1), center=dict(x=0, y=0, z=0), eye=dict(x=0, y=2.5, z=0)
    )
    fig.update_layout(scene_camera=camera)
    fig.show(config=dict(displayModeBar=False))
