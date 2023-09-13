from dash import html, dash_table


def render(app, df):
    table = dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])

    return html.Div(children=[
            html.H6("Number of times worked per equipment", style={'textAlign': 'center'}),
            html.Div(table, id="table")
            ])
