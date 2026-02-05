import dash
from dash import html, dcc, Input, Output, State
import random
import pandas as pd
import os
from datetime import datetime


# =====================
# CONFIG
# =====================

DATA_FILE = "memory_data.csv"

N_WORDS = 12

WORD_LIST = [
    "arbre","maison","livre","chat","pluie","route","pain",
    "soleil","mer","montagne","clé","verre","horloge","nuage",
    "table","feu","porte","train","fleur","stylo"
]


# =====================
# INIT FILE
# =====================

if not os.path.exists(DATA_FILE):

    df = pd.DataFrame(columns=[
        "timestamp",
        "subject",
        "position",
        "word",
        "recalled"
    ])

    df.to_csv(DATA_FILE, index=False)


# =====================
# APP
# =====================

app = dash.Dash(__name__)


app.layout = html.Div([

    html.H2("Expérience : Effet de récence (mémoire)"),

    dcc.Store(id="words"),
    dcc.Store(id="index", data=0),

    html.Div(id="instructions"),

    html.H1(id="word-display"),

    html.Button("Mot suivant (Espace)", id="next"),

    html.Br(), html.Br(),

    html.Div(id="recall-phase"),

    dcc.Textarea(
        id="recall-input",
        style={"width":"100%","height":"120px"}
    ),

    html.Br(),

    html.Button("Valider rappel", id="submit"),

    html.Div(id="feedback"),

    html.Div(id="thanks"),

],
style={"width":"600px","margin":"auto"})

# Initialisation des mots et des instructions
@app.callback(
    Output("words", "data"),
    Output("instructions", "children"),

    Input("instructions", "children"),
    prevent_initial_call=False
)
def init(_):

    words = random.sample(WORD_LIST, N_WORDS)

    return words, "Appuyez sur 'Mot suivant' pour voir les mots."

# Affichage séquentiel
@app.callback(
    Output("word-display", "children"),
    Output("index", "data"),
    Output("recall-phase", "children"),

    Input("next", "n_clicks"),

    State("words", "data"),
    State("index", "data"),

    prevent_initial_call=True
)
def show_word(n, words, idx):

    if idx < N_WORDS:

        word = words[idx]

        return word, idx+1, ""

    else:

        return "", idx, "Phase de rappel : écrivez les mots dont vous vous souvenez."

# Enregistrement rappel
@app.callback(
    Output("feedback", "children"),
    Output("thanks", "children"),

    Input("submit", "n_clicks"),

    State("recall-input", "value"),
    State("words", "data"),

    prevent_initial_call=True
)
def save(n, text, words):

    if not text:
        return "Veuillez écrire des mots.", ""

    recalled = set(
        w.strip().lower() for w in text.split()
    )

    now = datetime.now().isoformat()

    df = pd.read_csv(DATA_FILE)

    subject = now  # identifiant simple

    for i, w in enumerate(words):

        row = {
            "timestamp": now,
            "subject": subject,
            "position": i+1,
            "word": w,
            "recalled": int(w.lower() in recalled)
        }

        df = df.append(row, ignore_index=True)

    df.to_csv(DATA_FILE, index=False)

    return "Réponses enregistrées.", "Merci !"

if __name__ == "__main__":
    app.run_server(debug=True)
