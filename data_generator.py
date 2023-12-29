import pandas as pd
from faker import Faker
import random
import os  # Import the os module for path manipulation

class DataGenerator:
    def __init__(self, num_records=1000):
        self.num_records = num_records
        self.fake = Faker()

    def generate_drivers(self):
        return pd.DataFrame([vars(self.Driver(self.fake)) for _ in range(self.num_records)])

    def generate_trucks(self):
        return pd.DataFrame([vars(self.Truck(self.fake)) for _ in range(self.num_records)])

    def generate_deliveries(self, trucks_df):
        deliveries_data = [vars(self.Delivery(self.fake, truck_number=row['truck_number'])) for _, row in trucks_df.iterrows()]
        return pd.DataFrame(deliveries_data)

    def generate_expenses(self, drivers_df):
        expenses_data = [vars(self.Expenses(self.fake, driver_name=row['name'])) for _, row in drivers_df.iterrows()]
        return pd.DataFrame(expenses_data)

    class Driver:
        def __init__(self, fake, name=None, working_h=None, salary=None, overtime=None):
            self.name = name or fake.name()
            self.working_h = working_h or random.randint(30, 50)
            self.salary = salary or random.randint(3000, 6000)
            self.overtime = overtime or random.randint(0, 10)

    class Truck:
        def __init__(self, fake, truck_number=None, cargo_hold_capacity=None, total_distance_traveled=None):
            self.truck_number = truck_number or fake.uuid4()
            self.cargo_hold_capacity = cargo_hold_capacity or random.randint(50, 200)
            self.total_distance_traveled = total_distance_traveled or random.randint(1000, 5000)

    class Delivery:
        def __init__(self, fake, truck_number=None, type_of_cargo=None, start_point=None, destination=None,
                     distance_in_km=None, truck_base_volume=None, current_cargo_volume=None):
            self.truck_number = truck_number or fake.uuid4()
            self.type_of_cargo = type_of_cargo or random.choice(["Electronics", "Clothing", "Food", "Furniture"])
            self.start_point = start_point or fake.city()
            self.destination = destination or fake.city()
            self.distance_in_km = distance_in_km or random.randint(50, 500)
            self.truck_base_volume = truck_base_volume or random.randint(20, 100)
            self.current_cargo_volume = current_cargo_volume or random.randint(0, self.truck_base_volume)

    class Expenses:
        def __init__(self, fake, driver_name=None, gasoline_cost=None, driver_cost=None, maintenance_cost=None):
            self.driver_name = driver_name or fake.name()
            self.gasoline_cost = gasoline_cost or random.randint(100, 500)
            self.driver_cost = driver_cost or random.randint(1000, 3000)
            self.maintenance_cost = maintenance_cost or random.randint(50, 200)

class DataProcessor:
    @staticmethod
    def export_data_to_csv(filename, dataframe):
        data_folder = "Data_Generated"  # Folder where CSV files will be saved
        os.makedirs(data_folder, exist_ok=True)  # Create the folder if it doesn't exist
        filepath = os.path.join(data_folder, filename)
        dataframe.to_csv(filepath, index=False)
