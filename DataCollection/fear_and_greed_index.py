import csv
from datetime import datetime, date
import requests
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
from get_data import fetch_and_save_candlestick_data, Client

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



def plot_fear_and_greed_data(csv_file_name, csv_file_name2):
    # Load the data from the CSV file
    df = pd.read_csv(csv_file_name, parse_dates=['date'])
    df1 = pd.read_csv(csv_file_name2, parse_dates=['Kline open time'])

    # Create a figure and axis object
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot Fear and Greed Index on primary y-axis
    ax1.plot(df['date'], df['fear and greed index'], color='blue', label='Fear and Greed Index', marker='o', linestyle='-')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Fear and Greed Index', color='blue')
    ax1.tick_params('y', colors='blue')

    # Create a secondary y-axis for BTC price
    ax2 = ax1.twinx()
    ax2.plot(df1['Kline open time'], df1['High price'], color='red', label='BTC price', marker='o', linestyle='-')
    ax2.set_ylabel('BTC Price', color='red')
    ax2.tick_params('y', colors='red')

    # Set title and legend
    plt.title('Fear and Greed Index vs BTC Price Over Time')
    fig.tight_layout()
    fig.legend(loc='upper left')

    # Rotate x-axis labels
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()



def date_to_name_format(input_date):  # Input date in "YYYY-MM-DD" format

    # Convert input date to datetime object
    dt_object = datetime.strptime(input_date, "%Y-%m-%d")

    # Format datetime object as "16 April, 2023"
    formatted_date = dt_object.strftime("%d %B, %Y")

    return formatted_date


def date_to_comma_format(date_str):
    # Split the date string by hyphens
    parts = date_str.split('-')
    
    # Join the parts with commas
    comma_format = ','.join(parts)
    
    return comma_format




start_date = '2020-01-01'
end_date = '2024-03-03'

# Convert string to datetime object
start_date_formatted = date(2020,1,1)
end_date_formatted= date(2024,3,3)

start_date_name = date_to_name_format(start_date)
end_date_name = date_to_name_format(end_date)




# Creating csv file of Fear & Greed Index
get_fear_and_greed_index(start_date_formatted, end_date_formatted)

# Creating csv file of BTC price data
fetch_and_save_candlestick_data("BTCUSDT", Client.KLINE_INTERVAL_1DAY, start_date_name, end_date_name, "BTC_data.csv")



# Plotting Fear & Greed Index
plot_fear_and_greed_data('fear_and_greed_data.csv','BTC_data.csv')