import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def capture_daily_stocks():
    # Define the list of tickers to capture data for
    tickers_to_capture = ['AAPL', 'MSFT', 'UBS']

    # Get the current date and time
    today = datetime.now()

    # Calculate yesterday's date
    yesterday = today - timedelta(days=1)

    # Create an empty DataFrame to store the data for all tickers
    all_data = pd.DataFrame()

    # Loop through the list of tickers and fetch data for each
    for ticker in tickers_to_capture:
        # Create a yfinance Ticker object for the current ticker
        stock = yf.Ticker(ticker)

        # Fetch historical stock data for yesterday
        stock_data = stock.history(start=yesterday, end=yesterday)

        # Add a 'Ticker' column to identify the data for each ticker
        stock_data['Ticker'] = ticker

        # Concatenate the data for the current ticker with the overall data
        all_data = pd.concat([all_data, stock_data])

    return all_data

if __name__ == "__main__":
    multi_stock_data = capture_daily_stocks()
    print(multi_stock_data)
