from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import uuid
from simple_bar_chart import create_bar_chart
from simple_heatmap import create_simple_heatmap
from heatmap_heathrow import create_heatmap_heathrow

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret"

class MyForm(FlaskForm):
     start_date = StringField("Start Year")
     end_date = StringField("End Year")
     weather_type = StringField("Weather Type")
     my_submit = SubmitField("Submit")
      
@app.route("/", methods=["GET"])
def index():
  flask_form = MyForm()
  return render_template("index.html", template_form=flask_form)

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/graph_display", methods=["GET", "POST"])
def graph_display():
  if request.method == 'POST':
    print("I am a post request")
    start = int(request.form.get('start_date'))
    end = int(request.form.get('end_date'))
    weather = int(request.form.get('weather_type'))
  unique_identifier = uuid.uuid4()
  create_heatmap_heathrow(unique_identifier, start, end, weather)
  return render_template("graph_display.html", template_uuid = unique_identifier)
