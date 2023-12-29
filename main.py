from data_generator import DataGenerator, DataProcessor

if __name__ == '__main__':
    # Initialize DataGenerator
    generator = DataGenerator()

    # Generate dimension tables
    drivers_df = generator.generate_drivers()
    trucks_df = generator.generate_trucks()

    # Generate fact table
    deliveries_df = generator.generate_deliveries(drivers_df, trucks_df)
    expenses_df = generator.generate_expenses(drivers_df)

    # Initialize DataProcessor
    processor = DataProcessor()

    # Export dimension tables to CSV
    processor.export_data_to_csv('drivers.csv', drivers_df)
    processor.export_data_to_csv('trucks.csv', trucks_df)

    # Export fact table to CSV
    processor.export_data_to_csv('deliveries.csv', deliveries_df)

    # Additional dimension table (expenses)
    processor.export_data_to_csv('expenses.csv', expenses_df)

    print("Data generated and exported successfully.")
