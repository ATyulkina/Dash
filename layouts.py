import dash_bootstrap_components as dbc
from dash import dcc, html

def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(
            brand='Дашборд состояния воздуха в городе 🌆',
            brand_href='#',
            sticky='top', 
            className='mb-3 shadow',
            brand_style={'textAlign': 'center', 'width': '100%', 'fontSize': '24px'}
        ),

        dbc.Row([
            dbc.Col(dbc.Card(id='air-quality-output', body=True), width=8, md=8, xs=12),
            dbc.Col(dbc.Input(id='city-input', value='Saint Peterburg', placeholder='Введите город', type='text', debounce=True), width=4, md=4, xs=12)
        ], className='mb-3'),
        dbc.Row([
            dbc.Col(dcc.Graph(id='co-graph'), width=4, md=4, xs=12),
            dbc.Col(dcc.Graph(id='no2-graph'), width=4, md=4, xs=12),
            dbc.Col(dcc.Graph(id='o3-graph'), width=4, md=4, xs=12)
        ], className='mb-3'),
        dbc.Row([
            dbc.Col(dcc.Graph(id='so2-graph'), width=4, md=4, xs=12),
            dbc.Col(dcc.Graph(id='pm2_5-graph'), width=4, md=4, xs=12),
            dbc.Col(dcc.Graph(id='pm10-graph'), width=4, md=4, xs=12)
        ], className='mb-3'),

        html.Div(className='mb-5')

    ], fluid=True)