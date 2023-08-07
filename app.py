import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from datetime import date
import plotly.graph_objs as go

app = dash.Dash()


app.layout = html.Div(id ='container',children=[
    dcc.Input(id="input1", type="text", placeholder="", style={'display':'inline-grid','marginRight':'10px', 'height': '150 px','font-size':'1.5rem'}),
    dcc.Dropdown([{'label':'A','value':'A'},{'label':'B','value':'B'},{'label':'C','value':'C'}], id='dropdown', style={"display":'inline-grid','width':'300px','vertical-align':'top', 'margin-right':'40px','font-size':'1.5rem'}),
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2025, 12, 31),
        initial_visible_month=date(2023, 6, 30),
        end_date=date(2017, 8, 25), style = {'display':'inline-grid','width':'400px','vertical-align':'top','font-size':'1.5rem','margin-right':'2px'}
    ),

       html.Button('Submit', id='submit-val', n_clicks=0,style={'width':'100px', 'height':'40px'})

]



)





if __name__ =='__main__':
    app.run_server()