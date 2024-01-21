# Payment
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
from yzapps.modules import staff_profile



layout = html.Div(
    [
        html.H2('Payment Type'), 
        html.Hr(),
        dbc.Card( 
            [
                dbc.CardHeader(
                    [
                        html.H3('Manage Payment')
                    ]
                ),
                dbc.CardBody( 
                [   
                        html.Div( 
                            [
                                dbc.Button('Add Payment Type', color="secondary", href='/modules/payment_profile?mode=add'),
                            ]
                        ),
                        html.Hr(),
                        html.Div(
                            [
                                html.H4(''),
                                    html.Div(
                                    id='payment_list'
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
    Output('payment_list', 'children') #make sure outputs have unique names
],
[
    Input('url', 'pathname'),
]
)
    
def payment_loadlist(pathname):
    if pathname == '/modules/payment':
        sql = """
        select type_name, type_description, type_id
            from payment_type
            where not type_delete_ind
        """
        #include not delete or else search will not work
        values = [] 
        cols = ['Name', 'Description',  'ID'] #make sure column number of data matches sql

        df = db.querydatafromdatabase(sql, values, cols)
        if df.shape: 
            buttons = []
            for profile_id in df['ID']:
                buttons +=  [
                    html.Div(
                        dbc.Button('Edit',href=f'/modules/payment_profile?mode=edit&id={profile_id}',
                                   size='sm', color='warning'),
                                   style={'text-align': 'center'}
                    )
                ]
            df['Action'] =buttons
            df= df[['Name', 'Description', "Action"]]

            table = dbc.Table.from_dataframe(df, striped=True, bordered=True,
            hover=True, size='sm')
            return [table]
        else:
            return ["No records to display"]
    else:
        raise PreventUpdate