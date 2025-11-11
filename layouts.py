import dash_bootstrap_components as dbc
from dash import dcc, html

def create_layout():
    return dbc.Container([
        html.Div([html.H1('Дашборд состояния воздуха в городе 🌆', className='header')]),

        dbc.Row([
            dbc.Col(dbc.Card(id='air-quality-output', body=True, className='dash-card'), width=3, md=3, xs=12),
            dbc.Col(dbc.Card(id='us_epa-output', body=True, className='card-1'), width=3),
            dbc.Col(dbc.Card(id='uk_defra-output', body=True, className='card-1'), width=3),
            dbc.Col(dbc.Input(id='city-input', value='Saint Peterburg', placeholder='Введите город', type='text', debounce=True, className='city'), width=3, md=3, xs=12)
        ], className='mb-3'),
        dbc.Row([
            dbc.Col(dbc.Card(id='co-output', body=True, className='card')),
            dbc.Col(dbc.Card(id='no2-output', body=True, className='card')),
            dbc.Col(dbc.Card(id='o3-output', body=True, className='card')),
            dbc.Col(dbc.Card(id='so2-output', body=True, className='card')),
            dbc.Col(dbc.Card(id='pm2_5-output', body=True, className='card')),
            dbc.Col(dbc.Card(id='pm10-output', body=True, className='card')),]),


        dbc.Row([
            dbc.Col([html.Label("Выберите день", className="filter-label"),
                    dcc.Dropdown(id="day-input", className='filter-dropdown',
                                options=[
                                    {'label': 'Сегодня', 'value': 0},
                                    {'label': 'Завтра', 'value': 2},
                                    {'label': 'Послезавтра', 'value': 3},
                                    ],
                                value=0,  # значение по умолчанию
                                )], md=2, )]),

        dbc.Row([
            dbc.Col(dcc.Graph(id='co-graph', className='dash-graph'), width=4, md=4, xs=12, className='dash-graph'),
            dbc.Col(dcc.Graph(id='no2-graph', className='dash-graph'), width=4, md=4, xs=12, className='dash-graph'),
            dbc.Col(dcc.Graph(id='o3-graph', className='dash-graph'), width=4, md=4, xs=12, className='dash-graph')
        ], className='mb-3'),
        dbc.Row([
            dbc.Col(dcc.Graph(id='so2-graph', className='dash-graph'), width=4, md=4, xs=12, className='dash-graph'),
            dbc.Col(dcc.Graph(id='pm2_5-graph', className='dash-graph'), width=4, md=4, xs=12, className='dash-graph'),
            dbc.Col(dcc.Graph(id='pm10-graph', className='dash-graph'), width=4, md=4, xs=12, className='dash-graph')
        ], className='mb-3'),

        html.Div(className='mb-5')

    ], fluid=True)