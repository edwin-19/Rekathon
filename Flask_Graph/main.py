from time import time
from random import random
from flask import Flask, render_template, make_response, request,jsonify
import logging
from logging.handlers import RotatingFileHandler
from time import strftime
import traceback
import dbhelper

app = Flask(__name__)

#Basic logging
def intializeLog():
    #initialize the log handler
    logHandler = RotatingFileHandler('log/report.log', maxBytes=1000, backupCount=1)

    #set the log handler level
    logHandler.setLevel(logging.INFO)

    #set teh app logger level
    app.logger.setLevel(logging.INFO)

    app.logger.addHandler(logHandler)

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
def exceptions(e):
    ts = strftime('[%Y-%b-%d %H:%M]')
    tb = traceback.format_exc()
    logging.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                  ts,
                  request.remote_addr,
                  request.method,
                  request.scheme,
                  request.full_path,
                  tb)
    return render_template("HTTP404.html") , 500

if __name__ == '__main__':
    intializeLog()
    #dbhelper.createTable()
    app.run(debug=True, port=5000)