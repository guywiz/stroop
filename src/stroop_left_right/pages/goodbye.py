import dash
from dash import html, dcc, Input, Output, State, no_update

dash.register_page(
    __name__,
    path="/goodbye",
    title="Stroop spatial - conclusion"
)

layout = html.Div(
    style={
        "maxWidth": "700px",
        "margin": "80px auto",
        "fontFamily": "Arial",
    },
    children=[
        html.H1("Expérience de Stroop spatial"),

        html.P("L'équipe vous remercie du temps accordé à cette expérience."),

    ]
)
