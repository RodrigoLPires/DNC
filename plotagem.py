import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash()

dataframe_one = pd.DataFrame(
    {
        'Fruit': ['Apples', 'Banana'],
        'Valor': [25.9, 30.6]
    }
)

figure_one = px.bar(dataframe_one, x='Fruit', y='Valor')

figure_two = px.line(dataframe_one, x='Fruit', y='Valor')

app.layout = html.Div(
    children=[
        html.H1('Dash Tutorial'),
        html.H2('Outro Titulo'),
        html.Button('Outro Lugar'),
        dcc.Graph(
            id='Example I',
            figure=figure_one,
        ),
        dcc.Graph(
            id='Example II',
            figure=figure_two
        ),
        dcc.Dropdown(
            [1,2]
        )        
    ]
)
app.run_server()