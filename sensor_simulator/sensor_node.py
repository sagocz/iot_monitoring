import os
import time
import random
import requests

from sensor_data import SensorData

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/data")

def generate_sensor_data(sensor_id: int):
    return SensorData(sensor_id=sensor_id,timestamp=time.time(),
                      temperature=round(random.uniform(20.0, 30.0), 2),
                      pressure=round(random.uniform(100.0, 105.0), 2),)

def run(sensor_id=1, interval=5):
    while True:
        data = generate_sensor_data(sensor_id)
        try:
            response = requests.post(BACKEND_URL, json=data.__dict__)
            print(f"Response: {response.status_code}, Content: {response.text}")
        except Exception as e:
            print(f"Error sending data: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    run()