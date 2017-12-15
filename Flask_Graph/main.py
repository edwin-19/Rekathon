import json
from time import time
from random import random
from flask import Flask, render_template, make_response, request,jsonify

app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("index.html")

@app.route("/getMessage")
def getMethod():
    query = request.args.get('message', default='', type=str)
    return query

@app.route("/liveCharts")
def livecharts():
    return render_template("liveChart.html", data='test')

@app.route("/live-data")
def live_data():
    data = [time() * 1000, random() * 100]
    response = jsonify(data)
    response.content_type = 'application/json'
    return response

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("templates/HTTP404.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)