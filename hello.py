from flask import Flask
import uuid
from simple_bar_chart import create_bar_chart
from simple_heatmap import create_simple_heatmap
from heatmap_heathrow import create_heatmap_heathrow

app = Flask(__name__)

@app.route("/")
def hello_world():
    unique_identifier = uuid.uuid4()
    print(unique_identifier)
    create_heatmap_heathrow(unique_identifier, 1980, 1990, 1)
    #weather_type max, min, frost, rainfall, sunshine - numbered at the moment
    return f'''
        <h1>Mum's Graph</h1>
        <img src="/static/{unique_identifier}.png">
        '''

