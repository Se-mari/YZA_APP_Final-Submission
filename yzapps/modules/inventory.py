#transaction WIP
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app

from yzapps import dbconnect as db
from yzapps.modules import services_profile
layout = html.Div(
    [
        html.H2('Inventory Level'), 
        html.Hr(),
        dbc.Card( 
            [
                dbc.CardHeader(
                    [
                        html.H3()
                    ]
                ),
                dbc.CardBody( 
                [   
                        html.Hr(),
                        html.Div(
                            [
                                html.H4(),
                                    html.Div(
                                    id='inventory_list'
                                )
                            ]
                        )   
                    ]
                )
            ]   
        )
    ]
)

@app.callback(
[
    Output('inventory_list', 'children') #make sure outputs have unique names
],
[
    Input('url', 'pathname'),
]
)
    
def inventory_loadlist(pathname):
    if pathname == '/modules/inventory':
        sql = """
                    WITH OutputData AS (
                SELECT
                    ma.material_name,
                    SUM(tr.quantity * se.quantity) AS total_inventory_output
                FROM
                    transaction tr
                INNER JOIN
                    service se ON se.service_id = tr.service_id
                INNER JOIN
                    material ma ON ma.material_id = se.material_id
                WHERE
                    NOT se.service_delete_ind
                    AND NOT tr.transaction_delete_ind
                    AND NOT ma.material_delete_ind
                GROUP BY
                    ma.material_name
            ),
            InputData AS (
                SELECT
                    ma.material_name,
                    SUM(su.quantity) AS total_inventory_input
                FROM
                    material ma
                INNER JOIN
                    supplies su ON su.material_id = ma.material_id
                GROUP BY
                    ma.material_name
            )
            SELECT
                o.material_name,
                COALESCE(total_inventory_input, 0) - COALESCE(total_inventory_output, 0) AS net_inventory
            FROM
                OutputData o
            FULL OUTER JOIN
                InputData i ON o.material_name = i.material_name;

        """
        #include not delete or else search will not work
        values = [] 
        cols = ["Material Name", "Inventory Level"] #make sure column number of data matches sql

        df = db.querydatafromdatabase(sql, values, cols)
        if df.shape: 

            df= df[["Material Name", "Inventory Level"]]

            table = dbc.Table.from_dataframe(df, striped=True, bordered=True,
            hover=True, size='sm')
            return [table]
        else:
            return ["No records to display"]
    else:
        raise PreventUpdate