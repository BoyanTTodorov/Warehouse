import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

class DataGenerator:
    @staticmethod
    def generate_truck_data(num_records=10):
        truck_data = []
        for _ in range(num_records):
            truck_data.append({
                'truck_number': fake.unique.random_number(digits=4),
                'driver_name': fake.name(),
            })
        return truck_data

    @staticmethod
    def generate_cargo_data(num_records=5):
        cargo_data = []
        for _ in range(num_records):
            cargo_data.append({
                'cargo_type': fake.unique.random_element(elements=('Fruits', 'Electronics', 'Clothing')),
                'cargo_description': fake.sentence(),
            })
        return cargo_data

    @staticmethod
    def generate_location_data(num_records=5):
        location_data = []
        for _ in range(num_records):
            location_data.append({
                'location_id': fake.unique.random_number(digits=4),
                'location_name': fake.city(),
                'latitude': fake.latitude(),
                'longitude': fake.longitude(),
            })
        return location_data

    @staticmethod
    def generate_time_data(num_records=100):
        time_data = []
        start_date = datetime(2023, 1, 1)
        for _ in range(num_records):
            timestamp = start_date + timedelta(hours=random.randint(1, 8760))  # Random hours within a year
            time_data.append({
                'time_id': fake.unique.random_number(digits=6),
                'timestamp': timestamp,
                'year': timestamp.year,
                'month': timestamp.month,
                'day': timestamp.day,
                'hour': timestamp.hour,
            })
        return time_data

    @staticmethod
    def generate_driver_data(num_records=10):
        driver_data = []
        for _ in range(num_records):
            driver_data.append({
                'driver_id': fake.unique.random_number(digits=4),
                'driver_name': fake.name(),
            })
        return driver_data

    @staticmethod
    def generate_fact_table_data(truck_data, cargo_data, location_data, time_data, driver_data, num_records=100):
        fact_table_data = []
        for _ in range(num_records):
            fact_table_data.append({
                'fact_id': fake.unique.random_number(digits=6),
                'truck_number': random.choice(truck_data)['truck_number'],
                'departure_time': random.choice(time_data)['timestamp'],
                'arrival_time': random.choice(time_data)['timestamp'],
                'distance_traveled': random.uniform(100, 1000),
                'cargo_type': random.choice(cargo_data)['cargo_type'],
                'other_metric': random.randint(1, 100),
            })
        return fact_table_data
