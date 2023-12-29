from data_generator import DataGenerator, DataProcessor

if __name__ == '__main__':
    # Initialize DataGenerator
    generator = DataGenerator()

    # Generate data
    drivers_df = generator.generate_drivers()
    trucks_df = generator.generate_trucks()
    deliveries_df = generator.generate_deliveries(trucks_df)
    expenses_df = generator.generate_expenses(drivers_df)

    # Initialize DataProcessor
    processor = DataProcessor()

    # Export data to CSV using DataProcessor
    processor.export_data_to_csv('drivers.csv', drivers_df)
    processor.export_data_to_csv('trucks.csv', trucks_df)
    processor.export_data_to_csv('deliveries.csv', deliveries_df)
    processor.export_data_to_csv('expenses.csv', expenses_df)

    print("Data generated and exported successfully.")
