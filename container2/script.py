import threading
import random
import datetime
import time
import requests

def send_data(sensor_id):
    while True:
        value = random.randint(10, 200)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {
            "value": value,
            "timestamp": timestamp,
            "device_id": f"aqi_sensor_{sensor_id}"
        }
        requests.post('http://container1:5000/data', json=data)
        time.sleep(5)

if __name__ == "__main__":
    sensors = ['1', '2', '3']
    threads = []
    for sensor_id in sensors:
        thread = threading.Thread(target=send_data, args=(sensor_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
