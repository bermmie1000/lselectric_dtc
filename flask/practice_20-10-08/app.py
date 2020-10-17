import dash
import dash_html_components as html

from dash.dependencies import Input, Output
import random

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button("create random number", id="button"),
        html.Br(),
        html.Label("축하합니다", id="label"),
    ]
)

app.layout = html.Div(
    [
        html.Button("create random number", id="button"),
        html.Br(),
        html.Label("축하합니다", id="label"),
    ]
)


@app.callback(
    Output(component_id="label", component_property="children"),
    [Input(component_id="button", component_property="n_clicks")],
)
def update_output(input_value):
    return random.random()


if __name__ == "__main__":
    app.run_server(debug=True, host="127.0.0.1")
