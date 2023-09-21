import pandas as pd
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

def render(app, df, worker_names):
    
    @app.callback(
        Output("bar-chart", "children"),
        Input("equipment_dropdown", "value")
    )
    def update_bar_chart(all_equipment):
        long_format_df = pd.melt(df, 
                                id_vars=["Equipment"],
                                value_vars=worker_names,
                                var_name="Name",
                                value_name="Nr of times worked")
        filtered_data = long_format_df.query("Equipment in @all_equipment")
        fig = px.bar(filtered_data,
                    x="Equipment",
                    y="Nr of times worked",
                    color="Name",
                    barmode="group"
                    )
        fig.update_layout(
            title=dict(text="Comparison of the number of times worked per equipment"),
            font=dict(size=18)
        )
        return html.Div(dcc.Graph(figure=fig), id="bar-chart")
    return html.Div(id="bar-chart")