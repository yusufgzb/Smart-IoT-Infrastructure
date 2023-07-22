import csv
import time
import json
from kafka import KafkaProducer
import datetime

# Kafka ayarları
bootstrap_servers = ['localhost:9092'] # Kafka broker'ın adresi ve portu
topic_name = 'ornek' # Kafka topic adı
print(topic_name)

# Kafka producer'ı oluşturma
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
print(producer)
# CSV dosyasını açma
with open('data/homeC.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    print(reader)

    next(reader) # İlk satırı atla
    for row in reader:
        # Satırı Kafka topic'e gönder
        data = {
            "time": int(row[0]),
            "apparenttemperature": float(row[24]),
            "barn_kw": float(row[14]),
            "cloudcover": row[27],
            "dewpoint": float(row[30]),
            "dishwasher_kw": float(row[4]),
            "fridge_kw": float(row[8]),
            "furnace_1_kw": float(row[5]),
            "furnace_2_kw": float(row[6]),
            "garage_door_kw": float(row[10]),
            "gen_kw": float(row[2]),
            "house_overall_kw": float(row[3]),
            "home_office_kw": float(row[7]),
            "humidity": float(row[21]),
            "icon": row[20],
            "kitchen_12_kw": float(row[11]),
            "kitchen_14_kw": float(row[12]),
            "kitchen_38_kw": float(row[13]),
            "living_room_kw": float(row[17]),
            "microwave_kw": float(row[16]),
            "precipintensity": float(row[29]),
            "precipprobability": int(row[31]),
            "pressure": float(row[25]),
            "solar_kw": float(row[18]),
            "summary": row[23],
            "temperature": float(row[19]),
            "use_kw": float(row[1]),
            "visibility": int(row[22]),
            "well_kw": float(row[15]),
            "windbearing": int(row[28]),
            "windspeed": float(row[26]),
            "wine_cellar_kw": float(row[9])
            }



        producer.send(topic_name, value=data)
        producer.flush()
        print("data")
        time.sleep(1) # 1 saniye bekle

