from flask import Flask, render_template, redirect, Blueprint, jsonify, request
from flask_pymongo import PyMongo
import os
import pandas as pd
import json
from dotenv import load_dotenv
load_dotenv()


#app = Flask(__name__)
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection

app.config["MONGO_URI"] = os.getenv('MONGO_URI', '')
mongo = PyMongo(app)

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response 

@app.route("/")
def home():
  return render_template('index.html')


@app.route("/index.html")
def back():
    return render_template('index.html')

@app.route("/project.html")
def project():
    return render_template('project.html')

@app.route("/graphs.html")
def graphs():
    return render_template('graphs.html')

@app.route('/graphs.html')
@app.route('/canceled.html')
def cancelation():
    return render_template('canceled.html')

@app.route('/graphs.html')
@app.route('/hotels.html')
def hotels():
    return render_template('hotels.html')

@app.route('/graphs.html')
@app.route('/depositeffect.html')
def depsoit():
    return render_template('depositeffect.html')

@app.route('/graphs.html')
@app.route('/leadtime.html')
def leadtime():
    return render_template('leadtime.html')

@app.route('/graphs.html')
@app.route('/yearcomp.html')
def yearcomp():
    return render_template('yearcomp.html')

@app.route('/graphs.html')
@app.route('/marketsegments.html')
def market():
    return render_template('marketsegments.html')

@app.route('/graphs.html')
@app.route('/accommodation.html')
def accommodation():
    return render_template('accommodation.html')

@app.route('/graphs.html')
@app.route('/residual.html')
def residual():
    return render_template('residual.html')


#@app.route("/api")
#def api():
#    print("hotel_bookings")
#    print()
    
# Route to get data
@app.route("/api")
def api():
    
    collections = mongo.db.hotel_bookings.find({}, {'_id': False})
    businesses = [collection for collection in collections]
    data = {
        "businesses": businesses
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)