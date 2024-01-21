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
layout = html.Div(
    [
        html.H2('Customer Analytics'), 
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
                                html.H4('Most used Services'),
                                    html.Div(
                                    id='service_analytics_list'
                                )
                            ]
                        ) ,
                        html.Hr(),
                        html.Div(
                            [
                                html.H4('Loyal Customers'),
                                    html.Div(
                                    id='customer_analytics_list'
                                )
                            ]
                        )  ,
                        html.Hr(),
                        html.Div(
                            [
                                html.H4('Occupations with the most number of people'),
                                    html.Div(
                                    id='occupation_analytics_list'
                                )
                            ]
                        ) ,
                    ]
                )
            ]   
        )
    ]
)

@app.callback(
[
    Output('service_analytics_list', 'children') #make sure outputs have unique names
],
[
    Input('url', 'pathname'),
]
)
    
def service_analytics_loadlist(pathname):
    if pathname == '/modules/analytics':
        sql = """
            select  service_name, count (service_name) as total_service
            from transaction tr
            inner join service se on se.service_id = tr.service_id
            where not transaction_delete_ind and not service_delete_ind
            group by service_name
            order by total_service desc
            limit 5;

        """
        #include not delete or else search will not work
        values = [] 
        cols = ["Service Name", "Number of times the service availed"] #make sure column number of data matches sql

        df = db.querydatafromdatabase(sql, values, cols)
        if df.shape: 

            df= df[["Service Name", "Number of times the service availed"]]

            table = dbc.Table.from_dataframe(df, striped=True, bordered=True,
            hover=True, size='sm')
            return [table]
        else:
            return ["No records to display"]
    else:
        raise PreventUpdate# Usual Dash dependencies
@app.callback(
[
    Output('customer_analytics_list', 'children') #make sure outputs have unique names
],
[
    Input('url', 'pathname'),
]
)
    
def customer_analytics_loadlist(pathname):
    if pathname == '/modules/analytics':
        sql = """
            select concat (customer_fname, ' ', customer_lname) , count (concat (customer_fname, ' ', customer_lname)) as total_customer
            from transaction tr
            inner join customer cu on cu.customer_id=tr.customer_id
            where not transaction_delete_ind and not customer_delete_ind
            group by concat (customer_fname, ' ', customer_lname)
            order by total_customer desc
            limit 5;

        """
        #include not delete or else search will not work
        values = [] 
        cols = ["Customer Name", "Number of services availed"] #make sure column number of data matches sql

        df = db.querydatafromdatabase(sql, values, cols)
        if df.shape: 

            df= df[["Customer Name", "Number of services availed"]]

            table = dbc.Table.from_dataframe(df, striped=True, bordered=True,
            hover=True, size='sm')
            return [table]
        else:
            return ["No records to display"]
    else:
        raise PreventUpdate# Usual Dash dependencies

@app.callback(
[
    Output('occupation_analytics_list', 'children') #make sure outputs have unique names
],
[
    Input('url', 'pathname'),
]
)
    
def occupation_analytics_loadlist(pathname):
    if pathname == '/modules/analytics':
        sql = """
           select occupation_name, count( occupation_name) as occupation_count
            from customer cu
            inner join occupation oc on oc.occupation_id=cu.occupation_id
            where  not customer_delete_ind and not occupation_delete_ind
            group by occupation_name
            order by occupation_count desc
            limit 5;
        """
        #include not delete or else search will not work
        values = [] 
        cols = ["Occupation Name", "Number of Customers"] #make sure column number of data matches sql

        df = db.querydatafromdatabase(sql, values, cols)
        if df.shape: 

            df= df[["Occupation Name", "Number of Customers"]]

            table = dbc.Table.from_dataframe(df, striped=True, bordered=True,
            hover=True, size='sm')
            return [table]
        else:
            return ["No records to display"]
    else:
        raise PreventUpdate# Usual Dash dependencies
