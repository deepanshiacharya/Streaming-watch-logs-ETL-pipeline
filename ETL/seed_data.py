import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
NUM_ROWS = 10000
USER_IDS = [f"user_{i}" for i in range(1, 201)]
CONTENT_IDS = [f"movie_{i}" for i in range(1, 101)]
DEVICES = ['Mobile', 'Laptop', 'TV', 'Tablet']
GENRES = ['Drama', 'Comedy', 'Thriller', 'Action', 'Documentary', 'Romance']
COUNTRIES = ['India', 'USA', 'UK', 'Canada', 'Australia', 'Germany']

def generate_logs(num_rows):
    data = []
    base_time = datetime.now() - timedelta(days=60)

    for _ in range(num_rows):
        user_id = random.choice(USER_IDS)
        content_id = random.choice(CONTENT_IDS)
        genre = random.choice(GENRES)
        device = random.choice(DEVICES)
        country = random.choice(COUNTRIES)

        # Generate session start and duration
        session_start = base_time + timedelta(
            days=random.randint(0, 59),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )
        watch_duration = random.randint(1, 180)  # in minutes

        data.append({
            "user_id": user_id,
            "content_id": content_id,
            "genre": genre,
            "device": device,
            "country": country,
            "watch_start": session_start.strftime('%Y-%m-%d %H:%M:%S'),
            "watch_duration_min": watch_duration
        })

    return pd.DataFrame(data)

# Generate data
df = generate_logs(NUM_ROWS)

# Generate timestamped filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f"watch_logs_{timestamp}.csv"

# Save CSV
output_path = rf"D:\Current user data\Desktop\VS\project\ETL\retail-etl\data\raw\netflix_{filename}"
df.to_csv(output_path, index=False)

print(f"Generated '{filename}' with {len(df)} rows.")
