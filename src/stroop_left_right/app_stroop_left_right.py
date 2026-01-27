from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div(
    children=[
        dcc.Store(id="subject-info"),
        dash.page_container,
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
