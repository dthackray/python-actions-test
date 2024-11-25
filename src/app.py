from dash import Dash

from components.layout import create_layout

app = Dash(__name__)
app.layout = create_layout()

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
