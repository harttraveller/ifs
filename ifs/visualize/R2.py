def v2D(points, save):  # 2D scatterplot
    pass


from ifs.fractals import sierpinski
from ifs.resources import SIMPLEX
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import random

n = 97
d = 2

points = sierpinski(n, d)
points = [list(i) for i in points]
x, y = zip(*points)


def make_chart(x, y, xs, ys, duration):
    x, y = xs + x, ys + y
    # make figure
    fig_dict = {"data": [], "layout": {}, "frames": []}

    # fill in most of layout
    fig_dict["layout"]["xaxis"] = {
        "range": [-0.6, 0.8],
        "title": "x",
        "showgrid": False,
    }
    fig_dict["layout"]["yaxis"] = {
        "range": [-0.6, 0.6],
        "title": "y",
        "showgrid": False,
    }
    fig_dict["layout"]["paper_bgcolor"] = "rgba(0,0,0,0)"
    fig_dict["layout"]["plot_bgcolor"] = "rgba(0,0,0,0)"
    fig_dict["layout"]["hovermode"] = "closest"
    fig_dict["layout"]["updatemenus"] = [
        {
            "buttons": [
                {
                    "args": [
                        None,
                        {
                            "frame": {"duration": duration, "redraw": False},
                            "fromcurrent": True,
                            "transition": {"duration": duration},
                        },
                    ],
                    "label": "Play",
                    "method": "animate",
                },
                {
                    "args": [
                        [None],
                        {
                            "frame": {"duration": duration, "redraw": False},
                            "mode": "immediate",
                            "transition": {"duration": duration},
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
            "prefix": "loop #: ",
            "visible": True,
            "xanchor": "right",
        },
        "transition": {"duration": duration},
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
        "steps": [],
    }

    # make data
    fig_dict["data"].append(
        {
            "x": xs,
            "y": ys,
            "mode": "markers",
            "marker": {"color": "#2ca02c", "size": 10},
        }
    )

    # make frames
    for i in range(len(x)):
        frame = {"data": [], "name": str(i)}

        frame["data"].append(
            {
                "x": x[: i + 3],
                "y": y[: i + 3],
                "mode": "markers",
                "marker": {
                    "color": ["#2ca02c"] * 3 + ["white"] * (i - 1) + ["red"],
                    "size": 10,
                },
            }
        )

        fig_dict["frames"].append(frame)
        slider_step = {
            "args": [
                [i],
                {
                    "frame": {"duration": duration, "redraw": False},
                    "mode": "immediate",
                    "transition": {"duration": duration},
                },
            ],
            "label": i,
            "method": "animate",
        }
        sliders_dict["steps"].append(slider_step)

    fig_dict["layout"]["sliders"] = [sliders_dict]

    fig = go.Figure(fig_dict)

    fig.update_layout(
        template="plotly_dark",
        autosize=False,
        width=480,
        height=480,
        margin=dict(l=0, r=0, b=0, t=0, pad=0),
    )
    fig.update_yaxes(visible=False, showticklabels=False)
    fig.update_xaxes(visible=False, showticklabels=False)
    return fig


xs, ys = list(zip(*SIMPLEX[2]))

fig = make_chart(x, y, xs, ys, 300)

fig.show(config=dict(displayModeBar=False))

fig.write_html(
    "../data/chaos_game_demo.html", auto_play=False, config=dict(displayModeBar=False)
)
