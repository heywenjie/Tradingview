import yfinance as yf
import pandas as pd

def calculate_stock_price_changes():
    # Define the ticker symbol for Tesla
    ticker_symbol = "TSLA"

    # Get the historical stock data for Tesla
    ticker_data = yf.Ticker(ticker_symbol)
    historical_data = ticker_data.history(period="2d")

    # Extract the required values from the historical data
    close_price_yesterday = historical_data["Close"].iloc[-2]
    opening_price_today = historical_data["Open"].iloc[-1]
    closing_price_today = historical_data["Close"].iloc[-1]
    highest_price_today = historical_data["High"].max()
    lowest_price_after_highest = historical_data["Low"][historical_data["High"].idxmax():].min()
    lowest_price_today = historical_data["Low"].min()

    # Calculate the percentage difference between opening price and closing price of yesterday
    if opening_price_today < close_price_yesterday:
        price_difference_percentage = ((close_price_yesterday - opening_price_today) / close_price_yesterday) * 100
    else:
        price_difference_percentage = 0

    # Calculate the percentage change between lowest price after opening and the price before the increase
    lowest_price_before_increase = historical_data["Low"][historical_data["Low"] < opening_price_today].max()
    if not pd.isna(lowest_price_before_increase):
        percentage_change_after_increase = ((lowest_price_after_highest - lowest_price_before_increase) / lowest_price_before_increase) * 100
    else:
        percentage_change_after_increase = 0

    # Check if the closing price today is the highest price
    if closing_price_today == highest_price_today:
        return "No price is higher"

    # Calculate the percentage change between the lowest price after the highest price and the lowest price today
    percentage_change_after_lowest = ((lowest_price_today - lowest_price_after_highest) / lowest_price_after_highest) * 100

    return close_price_yesterday, opening_price_today, closing_price_today, highest_price_today, lowest_price_after_highest, lowest_price_today, price_difference_percentage, percentage_change_after_increase, percentage_change_after_lowest

# Call the function to get the stock price information and perform the calculations
result = calculate_stock_price_changes()
print(result)
