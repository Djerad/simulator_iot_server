import requests
import random
import time
from datetime import datetime

# قائمة الـ Hive IDs الموجودة في DB
HIVE_IDS = ["HBX-2938471-TT"]

API_URL = "http://ip:8000/api/sensor/data/"
def generate_fake_data(hive_id):
    """توليد بيانات وهمية لكل Hive"""
    data = {
        "hive_id": hive_id,
        "temperature": round(random.uniform(30, 50), 2),
        "humidity": round(random.uniform(50, 80), 2),
        "weight": round(random.uniform(30, 50), 2),
        "co2": round(random.uniform(300, 600), 2),
        "vibration": round(random.uniform(0, 0.05), 2),
        "gps_lat": round(random.uniform(36.7, 36.8), 6),
        "gps_lng": round(random.uniform(3, 3.1), 6),
        "timestamp": datetime.now().isoformat()
    }
    return data     

while True:
    for hive_id in HIVE_IDS:
        payload = generate_fake_data(hive_id)
        print(f"إرسال البيانات لـ Hive ID: {hive_id}")
        print(payload)
        try:
            response = requests.post(API_URL, json=payload)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"حدث خطأ أثناء الإرسال: {e}")
    time.sleep(5)
