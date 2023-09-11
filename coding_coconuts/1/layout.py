from dash import html
import bar_chart, data_table, equipment_dropdown
from job_data import create_df, \
get_worker_names, create_summary_df, create_datatable_df

def create_layout(app):
    df = create_df()
    bar_chart_df = create_summary_df(df)
    data_table_df = create_datatable_df(df)
    worker_names = get_worker_names(create_df())
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title, style={'textAlign': 'center'}),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    equipment_dropdown.render(app, bar_chart_df),
                ],
            ),
            bar_chart.render(app, bar_chart_df, worker_names),
            html.Br(),
            html.Hr(),
            data_table.render(app, data_table_df),
        ],
    )