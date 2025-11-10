import plotly.graph_objects as go
import assets.design as ds
from utils.data_loader import load_data
from dash import Input, Output, html
from datetime import datetime

def register_callbacks(app):

    @app.callback(    # декоратор функции
           Output('air-quality-output', 'children'),
           Output('co-output', 'children'),
           Output('no2-output', 'children'),
           Output('o3-output', 'children'),
           Output('so2-output', 'children'),
           Output('pm2_5-output', 'children'),
           Output('pm10-output', 'children'),
           Output('us_epa-output', 'children'),
           Output('uk_defra-output', 'children'),
           Output('co-graph', 'figure'),
           Output('no2-graph', 'figure'),
           Output('o3-graph', 'figure'),
           Output('so2-graph', 'figure'),
           Output('pm2_5-graph', 'figure'),
           Output('pm10-graph', 'figure'),
           Input('city-input', 'value'),
           Input('day-input', 'value'),
    ) 
    def update_dashboard(city, days):
        data = load_data(city, days)

        air_quality_info = html.Div([
            # html.H4(f'{data['date']}'),
            html.H4(f'{datetime.strptime(data['day'], '%Y-%m-%d').strftime('%d.%m.%Y')} 🌳')
        ])

        co_info = html.Div([
            html.H4('CO'),
            html.H6('Оксид углерода'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H4(f'{data['co']} мкг/м³')
        ])

        no2_info = html.Div([
            html.H4('NO₂'),
            html.H6('Диоксид азота'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H4(f'{data['no2']} мкг/м³')
        ])

        o3_info = html.Div([
            html.H4('O₃'),
            html.H6('Озон'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H4(f'{data['o3']} мкг/м³')
        ])

        so2_info = html.Div([
            html.H4('SO₂'),
            html.H6('Диоксид серы'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H4(f'{data['so2']} мкг/м³')
        ])


        pm2_5_info = html.Div([
            html.H4('PM2.5'),
            html.H6('Мелкие частицы (≤ 2,5 мкм)'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H4(f'{data['pm2_5']} мкг/м³')
        ])

        pm10_info = html.Div([
            html.H4('PM10'),
            html.H6('Крупные частицы (≤ 10 мкм)'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H4(f'{data['pm10']} мкг/м³')
        ])

        us_epa_info = html.Div([
            html.H4('EPA'),
            html.H6('Индекс качества воздуха US'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H4(f'{data['us_epa_index']} мкг/м³')
        ])

        uk_defra_info = html.Div([
            html.H4('DEFRA'),
            html.H6('Индекс качества воздуха UK'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H4(f'{data['gb_defra_index']} мкг/м³')
        ])






        co_fig = go.Figure(
            data=go.Scatter(x=data['hour'], y=data['co_hour'], mode='lines+markers', line=dict(color=ds.GRAPH_LINE_COLOR), marker=dict(color=ds.GRAPH_LINE_COLOR)),
            layout=go.Layout(
                title='Концентрация CO по часам', 
                xaxis_title='Время', 
                yaxis_title='Концентрация (мкг/м³)',
                title_font_size=ds.GRAPH_TITLE_FONT_SIZE,
                title_font_color=ds.GRAPH_TITLE_COLOR,
                title_x=ds.GRAPH_TITLE_ALIGN,
                title_font_weight=ds.GRAPH_TITLE_FONT_WEIGHT,
                font=dict(family=ds.GRAPH_FONT_FAMILY),
                xaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, color=ds.GRAPH_TITLE_COLOR, gridcolor=ds.GRAPH_GRID_COLOR, tickfont=dict(size=ds.GRAPH_TICK_FONT_SIZE)),
                yaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, color=ds.GRAPH_TITLE_COLOR, gridcolor=ds.GRAPH_GRID_COLOR, tickfont=dict(size=ds.GRAPH_TICK_FONT_SIZE)),
                legend=dict(font=dict(size=ds.GRAPH_FONT_SIZE)),
                plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
                paper_bgcolor=ds.PAPER_BACKGROUND_COLOR,
                )
        )
        
        no2_fig = go.Figure(
            data=go.Scatter(x=data['hour'], y=data['no2_hour'], mode='lines+markers', line=dict(color=ds.GRAPH_LINE_COLOR), marker=dict(color=ds.GRAPH_LINE_COLOR)),
            layout=go.Layout(
                title='Концентрация NO₂ по часам', 
                xaxis_title='Время', 
                yaxis_title='Концентрация (мкг/м³)',
                title_font_size=ds.GRAPH_TITLE_FONT_SIZE,
                title_font_color=ds.GRAPH_TITLE_COLOR,
                title_x=ds.GRAPH_TITLE_ALIGN,
                title_font_weight=ds.GRAPH_TITLE_FONT_WEIGHT,
                font=dict(family=ds.GRAPH_FONT_FAMILY),
                xaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, color=ds.GRAPH_TITLE_COLOR, gridcolor=ds.GRAPH_GRID_COLOR, tickfont=dict(size=ds.GRAPH_TICK_FONT_SIZE)),
                yaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, color=ds.GRAPH_TITLE_COLOR, gridcolor=ds.GRAPH_GRID_COLOR, tickfont=dict(size=ds.GRAPH_TICK_FONT_SIZE)),
                legend=dict(font=dict(size=ds.GRAPH_FONT_SIZE)),
                plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
                paper_bgcolor=ds.PAPER_BACKGROUND_COLOR
                )
        )

        o3_fig = go.Figure(
            data=go.Scatter(x=data['hour'], y=data['o3_hour'], mode='lines+markers', line=dict(color=ds.GRAPH_LINE_COLOR), marker=dict(color=ds.GRAPH_LINE_COLOR)),
            layout=go.Layout(
                title='Концентрация O₃ по часам', 
                xaxis_title='Время', 
                yaxis_title='Концентрация (мкг/м³)', 
                title_font_size=ds.GRAPH_TITLE_FONT_SIZE,
                title_font_color=ds.GRAPH_TITLE_COLOR,
                title_x=ds.GRAPH_TITLE_ALIGN,
                title_font_weight=ds.GRAPH_TITLE_FONT_WEIGHT,
                font=dict(family=ds.GRAPH_FONT_FAMILY),
                xaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, color=ds.GRAPH_TITLE_COLOR, gridcolor=ds.GRAPH_GRID_COLOR, tickfont=dict(size=ds.GRAPH_TICK_FONT_SIZE)),
                yaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, color=ds.GRAPH_TITLE_COLOR, gridcolor=ds.GRAPH_GRID_COLOR, tickfont=dict(size=ds.GRAPH_TICK_FONT_SIZE)),
                legend=dict(font=dict(size=ds.GRAPH_FONT_SIZE)),
                plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
                paper_bgcolor=ds.PAPER_BACKGROUND_COLOR
                )
        )

        so2_fig = go.Figure(
            data=go.Scatter(x=data['hour'], y=data['so2_hour'], mode='lines+markers', line=dict(color=ds.GRAPH_LINE_COLOR), marker=dict(color=ds.GRAPH_LINE_COLOR)),
            layout=go.Layout(
                title='Концентрация SO₂ по часам', 
                xaxis_title='Время', 
                yaxis_title='Концентрация (мкг/м³)',
                title_font_size=ds.GRAPH_TITLE_FONT_SIZE,
                title_font_color=ds.GRAPH_TITLE_COLOR,
                title_x=ds.GRAPH_TITLE_ALIGN,
                title_font_weight=ds.GRAPH_TITLE_FONT_WEIGHT,
                font=dict(family=ds.GRAPH_FONT_FAMILY),
                xaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, color=ds.GRAPH_TITLE_COLOR, gridcolor=ds.GRAPH_GRID_COLOR, tickfont=dict(size=ds.GRAPH_TICK_FONT_SIZE)),
                yaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, color=ds.GRAPH_TITLE_COLOR, gridcolor=ds.GRAPH_GRID_COLOR, tickfont=dict(size=ds.GRAPH_TICK_FONT_SIZE)),
                legend=dict(font=dict(size=ds.GRAPH_FONT_SIZE)),
                plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
                paper_bgcolor=ds.PAPER_BACKGROUND_COLOR
                )                             
        )

        pm2_5_fig = go.Figure(
            data=go.Scatter(x=data['hour'], y=data['pm2_5_hour'], mode='lines+markers', line=dict(color=ds.GRAPH_LINE_COLOR), marker=dict(color=ds.GRAPH_LINE_COLOR)),
            layout=go.Layout(
                title='Концентрация PM2.5 по часам', 
                xaxis_title='Время', 
                yaxis_title='Концентрация (мкг/м³)',
                title_font_size=ds.GRAPH_TITLE_FONT_SIZE,
                title_font_color=ds.GRAPH_TITLE_COLOR,
                title_x=ds.GRAPH_TITLE_ALIGN,
                title_font_weight=ds.GRAPH_TITLE_FONT_WEIGHT,
                font=dict(family=ds.GRAPH_FONT_FAMILY),
                xaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, color=ds.GRAPH_TITLE_COLOR, gridcolor=ds.GRAPH_GRID_COLOR, tickfont=dict(size=ds.GRAPH_TICK_FONT_SIZE)),
                yaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, color=ds.GRAPH_TITLE_COLOR, gridcolor=ds.GRAPH_GRID_COLOR, tickfont=dict(size=ds.GRAPH_TICK_FONT_SIZE)),
                legend=dict(font=dict(size=ds.GRAPH_FONT_SIZE)),
                plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
                paper_bgcolor=ds.PAPER_BACKGROUND_COLOR
                )
        )

        pm10_fig = go.Figure(
            data=go.Scatter(x=data['hour'], y=data['pm10_hour'], mode='lines+markers', line=dict(color=ds.GRAPH_LINE_COLOR), marker=dict(color=ds.GRAPH_LINE_COLOR)),
            layout=go.Layout(
                title='Концентрация PM10 по часам', 
                xaxis_title='Время', 
                yaxis_title='Концентрация (мкг/м³)', 
                title_font_size=ds.GRAPH_TITLE_FONT_SIZE,
                title_font_color=ds.GRAPH_TITLE_COLOR,
                title_x=ds.GRAPH_TITLE_ALIGN,
                title_font_weight=ds.GRAPH_TITLE_FONT_WEIGHT,
                font=dict(family=ds.GRAPH_FONT_FAMILY),
                xaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, color=ds.GRAPH_TITLE_COLOR, gridcolor=ds.GRAPH_GRID_COLOR, tickfont=dict(size=ds.GRAPH_TICK_FONT_SIZE)),
                yaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, color=ds.GRAPH_TITLE_COLOR, gridcolor=ds.GRAPH_GRID_COLOR, tickfont=dict(size=ds.GRAPH_TICK_FONT_SIZE)),
                legend=dict(font=dict(size=ds.GRAPH_FONT_SIZE)),
                plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
                paper_bgcolor=ds.PAPER_BACKGROUND_COLOR,
                )
        )
        
        return air_quality_info, co_info, no2_info, o3_info, so2_info, pm2_5_info, pm10_info, us_epa_info, uk_defra_info, co_fig, no2_fig, o3_fig, so2_fig, pm2_5_fig, pm10_fig
