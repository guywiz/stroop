import random
import time
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, no_update, callback_context
from dash.exceptions import PreventUpdate

dash.register_page(
    __name__,
    path="/experiment",
    title="Expérience – Stroop classique"
)

# Couleurs et mapping Dash (HTML)
nb_trials = 10

COLORS = {
    "Rouge": "red",
    "Vert": "green",
    "Bleu": "blue",
    "Jaune": "#ffda03" # jaune pas trop clair (parce que sur fond blanc)
}

layout = html.Div(
    style={"textAlign": "center", "fontFamily": "Arial", "marginTop": "50px"},
    children=[
        html.H2("Expérience Stroop"),
        html.P("Clique la couleur du texte, pas ce qui est écrit."),

        html.Div(id="stroop-word", style={"fontSize": "48px", "margin": "40px"}),

        html.Div([
            html.Button(c, id=f"btn-{c}", n_clicks=0,
                        style={"fontSize": "24px", "margin": "10px"}) 
            for c in COLORS.keys()
        ]),

        html.Button("Nouveau mot", id="new-word", 
                    style={"marginTop": "40px", "fontSize": "20px"}),

        dcc.Store(id="trial-data"),
        dcc.Store(id="start-time"),
        dcc.Location(id="redirect_goodbye"),  # Pour la redirection à la fin
    ]
)

'''
# Affichage d'un nouveau mot Stroop
@dash.callback(
    Output("stroop-word", "children"),
    Output("stroop-word", "style"),
    Output("trial-data", "data"),
    Output("start-time", "data"),
    Input("new-word", "n_clicks"),
    prevent_initial_call=True
)
def new_word(_):
    global displayed_word, displayed_color, start_time

    displayed_word = random.choice(list(COLORS.keys()))
    displayed_color = random.choice(list(COLORS.values()))
    trial_data = {"word": displayed_word, "color": displayed_color, "congruent": displayed_color == COLORS[displayed_word], "nb_trial": (trial["nb_trial"] + 1) if trial else 1},
    start_time = time.time()

    return displayed_word, {"color": displayed_color, "fontSize": "48px"}, trial_data, start_time
'''

# Réception d’un clic d’un bouton couleur ou "Nouveau mot"
@dash.callback(
    Output("stroop-word", "children"),
    Output("stroop-word", "style"),
    Output("trial-data", "data"),
    Output("start-time", "data"),
	[Input(f"btn-{color}", "n_clicks") for color in COLORS.keys()],
    Input("new-word", "n_clicks"),
    State("trial-data", "data"),
    State("start-time", "data"),
	prevent_initial_call=True
)
def handle_event(color1, color2, color3, color4, current_res, trial, start_time):
    ctx = callback_context

    if not ctx.triggered:
        raise PreventUpdate

    #trial = ctx.states["trial-data.data"]
    #start_time = ctx.states["start-time.data"]

    trigger = ctx.triggered_id

    if trigger == "new-word":
        print(f"Triggered by new word\n")
        print(f"Received trial: {trial}\n")
        displayed_word = random.choice(list(COLORS.keys()))
        displayed_color = random.choice(list(COLORS.values()))
        trial_data = {"displayed_word": displayed_word, "color": displayed_color, "congruent": displayed_color == COLORS[displayed_word], "nb_trial": (trial[0]["nb_trial"] + 1) if trial else 1},
        start_time = time.time()

        return displayed_word, {"color": displayed_color, "fontSize": "48px"}, trial_data, start_time

    elif trigger in [f"btn-{c}" for c in COLORS.keys()]:
        print(f"Triggered by new color {trigger}\n")
        print(f"Received trial: {trial}\n")
        rt = (time.time() - start_time) * 1000  # en ms
        clicked_button = trigger.split("-")[1]
        displayed_color = trial[0]["color"]
        correct = (COLORS[clicked_button] == displayed_color)

        with open("./results.txt", "a") as fp:
            fp.write(f"Temps de réponse;{rt};correct;{correct};displayed_word;{trial[0]['displayed_word']};displayed_color;{displayed_color};congruence;{trial[0]['congruent']};\n")

        return "", {}, trial, start_time


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