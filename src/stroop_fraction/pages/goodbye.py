import dash
from dash import html, dcc, Input, Output, State, no_update

dash.register_page(
    __name__,
    path="/goodbye",
    title="Stroop numérique - conclusion"
)

layout = html.Div(
    style={
        "maxWidth": "700px",
        "margin": "80px auto",
        "fontFamily": "Arial",
        "lineHeight": "1.6",
    },
    children=[
        html.H1("Expérience de Stroop numérique"),

        html.P("L'équipe vous remercie du temps accordé à cette expérience."),

    ]
)
