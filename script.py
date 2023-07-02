import numpy as np
import pandas as pd
from scipy.stats import volatility



def setDateFormat(df):
    # Define the date format
    df['Date'] = pd.to_datetime(df['Date'],format='%b %d, %Y')

def cleanUpDataframe(df):
    df = df.dropna()
    df = df.drop_duplicates()

    #Setting price
    if 'Price' not in df.columns:
        setPrice(df)

    df['Price']=df['Price'].apply(convert_to_float)
    df['High']=df['High'].apply(convert_to_float)
    df['Low']=df['Low'].apply(convert_to_float)
    
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
