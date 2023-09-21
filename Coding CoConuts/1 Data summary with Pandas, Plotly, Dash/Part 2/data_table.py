from dash import html, dash_table

def render(app, df):
    table = dash_table.DataTable(
        data=df.to_dict("records"),
        columns=[{"name":c, "id":c} for c in df.columns]
    )
    
    return html.Div(children=[
        html.H6("Nr of times worked per equipment",
        style={"textAlign":"center"}),
        html.Div(table, id="table")
    ]
    )