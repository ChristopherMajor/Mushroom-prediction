
# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from sklearn.ensemble import RandomForestClassifier
import category_encoders as category_encoders

# Imports from this application
from app import app

#load in pipeline
from joblib import load
pipeline = load('assets/pipeline.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Enter mushroom attribues here

            Check "Insights" tab for information on mushroom attributes.

            """
        ),
        dcc.Markdown('##### Odor', className='mb-5'),
        dcc.Dropdown(
            id='odor',
            options = [
                {'label': 'Almond', 'value': 'a'},
                {'label': 'Anise', 'value': 'l'},
                {'label': 'Creosote', 'value': 'c'},
                {'label': 'Fishy', 'value': 'y'},
                {'label': 'Foul', 'value': 'f'},
                {'label': 'Musty', 'value': 'm'},
                {'label': 'No Smell', 'value': 'n'},
                {'label': 'Pungent', 'value': 'p'},
                {'label': 'Spicy', 'value': 's'},

            ]
        ),
        
        dcc.Markdown('##### Bruises', className='mb-5'),
        dcc.Dropdown(
            id='bruises',
            options=[
                {'label': "Yes", 'value': 't'},
                {'label': 'No', 'value': 'f'},
            ]
        ),
        dcc.Markdown('##### Spore print color', className='mb-5'),
        dcc.Dropdown(
            id='spore_print_color',
            options = [
                {'label': 'Black', 'value': 'k'},
                {'label': 'Brown', 'value': 'n'},
                {'label': 'Buff', 'value': 'b'},
                {'label': 'Chocolate', 'value': 'h'},
                {'label': 'Green', 'value': 'r'},
                {'label': 'Orange', 'value': 'o'},
                {'label': 'Purple', 'value': 'u'},
                {'label': 'White', 'value': 'w'},
                {'label': 'Yellow', 'value': 'y'},
            ]
        ),
        dcc.Markdown('##### Gill size', className='mb-5'),
        dcc.Dropdown(
            id='gill_size',
            options = [
                {'label': 'Broad', 'value': 'b'},
                {'label': 'Narrow', 'value': 'n'},
            ]
        ),
        dcc.Markdown('##### Stalk color below ring', className= 'mb-5'),
        dcc.Dropdown(
            id='stalk_color_below_ring',
            options = [
                {'label': 'Brown', 'value' :'n'},
                {'label': 'Buff', 'value': 'b'},
                {'label': 'Cinnamon', 'value': 'c'},
                {'label': 'Gray', 'value': 'g'},
                {'label': 'Orange', 'value': 'o'},
                {'label': 'Pink', 'value': 'p'},
                {'label': 'Red', 'value': 'e'},
                {'label': 'White', 'value': 'w'},
                {'label': 'Yellow', 'value': 'y'},
            ]
        )
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H1('Edible or Poisonous?', className='mb-5'),
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])

#adding callback
import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('odor', 'value'),
    Input('bruises', 'value'),
    Input('spore_print_color', 'value'),
    Input('gill_size', 'value'),
    Input('stalk_color_below_ring', 'value')
    ],
)

def predict(odor, bruises, spore_print_color, gill_size, stalk_color_below_ring):
    df=pd.DataFrame(
        columns=['odor', 'bruises','spore_print_color', 'gill_size', 'stalk_color_below_ring'],
        data=[[odor, bruises, spore_print_color, gill_size, stalk_color_below_ring]]
    )

    y_pred = pipeline.predict(df)[0]
    
    if y_pred == 'p':
        return html.H2('Your mushroom is poisonous'),
    if y_pred =='e':
        return html.H3('Your mushroom is edible')
