from flask import Flask, request, redirect
import html 
import os 
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),"templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    template=jinja_env.get_template("signup.html")
    return template.render(title="Hey, what's up?")

app.run()