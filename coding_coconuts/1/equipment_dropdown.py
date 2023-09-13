from dash import dcc, html
from dash.dependencies import Input, Output

def render(app, df):
    all_equipment = df["Equipment"].unique()

    @app.callback(
        Output("equipment_dropdown", "value"),
        Input("select_all_button", "n_clicks"),
    )
    def select_all_nations(_):
        return all_equipment

    return html.Div(
        children=[
            html.H6("Equipment"),
            dcc.Dropdown(
                id="equipment_dropdown",
                options=[{"label": equipment, "value": equipment} for equipment in all_equipment],
                value=all_equipment,
                multi=True,
            ),
            html.Button(
                children=["Select All"],
                id="select_all_button",
            ),
        ]
    )