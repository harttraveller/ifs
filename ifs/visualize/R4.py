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
