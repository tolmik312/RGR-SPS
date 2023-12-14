from dash import Dash, html, dash_table, dcc, callback, Output, Input 
import pandas as pd 
import plotly.express as px 

# Чтение данных из CSV файла 
df = pd.read_csv('E:/RGR SPS/rgr.csv') 

# Инициализация приложения 
app = Dash(__name__) 

# Макет приложения 
app.layout = html.Div([ 
    html.H1(children='Информация о бронировании номеров в отеле'), 

    # Выпадающий список 
    dcc.Dropdown( 
        id='dropdown', 
        options=[ 
            {'label': 'Начало бронирования', 'value': 'начало бронирования'}, 
            {'label': 'Конец бронирования', 'value': 'конец бронирования'},
            {'label': 'вместимость номера', 'value': 'вместимость номера'}
        ], 
        value='начало бронирования'  # Значение по умолчанию 
    ), 

    # Таблица с данными 
    dash_table.DataTable( 
        id='table', 
        columns=[{'name': col, 'id': col} for col in df.columns], 
        data=df.to_dict('records') 
    ), 

    # График временного ряда 
    dcc.Graph(id='graph'),

    # График рассеяния для анализа корреляции
    dcc.Graph(id='scatter-plot')
]) 

# Обновление графика в зависимости от выбранного параметра в выпадающем списке 
@app.callback( 
    Output('graph', 'figure'), 
    [Input('dropdown', 'value')] 
) 
def update_graph(selected_value): 
    fig = px.line(df, x=df.index, y=selected_value, title=f'График {selected_value} бронирования') 
    return fig

# Обновление графика рассеяния для анализа корреляции 
@app.callback( 
    Output('scatter-plot', 'figure'), 
    [Input('dropdown', 'value')] 
) 
def update_scatter_plot(selected_value):
    scatter_fig = px.scatter(df, x='номер', y=selected_value, title=f'График рассеяния для анализа корреляции')
    return scatter_fig
 
# Запуск приложения 
if __name__ == '__main__':
    app.run_server(debug=True)