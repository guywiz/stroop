import random
import time
import dash
from dash import html, dcc, Input, Output, State, no_update, callback_context
from dash.exceptions import PreventUpdate

dash.register_page(
    __name__,
    path="/experiment",
    title="Expérience – Stroop spatial"
)

WORDS = ["Gauche", "Droite", "GAUCHE", "DROITE"]
POSITIONS = ["left", "right"]

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
            children="Appuyez sur ESPACE pour commencer",
            style={
                "fontSize": "32px",
                "color": "gray",
                "position": "absolute",
                "textAlign": "center"
            }
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
    word = random.choice(WORDS)
    position = random.choice(POSITIONS)
    congruent = (
        (word == "Gauche" and position == "left") or
        (word == "Droite" and position == "right")
    )
    return word, position, congruent

@dash.callback(
    Output("stimulus", "children"),
    Output("stimulus", "style"),
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

    fontsize = random.randint(20, 80)
    fontstyle = random.choice(["normal", "italic", "bold", "bold italic"])
    style = {
        "fontSize": fontsize,
        "font-style": fontstyle,
        "color": "gray",
        #"position": "absolute",
        #"left": "20%" if position == "left" else "70%",
        "transform": "translateX(-50%)"
    }

    # Lancement d'un nouvel essai avec ESPACE
    if key == " ":
        word, position, congruent = new_trial()
        style["position"] = "absolute"
        style["left"] = "10%" if position == "left" else "90%"
        machin = (
            word,
            style,
            {"word": word, "position": position, "congruent": congruent, "nb_trial": (trial["nb_trial"] + 1) if trial else 1},
            time.time(),
            "F = gauche | J = droite",
            " "
        )
        print(f"Returning:\n{machin}\n")
        return machin

    # Réponse F ou J
    if trial and start_time and key in ["f", "j"]:
        rt = (time.time() - start_time) * 1000
        response = "left" if key == "f" else "right"
        correct = response == trial["position"]

        print(f"Trial data {trial}\n")

        with open("./results.txt", "a") as fp:
            fp.write(f"Temps de réponse;{rt};correct;{correct};word;{trial['word']};position;{trial['position']};congruence;{trial['congruent']};\n")

        return (
            #trial["word"],
            "",
            #no_update,
            style,
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
    if trial and trial["nb_trial"] > 10:
        return "/goodbye"
    return no_update