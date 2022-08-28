from ifs.fractals import sierpinski
from ifs.resources import SIMPLEX
import plotly.graph_objects as go
import plotly.
import numpy as np

points = sierpinski(10000, 2)

x, y = zip(*points)


fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', marker={"color": "white","size":1}))
fig.update_layout(yaxis_zeroline=False,
                  xaxis_zeroline=False,
                  template="plotly_dark",
                    autosize=False,
                    width=480,
                    height=480,
                    margin=dict(l=0, r=0, b=0, t=0, pad=0),
                  paper_bgcolor="rgba(0,0,0,0)",
                  plot_bgcolor="rgba(0,0,0,0)",
                  xaxis={"range": [-0.6, 0.6],"showgrid": False},
                  yaxis={"range": [-0.6, 0.6],"showgrid": False})
fig.update_yaxes(visible=False, showticklabels=False)
fig.update_xaxes(visible=False, showticklabels=False)

fig.show(
        config= dict(
            displayModeBar = False)
        )

fig.write_html("../data/chaos_game_highres.html",auto_play=False,
        config= dict(
            displayModeBar = False)
        )