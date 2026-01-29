import random
import time
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, no_update, callback_context
from dash.exceptions import PreventUpdate

dash.register_page(
    __name__,
    path="/experiment",
    title="Expérience – Stroop numérique"
)

nb_trials = 10

style_gauche={
    "fontSize": "64px",
    "color": "gray",
    #"position": "absolute",
    "textAlign": "left"
}
style_center={
    "fontSize": "64px",
    "color": "gray",
    #"position": "absolute",
    "textAlign": "center"
}
style_droite={
    "fontSize": "64px",
    "color": "gray",
    #"position": "absolute",
    "textAlign": "right"
}

layout = [html.Div(
    id="container",
    tabIndex="0",  # IMPORTANT : permet de capter le clavier
    style={
        "width": "100vw",
        "height": "100vh",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
        "outline": "none",
        "fontFamily": "Arial",
    },
    children=[
        dcc.Store(id="trial-data"),
        dcc.Store(id="start-time"),

        html.Div(
            id="stimulus",
            #children="Appuyez sur ESPACE pour commencer",
            children=dbc.Row(
                [
                    dbc.Col(html.Div(id="Gauche", children="Appuyer sur", style=style_gauche), width=4),
                    dbc.Col(html.Div(id="Center", children="ESPACE", style=style_center),width=4),
                    dbc.Col(html.Div(id="Droite", children="pour continuer", style=style_droite), width=4),
                ]
            ),
            #children=[
            #    html.Div(id="Gauche", style={"fontSize": "40px"}, children="Appuyez sur ESPACE pour commencer"),
            #    html.Div(id="Droite", style={"fontSize": "40px"}, children=""),
            #],
        ),

        html.Div(
            id="feedback",
            style={
                "position": "absolute",
                "bottom": "50px",
                "fontSize": "24px",
                "color": "darkblue"
            }
        ),

        dcc.Input(
            id="key-catcher",
            type="text",
            autoFocus=True,
            style={
                "position": "absolute",
                "left": "-10000px",
                "top": "-10000px"
            },
        ),
        dcc.Location(id="redirect_goodbye"),
    ])
]

def new_trial():
    a = random.choice(range(100, 10000))
    b = random.choice(range(100, 10000))
    fontsize_a = random.choice(range(4,40))
    fontsize_b = random.choice(range(4,40))
    while (a == b):
        b = random.choice(range(4,40))
    congruent = ((a < b) and (fontsize_a < fontsize_b)) or ((a > b) and (fontsize_a > fontsize_b))
    return a, b, fontsize_a, fontsize_b, congruent

@dash.callback(
    Output("Gauche", "children"),
    Output("Gauche", "style"),
    Output("Center", "children"),
    Output("Droite", "children"),
    Output("Droite", "style"),
    Output("trial-data", "data"),
    Output("start-time", "data"),
    Output("feedback", "children"),
    Output("key-catcher", "value"),
    Input("key-catcher", "value"),
    State("trial-data", "data"),     # <-- AJOUT
    State("start-time", "data"),     # <-- AJOUT
    prevent_initial_call=True
)
def handle_keypress(value, trial, start_time):

    ctx = callback_context
    if not value:
        raise PreventUpdate

    key = value[-1].lower()

    trial = ctx.states["trial-data.data"]
    start_time = ctx.states["start-time.data"]

    # Lancement d'un nouvel essai avec ESPACE
    if key == " ":
        a, b, fontsize_a, fontsize_b, congruent = new_trial()
        style_gauche["font-size"] = fontsize_a * 5
        print(f"Style gauche {style_gauche}")
        style_droite["font-size"] = fontsize_b * 5
        machin = (
            f"{a}",
            style_gauche,
            "",
            f"{b}",
            style_droite,
            {"numbers": [a, b], "fontsize": [fontsize_a, fontsize_b], "congruent": congruent, "nb_trial": (trial["nb_trial"] + 1) if trial else 1},
            time.time(),
            "F = gauche | J = droite",
            " "
        )
        return machin

    # Réponse F ou J
    if trial and start_time and key in ["f", "j"]:
        rt = (time.time() - start_time) * 1000
        response = "left" if key == "f" else "right"
        a, b = trial["numbers"]
        fontsize_a, fontsize_b = trial["fontsize"]
        correct = (a > b) and (response == "left") or (a < b) and (response == "right")

        with open("./results.txt", "a") as fp:
            fp.write(f"Temps de réponse;{rt};correct;{correct};numbers;{trial['numbers']};fontsize;{trial['fontsize']};congruence;{trial['congruent']};\n")

        return (
            #trial["word"],
            "",
            style_gauche,
            "",
            "",
            style_droite,
            trial,
            start_time,
            f"{'✔️' if correct else '❌'} "
            f"Temps de réaction : {rt:.0f} ms — "
            f"{'Congruent' if trial['congruent'] else 'Incongruent'} "
            f"(Espace pour recommencer)",
            " "
        )

    raise PreventUpdate

@dash.callback(
    Output("redirect_goodbye", "pathname"),
    Input("trial-data", "data"),
)
def redirect_when_done(trial):
    global nb_trials
    print(f"Input trial: {trial}\n")
    if trial and trial[0]["nb_trial"] > nb_trials:
        return "/goodbye"
    return no_update