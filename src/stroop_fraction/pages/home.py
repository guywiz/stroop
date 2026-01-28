import dash
from dash import html, dcc, Input, Output, State, no_update

dash.register_page(
    __name__,
    path="/",
    title="Accueil – Stroop spatial"
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

        html.P("En appuyant sur la barre d'espace, deux fractions seront affichées à l'écran."),
        html.P('Votre tâche consiste à indiquer la fraction (celle située à gauche, ou celle située à droite) est la plus grande.'),
        html.P('Il vous faut réagir le plus rapidement possible, "sans réfléchir".'),
        html.P('Pour cela, utilisez la touche "F" pour indiquer "Gauche" et la touche "J" pour indiquer "Droite".'),

        html.H3("Informations participant"),
        html.P("Avant de commencer l'expérience, merci de renseigner quelques informations vous concernant."),

        html.Label("Âge"),
        dcc.Input(
            id="age-input",
            type="number",
            min=10,
            max=100,
            step=1,
            style={"width": "100%", "marginBottom": "20px"},
        ),

        html.Label("Filière de formation"),
        dcc.Input(
            id="field-input",
            type="text",
            placeholder="Ex : Informatique, Psychologie…",
            style={"width": "100%", "marginBottom": "30px"},
        ),

        html.Button(
            "Commencer l’expérience",
            id="start-btn",
            n_clicks=0,
            style={"fontSize": "18px"},
        ),

        html.Div(
            id="form-error",
            style={"color": "darkred", "marginTop": "20px"},
        ),

        dcc.Location(id="redirect"),
    ]
)


@dash.callback(
    Output("subject-info", "data"),
    Output("redirect", "pathname"),
    Output("form-error", "children"),
    Input("start-btn", "n_clicks"),
    State("age-input", "value"),
    State("field-input", "value"),
    prevent_initial_call=True,
)
def validate_form(_, age, field):
    if age is None or not field or field.strip() == "":
        return no_update, no_update, "Veuillez renseigner tous les champs."

    with open("./results.txt", "a") as fp:
        fp.write(f"Filière {field}, age {age}\n")

    return (
        {"age": age, "field": field},
        "/experiment",
        "",
    )
