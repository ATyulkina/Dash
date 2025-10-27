from utils.data_loader import load_data
import plotly.graph_objects as go
from dash import Input, Output, html
from datetime import datetime

def register_callbacks(app):

    @app.callback(    # декоратор функции
           Output('air-quality-output', 'children'),
           Output('co-graph', 'figure'),
           Output('no2-graph', 'figure'),
           Output('o3-graph', 'figure'),
           Output('so2-graph', 'figure'),
           Output('pm2_5-graph', 'figure'),
           Output('pm10-graph', 'figure'),
           Input('city-input', 'value')
    ) 
    def update_dashboard(city):
        data = load_data(city)

        air_quality_info = html.Div([
            # html.H4(f'{data['city_name']}'),
            html.H4(f'{datetime.strptime(data['day'], '%Y-%m-%d').strftime('%d.%m.%Y')} 🌳 {data['city_name']}'),
            html.Br(),
            html.H5(f'CO - {data['co']} мкг/м³'),
            html.H5(f'NO₂ - {data['no2']} мкг/м³'),
            html.H5(f'O₃ - {data['o3']} мкг/м³'),
            html.H5(f'SO₂ - {data['so2']} мкг/м³'),
            html.H5(f'PM2.5 - {data['pm2_5']} мкг/м³'),
            html.H5(f'PM10 - {data['pm10']} мкг/м³'),
            html.H5(f'Индекс качества воздуха US EPA - {data['us_epa_index']}'),
            html.H5(f'Индекс качества воздуха UK DEFRA - {data['gb_defra_index']}')
        ])

        co_fig = go.Figure(
            data=go.Scatter(x=data['hour'], y=data['co_hour'], mode='lines+markers'),
            layout=go.Layout(title='Концентрация CO по часам', xaxis_title='Время', yaxis_title='Концентрация (мкг/м³)', template='gridon')
        )
        
        no2_fig = go.Figure(
            data=go.Scatter(x=data['hour'], y=data['no2_hour'], mode='lines+markers'),
            layout=go.Layout(title='Концентрация NO₂ по часам', xaxis_title='Время', yaxis_title='Концентрация (мкг/м³)', template='gridon')
        )

        o3_fig = go.Figure(
            data=[go.Scatter(x=data['hour'], y=data['o3_hour'], mode='lines+markers')],
            layout=go.Layout(title='Концентрация O₃ по часам', xaxis_title='Время', yaxis_title='Концентрация (мкг/м³)', template='gridon')
        )

        so2_fig = go.Figure(
            data=[go.Scatter(x=data['hour'], y=data['so2_hour'], mode='lines+markers')],
            layout=go.Layout(title='Концентрация SO₂ по часам', xaxis_title='Время', yaxis_title='Концентрация (мкг/м³)', template='gridon')
        )

        pm2_5_fig = go.Figure(
            data=[go.Scatter(x=data['hour'], y=data['pm2_5_hour'], mode='lines+markers')],
            layout=go.Layout(title='Концентрация PM2.5 по часам', xaxis_title='Время', yaxis_title='Концентрация (мкг/м³)', template='gridon')
        )

        pm10_fig = go.Figure(
            data=[go.Scatter(x=data['hour'], y=data['pm10_hour'], mode='lines+markers')],
            layout=go.Layout(title='Концентрация PM10 по часам', xaxis_title='Время', yaxis_title='Концентрация (мкг/м³)', template='gridon')
        )
        
        return air_quality_info, co_fig, no2_fig, o3_fig, so2_fig, pm2_5_fig, pm10_fig
