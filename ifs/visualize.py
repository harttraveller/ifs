import plotly.graph_objects as go


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
                    size=2,
                    color=a,  # set color equal to a variable
                    colorscale="Viridis",  # one of plotly colorscales
                    showscale=False,
                    reversescale=True,
                ),
            )
        ]
    )
    fig.update_layout(
        template="plotly_dark",
        autosize=False,
        width=500,
        height=500,
        margin=dict(l=10, r=10, b=10, t=10, pad=0),
    )
    if save is not None:
        fig.write_html(save)
    else:
        fig.show()


def visualize(points, save):
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
