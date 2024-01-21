#For YZAPP
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.exceptions import PreventUpdate

from app import app

navlink_style = {
    'color': '#FFFFFF'
}
navlink_style_drp = {
    'color': '#FFFFFF',
    'background-color':'#E44F4F'

}
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "12rem",
    "padding": "2rem 1rem",
    "background-color": "#E44F4F",
    "overflow": "auto"
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.

navbar = html.Div(
    [
        html.H2("YZApp", className="display-5", style={'color':'#FFFFFF', 'font-weight':'bold'}),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/home", style=navlink_style),
                dbc.NavLink("Transaction", href="/modules/transaction", style=navlink_style),
                dbc.DropdownMenu(
                    [dbc.NavLink("Customer Analytics", href="/modules/analytics", style=navlink_style_drp),
                     dbc.NavLink("Inventory Level", href="/modules/inventory", style=navlink_style_drp),
                         ],
                    label="Analytics",
                    toggle_style = {
                        "color": "#FFFFFF",
                        "background": "#E44F4F",},
                    nav=True,
                ),
                dbc.DropdownMenu(
                    [dbc.NavLink("Staff", href="/modules/staff", style=navlink_style_drp),
                        dbc.NavLink("Staff Report", href="/modules/staff_report", style=navlink_style_drp),],
                    label="Staff",
                    toggle_style = {
                        "color": "#FFFFFF",
                        "background": "#E44F4F",},
                    nav=True,
                ),   
                dbc.DropdownMenu(
                    [dbc.NavLink("Customers", href="/modules/customers", style=navlink_style_drp),
                        dbc.NavLink("Occupation", href="/modules/occupation", style=navlink_style_drp),
                        dbc.NavLink("Payment Types", href="/modules/payment", style=navlink_style_drp),],
                    label="Customer",
                    toggle_style = {
                        "color": "#FFFFFF",
                        "background": "#E44F4F",},
                    nav=True,
                ),   
                dbc.DropdownMenu(
                    [dbc.NavLink("Materials", href="/modules/material", style=navlink_style_drp),
                        dbc.NavLink("Category", href="/modules/category", style=navlink_style_drp), 
                        dbc.NavLink("Suppliers", href="/modules/suppliers", style=navlink_style_drp),
                        dbc.NavLink("Supplies", href="/modules/supplies", style=navlink_style_drp),],
                    label="Materials",
                    toggle_style = {
                        "color": "#FFFFFF",
                        "background": "#E44F4F",},
                    nav=True,
                ),  
                dbc.DropdownMenu(
                    [dbc.NavLink("Services", href="/modules/services", style=navlink_style_drp),
                        dbc.NavLink("Status", href="/modules/status", style=navlink_style_drp),],
                    label="Services",
                    toggle_style = {
                        "color": "#FFFFFF",
                        "background": "#E44F4F",},
                    nav=True,
                ),           
                dbc.NavLink("Users", href="/modules/users", style=navlink_style),
                dbc.NavLink("Logout", href="/logout", style=navlink_style),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)