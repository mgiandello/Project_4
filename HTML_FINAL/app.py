<<<<<<< HEAD:HTML_FINAL/app.py
# import necessary libraries
# from models import create_classes
from dotenv import load_dotenv
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

load_dotenv()

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# # Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Pet = create_classes(db)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model")
def model():
    return render_template("model.html")
=======
# import necessary libraries
# from models import create_classes
from dotenv import load_dotenv
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

load_dotenv()

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# Pet = create_classes(db)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model")
def model():
    return render_template("model.html")
>>>>>>> 6fa9add3bc9f9b7974c71b84fc40d4f87d3d7201:Flask/app.py
