import random
import time
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, no_update, callback_context
from dash.exceptions import PreventUpdate

dash.register_page(
    __name__,
    path="/experiment",
    title="Expérience – Stroop numérique bis",
)

# Globals
nb_trials = 10

POSITIONS = ["left", "center", "right"]

style={
    "fontSize": "64px",
    "color": "gray",
    "textAlign": "left"
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
        "outlin": "none",
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
                    dbc.Col(html.Div(id="Gauche", children="", style=style), width=4),
                    dbc.Col(html.Div(id="Center", children="Appuyez sur la barre d'espace pour poursuivre", style=style),width=4),
                    dbc.Col(html.Div(id="Droite", children="", style=style), width=4),
                ]
            ),
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
    digit = random.choice(range(1, 8))
    repeat = random.choice(range(1, 8))
    num = f'{digit}' * repeat
    position = random.choice(POSITIONS)
    congruent = (digit == repeat)
    return digit, repeat, num, position, congruent

@dash.callback(
    Output("Gauche", "children"),
    Output("Center", "children"),
    Output("Droite", "children"),
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
        digit, repeat, num, position, congruent = new_trial()
        machin = (
            num if position == "left" else "",
            num if position == "center" else "",
            num if position == "right" else "",
            {"digit": digit, "repeat": repeat, "congruent": congruent, "nb_trial": (trial["nb_trial"] + 1) if trial else 1},
            time.time(),
            "",
            " "
        )
        return machin

    # Réponse 1, 2, ... ou 9
    if trial and start_time and key in [f"{i}" for i in range(1, 10)]:
        rt = (time.time() - start_time) * 1000
        digit = trial["digit"]
        response = int(key)
        correct = (response == digit)

        with open("./results.txt", "a") as fp:
            fp.write(f"Temps de réponse;{rt};correct;{correct};digit;{trial['digit']};repeat;{trial['repeat']};congruence;{trial['congruent']};\n")

        return (
            "",
            "",
            "",
            trial,
            start_time,
            "Appuyez sur la barre d'espace pour poursuivre",
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
    if trial and trial["nb_trial"] > nb_trials:
        return "/goodbye"
    return no_update