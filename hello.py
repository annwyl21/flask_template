from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import uuid
from simple_bar_chart import create_bar_chart
from simple_heatmap import create_simple_heatmap
from heatmap_heathrow import create_heatmap_heathrow

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret"

class MyForm(FlaskForm):
    my_textfield = StringField("TextLabel")
    my_submit = SubmitField("SubmitName")

@app.route("/", methods=["GET", "POST"])
def hello_world():
    flask_form = MyForm()
    unique_identifier = uuid.uuid4()
    print(unique_identifier)
    create_heatmap_heathrow(unique_identifier, 1980, 1990, 1)
    #weather_type max, min, frost, rainfall, sunshine - numbered at the moment
    return f'''
        <h1>Mum's Graph</h1>
        <img src="/static/{unique_identifier}.png">
        '''
        

#try to add a form class to this page before you learn validation about what can be entered into the form
