from flask import Flask, jsonify, render_template
from geopy.geocoders import Nominatim
import pymysql
from mysql_config import mysql_db
import mysql.connector
import requests
import geocoder

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/map')
def map():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True,port=5500)
