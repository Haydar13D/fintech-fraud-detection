import time
import json
import random
from datetime import datetime
from google.cloud import pubsub_v1

# --- KONFIGURASI GCP ANDA ---
PROJECT_ID = "streaming-data-weather"  # <-- GANTI DENGAN PROJECT ID ANDA
TOPIC_ID = "financial-transactions-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

# Daftar ID pengguna dan kategori merchant
USER_IDS = [f"user_{i}" for i in range(101, 110)]
MCC_CODES = [5411, 5812, 5814, 5541, 5811, 5813, 5815, 5816, 5817, 5818, 5612, 5923, 5532, ] # Toko Kelontong, Restoran, Bar, SPBU
CITIES = [
    "Jakarta", "Surabaya", "Bandung", "Medan", "Makassar", 
    "Surakarta", "Boyolali", "Sragen", "Banten", "Semarang", 
    "Bogor", "Purwokerto", "Ponorogo"
]

def generate_transaction_data():
    """Menghasilkan satu baris data transaksi, kadang-kadang anomali."""
    
    user = random.choice(USER_IDS)
    amount = round(random.uniform(50000, 500000), 2) # Transaksi normal 50k - 500k
    is_anomaly = False
    
    # 5% kemungkinan membuat transaksi anomali
    if random.randint(1, 100) <= 5: 
        amount = round(random.uniform(5000000, 20000000), 2) # Transaksi besar 5jt - 20jt
        is_anomaly = True
    
    data = {
        "transaction_id": str(int(time.time() * 1000)),
        "timestamp": datetime.now().isoformat(sep='T', timespec='milliseconds') + 'Z',
        "user_id": user,
        "amount": amount,
        "mcc_code": random.choice(MCC_CODES),
        "city": random.choice(CITIES),
        "is_anomaly": is_anomaly
    }
    return data

print(f"Memulai streaming ke {topic_path}")

try:
    while True:
        data = generate_transaction_data()
        
        # Konversi data ke string JSON lalu ke bytes
        data_json = json.dumps(data)
        data_bytes = data_json.encode("utf-8")
        
        # Kirim ke Pub/Sub
        future = publisher.publish(topic_path, data_bytes)
        
        print(f"Publikasi: User={data['user_id']}, Amount={data['amount']}, Anomali={data['is_anomaly']}")
        
        # Tunggu 2 detik sebelum mengirim transaksi berikutnya
        time.sleep(2) 

except KeyboardInterrupt:
    print("\nStreaming dihentikan oleh pengguna.")
finally:
    publisher.stop()