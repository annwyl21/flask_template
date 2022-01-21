from flask import Flask, render_template
#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField
import uuid
from simple_bar_chart import create_bar_chart
from simple_heatmap import create_simple_heatmap
from heatmap_heathrow import create_heatmap_heathrow

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret"

# class MyForm(FlaskForm):
#     my_textfield = StringField("TextLabel")
#     my_submit = SubmitField("SubmitName")
      
@app.route("/", methods=["GET", "POST"])
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/graph_display")
def graph_display():
  #unique_identifier = uuid.uuid4()
  #create_heatmap_heathrow(unique_identifier, 1980, 1990, 1)
  create_heatmap_heathrow(888, 1980, 1990, 1)
  #weather_type max, min, frost, rainfall, sunshine - numbered at the moment
  #<img src="/static/{unique_identifier}.png">
  return render_template("graph_display.html")
