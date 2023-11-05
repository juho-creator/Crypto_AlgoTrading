import csv
from datetime import datetime, date
import requests


start_date = date(2020, 1, 1)
end_date = date(2023, 9, 30)


def get_fear_and_greed_index(start_date,end_date):
    today = datetime.now().date()

    days_diff_start = (today - start_date).days + 1
    days_diff_end = (today - end_date).days

    limit = days_diff_start - days_diff_end

    url = f"https://api.alternative.me/fng/?limit={days_diff_start}&format=json"
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


get_fear_and_greed_index(start_date=start_date,end_date=end_date)