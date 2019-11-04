import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

begin_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

@app.route("/")
def welcome():
    return (
        "Welcome to the Hawaii Rainfall API!<br/>"
        "Pick from the available routes below:<br/>"
        "This returns the precipitaion data by date"
        "/api/v1.0/precipitation<br/>"
        "This retuens list of stations in Hawaii"
        "/api/v1.0/stations<br/>"
        "This returns temperature observations"
        "/api/v1.0/tobs<br/>"
        "Enter a date at end of link to observe temperature data of a particular day"
        "/api/v1.0/<start><br/>"
        "Enter a date range to observe temperature data between particular dates"
        "/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > begin_date).order_by(Measurement.date).all()
    prcp_data = []
    
    for prcp in results:
        prcp_data_dict = {}
        prcp_data_dict["Date"] = prcp.date
        prcp_data_dict['Precipitation'] = prcp.prcp
        prcp_data.append(prcp_data_dict)

    return jsonify(prcp_data)

@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Station.station, Station.name).group_by(Station.station)
    station_list = []

    for station in stations:
        station_dict = {}
        station_dict['Station Name'] = station.name
        station_dict['Station'] = station.station
        station_list.append(station_dict)
    
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    year_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > '2016-08-23').order_by(Measurement.station).all()
    temp_data = []

    for temp in year_data:
        temp_data_dict = {}
        temp_data_dict['Date'] = temp.date
        temp_data_dict['Temperature'] = temp.tobs
        temp_data.append(temp_data_dict)
    
    return jsonify(temp_data)

@app.route("/api/v1.0/<start>")
def start_stats(start=None):
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    temp_stats = []

    for tmin, tavg, tmax in results:
        temp_stats_dict = {}
        temp_stats_dict['Minimum Temperature'] = tmin
        temp_stats_dict['Average Temperature'] = tavg
        temp_stats_dict['Maximum Temperature'] = tmax
        temp_stats.append(temp_stats_dict)
    
    return jsonify(temp_stats)

@app.route("/api/v1.0/<start>/<end>")
def stats(start=None, end=None):
    start_and_end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    start_end_stats = []

    for tmin, tavg, tmax in start_and_end:
        start_end_dict = {}
        start_end_dict['Minimum Temperature'] = tmin
        start_end_dict['Average Temperature'] = tavg
        start_end_dict['Maximum Temperature'] = tmax
        start_end_stats.append(start_end_dict)

    return jsonify(start_end_stats)


if __name__ == "__main__":
    app.run(debug=True)