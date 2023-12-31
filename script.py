import numpy as np
import pandas as pd


def refactorDF(df):
    df = df.dropna()
    df = df.drop_duplicates()

    #Setting price
    if 'Price' not in df.columns:
        setPrice(df)

    df['Price']=df['Price'].apply(convert_to_float)
    df['High']=df['High'].apply(convert_to_float)
    df['Low']=df['Low'].apply(convert_to_float)

    # Convert 'Date' column to datetime type
    df['Date'] = pd.to_datetime(df['Date'])
     # Add columns for year and month
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month

    return df

# Define the conversion function
def convert_to_float(number_str):
    if isinstance(number_str, str) and ',' in number_str:
        return float(number_str.replace(",", ""))
    else:
        return number_str
    
def setPrice(df):
    #Weighted avg price.
    df['Price'] = (df['High'] + df['Low'] + (2 * df['Close'])) / 4
