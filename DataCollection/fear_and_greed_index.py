import csv
from datetime import datetime, date
import requests
import pandas as pd
import matplotlib.pyplot as plt


def get_fear_and_greed_index(start_date,end_date):
    today = datetime.now().date()

    days_diff_start = (today - start_date).days + 1
    days_diff_end = (today - end_date).days

    limit = days_diff_start - days_diff_end

    url = f"https://api.alternative.me/fng/?limit={days_diff_start}&format=json&date_format=kr"
    response = requests.get(url)
    data = response.json()['data']

    # Define the CSV file name
    csv_file_name = 'fear_and_greed_data.csv'

    # Open the CSV file for writing
    with open(csv_file_name, 'w', newline='') as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow(['date', 'fear and greed index', 'classification'])

        # Write the data from days_diff_end to the end of the list
        for entry in data[days_diff_end:]:
            date = entry['timestamp']
            fng_index = entry['value']
            classification = entry['value_classification']
            csv_writer.writerow([date, fng_index, classification])

    print(f'{days_diff_start} most recent Fear and Greed data points (from {days_diff_end} to {days_diff_start}) saved to {csv_file_name}')


def plot_fear_and_greed_data(csv_file_name):
    # Load the data from the CSV file
    df = pd.read_csv(csv_file_name, parse_dates=['date'])

    # Create a line plot of the Fear and Greed Index
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['fear and greed index'], label='Fear and Greed Index', marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Fear and Greed Index')
    plt.title('Fear and Greed Index Over Time')
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()



start_date = date(2023, 10, 1)
end_date = date(2023, 10, 31)


# Creating csv file of Fear & Greed Index
get_fear_and_greed_index(start_date=start_date,end_date=end_date)

# Plotting Fear & Greed Index
plot_fear_and_greed_data('fear_and_greed_data.csv')