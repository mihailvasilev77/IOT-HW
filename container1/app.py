from flask import Flask, request, jsonify
from pysondb import db
import matplotlib.pyplot as plt

app = Flask(__name__)

db = db.getDb("data/data.json")

@app.route('/')
def home():
    return jsonify({'endpoints': ['/data', '/graph/{aqi-sensor-id}']})

@app.route('/data', methods=['POST'])
def add_data():
    content = request.json
    db.add(content)
    return jsonify({"message": "Data added successfully"})

@app.route('/graph/<string:aqi_sensor_id>', methods=['GET'])
def graph(aqi_sensor_id):
    data = db.getAll()
    values = [entry['value'] for entry in data if entry['device_id'] == aqi_sensor_id]
    timestamps = [entry['timestamp'] for entry in data if entry['device_id'] == aqi_sensor_id]
    
    colors = []
    for value in values:
        if value <= 50:
            colors.append('green')
        elif value <= 100:
            colors.append('yellow')
        elif value <= 150:
            colors.append('orange')
        else:
            colors.append('red')

    plt.stem(timestamps, values, linefmt='-', markerfmt=' ', basefmt=' ')
    plt.show()

    return jsonify({"message": "Graph generated successfully"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
