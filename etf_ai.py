import pandas as pd
import numpy as np
import os
import random

# Def ETFs using tickers for different levels of risk.
# Grouping these tickers by risk profile – Low, Medium, and High.
ETF = {
    "Low": ["VTI", "BND", "SPY"],
    "Medium": ["VOO", "VXUS", "QQQ"],
    "High": ["BITO", "XBI", "ARKK"]

}

def get_etf_data(ticker):
    """
    Fetch ETF pricing history from a saved CSV file.

    Args:
        ticker (str): The ETF ticker symbol.

    Returns:
        pd.DataFrame or None: DataFrame with ETF data if available,
        otherwise None.
    """
    file_path = f"data/{ticker}.csv"

    if not os.path.exists(file_path):
        print(f"There is no data for {ticker}. Please run the grab_data.py first.")
        return None
    
    df = pd.read_csv(file_path, index_col=0, parse_dates=True)
    return df


def analyse_performance(ticker):
    """
    Check out how an ETF is performing based on its historical data.

    Args:
        ticker (str): The ETF ticker symbol.

    Returns:
        dict or None: A dictionary with performance metrics or None
        if the data isn’t available.
    """
    df = get_etf_data(ticker)
    if df is None:
        return None
    # Calculate daily returns.
    df['Daily returns'] = df['Close'].pct_change()

    # Compute annual return (daily mean * 252 trading days).
    annual_return = df['Daily returns'].mean() * 252
    # Compute annualized volatility (daily std * sqrt(252)).
    volatility = df['Daily returns'].std() * np.sqrt(252)
    # Calculate Sharpe Ratio; if volatility is zero, we set it to 0.
    sharpe_ratio = annual_return / volatility if volatility > 0 else 0
    

    return {
        "ETF" : ticker,
        "Annual returns": annual_return,
        "Volatility" : volatility,
        "Sharpe Ratio": sharpe_ratio,
        
        
    }
def picking_top_etf(risk_level, exclude_etfs= None):

    """
    Pick the best ETF based on Sharpe Ratio for a given risk level.

    Args:
        risk_level (str): The risk level ("Low", "Medium", or "High").
        exclude_etfs (list, optional): ETFs to exclude from consideration.

    Returns:
        dict or str: A dictionary with performance metrics for the best ETF,
        or a string error message if something goes wrong.
    """
    if risk_level not in ETF:
        return "We can't help you choose unless you pick Low, Medium or High. Try again!"
    
    print(f"We are now checking the ETF's tickers based of your {risk_level} level")
    
    exclude_etfs = exclude_etfs or []  # Ensure it's a list
    etf_statistics = [
        analyse_performance(etf)
        for etf in ETF[risk_level]
        if etf not in exclude_etfs
    ]
    # Filter out any None values in case data wasn't found.
    etf_statistics = [e for e in etf_statistics if e is not None]

    if not etf_statistics:
        return "No more ETFs left to check for this risk level"


    # Pick the ETF with the highest Sharpe Ratio.
    top_etf = max(etf_statistics, key=lambda x: x["Sharpe Ratio"])
    return top_etf 

if __name__ == "__main__":
    # Run the ETF Advisor in a loop so you can keep exploring.
    while True:
        risk = input("\nLet me know your risk level? (Low, Medium or High): ").strip().capitalize()
        # Keep track of ETFs already chosen for this risk level.
        selected_etfs = []  # Track ETFs already chosen
        while True:  # 🔄 Loop to allow checking another ETF at the same risk level
            top_etf = picking_top_etf(risk, exclude_etfs=selected_etfs)

            if isinstance(top_etf, str):  # If there's an error message, print it
                print(top_etf)
                break

            print(f"Best ETF for {risk} investors: {top_etf['ETF']}")
            print(f"Sharpe Ratio: {top_etf['Sharpe Ratio']:.2f}")
            print("Why the Sharpe Ratio matters: It tells you how much return you are getting per unit of risk.")
            selected_etfs.append(top_etf["ETF"])  

            
            another_etf = input("\nWould you like to check another ETF in the same risk level? (yes/no): ").strip().lower()
            if another_etf != "yes":
                break


        again = input("\nWould you like to check another ETF? (yes/no): ").strip().lower()
        if again != "yes":
            print("No problem, thanks again for using the ETF Advisor! Bye!")
            break  
        
    

    
        
