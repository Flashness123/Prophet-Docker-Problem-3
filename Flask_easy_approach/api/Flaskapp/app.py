from flask import Flask, jsonify, abort, request
import models
from model import forecast, forecast_one_day

app = Flask(__name__)

@app.route('/')
def introduction():
    return 'Home Path of the Prophet API'


@app.route("/forecast-one-day", methods=["POST"])
def get_forecast_one_day():
   
    predictions = forecast_one_day()

    if not predictions:
        abort(400, "Model not found from get_forecast_one_day")

    return jsonify({"forecast": predictions})


@app.route("/forecast-n-days", methods=["POST"])
def get_forecast_n_days():
    if not request.json or not 'days' in request.json:
        predictions = forecast()
    else:
        predictions = forecast(request.json['days'])

    if not predictions:
        abort(400, "Model not found.")

    return jsonify({"forecast": predictions})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)