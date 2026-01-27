import time
import random
import dash
from dash import Dash, html, dcc, callback, Output, Input, State

# Couleurs et mapping Dash (HTML)
COLORS = {
    "Rouge": "red",
    "Vert": "green",
    "Bleu": "blue",
    "Jaune": "#ffda03" # jaune pas trop clair (parce que sur fond blanc)
}

# Variables globales (un fichier ou store pourrait être mieux plus tard)
displayed_word = None
displayed_color = None
start_time = None

app = Dash(__name__, use_pages=True)

app.layout = html.Div(
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

        html.Div(id="result", style={"fontSize": "24px", "marginTop": "30px", "color": "darkblue"})
    ]
)

# Affichage d'un nouveau mot Stroop
@callback(
    Output("stroop-word", "children"),
    Output("stroop-word", "style"),
    Input("new-word", "n_clicks"),
    prevent_initial_call=True
)
def new_word(_):
    global displayed_word, displayed_color, start_time

    displayed_word = random.choice(list(COLORS.keys()))
    displayed_color = random.choice(list(COLORS.values()))
    start_time = time.time()

    return displayed_word, {"color": displayed_color, "fontSize": "48px"}

# Réception d’un clic d’un bouton couleur

@callback(
	Output("result", "children"),
	[Input(f"btn-{color}", "n_clicks") for color in COLORS.keys()],
	State("result", "children"),
	prevent_initial_call=True
)
def check_answer(color1, color2, color3, color4, current_res):
	global start_time, displayed_color
	if start_time is None:
		return current_res

	reaction = (time.time() - start_time) * 1000  # en ms
	start_time = None

	clicked_button = dash.callback_context.triggered[0]["prop_id"].split("-")[1].split(".")[0]
	correct_color = [k for k, v in COLORS.items() if v == displayed_color][0]

	correct = (clicked_button == correct_color)
	with open("./results.txt", "a") as fp:
		fp.write(f"Temps de reaction {reaction:.0f} ms\n")
	print(f"Temps de reaction {reaction:.0f} ms")
	return f"{'✔️' if correct else '❌'} Temps de réaction : {reaction:.0f} ms"


if __name__ == "__main__":
    app.run(debug=True)
