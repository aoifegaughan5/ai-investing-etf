import yfinance as yf
import pandas as pd

# Define ETFs for different risk levels.
# We're grouping these tickers based on their risk profiles.
ETF = {
    "Low": ["VTI", "BND", "SPY"],
    "Medium": ["VOO", "VXUS", "QQQ"],
    "High": ["BITO", "XBI", "ARKK"],
}


def get_etf_data(ticker, start="2010-01-01", end="2024-03-17"):
    """
    Retrieve historical data for a given ETF ticker.

    Args:
        ticker (str): The ETF ticker symbol.
        start (str): Start date for the historical data (YYYY-MM-DD).
        end (str): End date for the historical data (YYYY-MM-DD).

    Returns:
        pd.DataFrame: A DataFrame containing the closing prices.
    """
    # Get the Ticker object from yfinance for our ETF.
    stock = yf.Ticker(ticker)
    # Grab the historical data for the specified period.
    history = stock.history(start=start, end=end)
    # Return just the 'Close' price column.
    return history[['Close']]


if __name__ == "__main__":
    # Loop through each risk category and its associated ETFs.
    for risk_type, investments in ETF.items():
        for ticker in investments:
            # Let the user know which ETF we're fetching data for.
            print(f"Getting your data for {ticker} ({risk_type} risk)")
            df = get_etf_data(ticker)  # Fetch historical data for this ticker.
            # Save the data into a CSV file in the 'data' directory.
            df.to_csv(f"data/{ticker}.csv")
