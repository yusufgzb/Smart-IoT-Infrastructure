import csv
import time
from kafka import KafkaProducer

# Kafka ayarları
bootstrap_servers = ['localhost:9092'] # Kafka broker'ın adresi ve portu
topic_name = 'ornek' # Kafka topic adı

# Kafka producer'ı oluşturma
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# CSV dosyasını açma
with open('data/homeC.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader) # İlk satırı atla
    for row in reader:
        # Satırı Kafka topic'e gönder
        producer.send(topic_name, value=bytes(','.join(row), 'utf-8'))
        time.sleep(1) # 1 saniye bekle