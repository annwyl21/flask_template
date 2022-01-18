from flask import Flask
from simple_bar_chart import create_bar_chart

app = Flask(__name__)

@app.route("/")
def hello_world():
    create_bar_chart()
    return f'''
        <h1>Mum's Graph</h1>
        <img src="/static/simple_bar_chart.png">
        '''

