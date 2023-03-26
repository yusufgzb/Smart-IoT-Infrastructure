import csv
import time
import json
from kafka import KafkaProducer
import datetime

# Kafka ayarları
bootstrap_servers = ['localhost:9092'] # Kafka broker'ın adresi ve portu
topic_name = 'ornek' # Kafka topic adı

# Kafka producer'ı oluşturma
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# CSV dosyasını açma
with open('data/homeC.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader) # İlk satırı atla
    for row in reader:
        # Satırı Kafka topic'e gönder
        data = {
            "time": int(row[0]),
            "apparentTemperature": float(row[24]),
            "barn_kW": float(row[14]),
            "cloudCover": row[27],
            "deqPoint": float(row[30]),
            "dishwasher_kW": float(row[4]),
            "dewPoint": float(row[30]),
            "fridge_kW": float(row[8]),
            "furnace_1_kW": float(row[5]),
            "furnace_2_kW": float(row[6]),
            "garage_door_kW": float(row[10]),
            "gen_kW": float(row[2]),
            "home_office_kW": float(row[7]),
            "humidity": float(row[21]),
            "icon": row[20],
            "kitchen_12_kW": float(row[11]),
            "kitchen_14_kW": float(row[12]),
            "kitchen_38_kW": float(row[13]),
            "living_room_kW": float(row[17]),
            "microwave_kW": float(row[16]),
            "precipIntensity": float(row[29]),
            "precipProbability": int(row[31]),
            "pressure": float(row[25]),
            "solar_kW": float(row[18]),
            "summary": row[23],
            "temperature": float(row[19]),
            "use_kW": float(row[1]),
            "visibility": int(row[22]),
            "well_kW": float(row[15]),
            "windBearing": int(row[28]),
            "windSpeed": float(row[26])
            }



        producer.send(topic_name, value=data)
        #print(data)
        time.sleep(1) # 1 saniye bekle
