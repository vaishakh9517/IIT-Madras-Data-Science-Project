# --- Importing required libraries --- 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# --- Loading files ---

stock_1 = pd.read_csv("D:/Git/IIT-Madras-Data-Science-Project/Data/Raw/Stock_File_1.csv", header=0)
stock_2 = pd.read_csv("D:/Git/IIT-Madras-Data-Science-Project/Data/Raw/Stock_File_2.txt", header=0, sep = ",")


# --- Checking for duplicates before merging ---

print("Head of Stock_1 File : ", stock_1.head())
print("Number of Rows in Stock_1 : ", len(stock_1))
print("Number of Unique Dates in Stock_1 : ", len(np.unique(stock_1['Date'])))

print("Head of Stock_2 File : ", stock_2.head())
print("Number of Rows in Stock_2: ", len(stock_2))
print("Number of Unique Dates in Stock_2 : ", len(np.unique(stock_2['Date'])))


# --- Checking if Date columns match in each file --- 

print("Column match in both files : ", stock_1.Date.equals(stock_2.Date))


# --- Formating Date ---

stock_1['Date'] = pd.to_datetime(stock_1['Date'], format="%d-%b-%y")
stock_2['Date'] = pd.to_datetime(stock_2['Date'], format="%d-%b-%y")


# --- Vertical Combining of the datasets ---

combined = pd.concat([stock_1, stock_2], ignore_index= True)
combined = combined.sort_values('Date').reset_index(drop=True)
combined_copy = combined.copy()

print("Number of Columns in Combined Stock : ", len(combined_copy))
print("Number of Unique Dates in  Combined Stock : ", len(np.unique(combined_copy['Date'])))


# --- Checking for null values ---

print("Null Values list : \n", combined_copy.isna().sum())
combined_copy = combined_copy.dropna().reset_index(drop=True)
print("Null Values list after removing them : \n", combined_copy.isna().sum())


# --- Checking datatypes of each column ---

print("Data type of each column : \n", combined_copy.dtypes)


# --- Changing data types ---

combined_copy['Volume'] = combined_copy['Volume'] = pd.to_numeric(
    combined_copy['Volume'].astype(str).str.replace(',', '', regex=False).str.strip(),
     errors='coerce'
     ).fillna(0).astype(float)

print(combined_copy.head().style.format({'Date': lambda t: t.strftime('%Y-%m-%d')}))
print("Data type of each column : \n", combined_copy.dtypes)


# --- Checking for Negative Volume entries ---

print("Any negative values in Volume? : ", (combined_copy["Volume"]<0).any())
print("Number of negative entries in Volume : ", (combined_copy["Volume"]<0).sum())


# --- Validating Price Relationships ---

valid_prices = (
    (combined_copy['Low'] <= combined_copy['Open']) &
    (combined_copy['Open'] <= combined_copy ['High']) &
    (combined_copy['Low'] <= combined_copy['Close']) &
    (combined_copy['Close'] <= combined_copy['High'])
)
combined_copy = combined_copy[valid_prices].reset_index(drop=True)


# --- Detection of duplicate entries ---

print("Number of duplicate entries : ", combined_copy.duplicated().sum())


# --- Remove Non-Trading Days if present ---

non_trading = (
    (combined_copy['Open'] == combined_copy['High']) &
    (combined_copy['High'] == combined_copy['Low']) &
    (combined_copy['Low'] == combined_copy['Close']) &
    (combined_copy['Volume'] == 0)
    )

print("Non trading days : ", non_trading.sum())

combined_copy = combined_copy[~non_trading].reset_index(drop=True)

check_non_trading = (
    (combined_copy['Open'] == combined_copy['High']) &
    (combined_copy['High'] == combined_copy['Low']) &
    (combined_copy['Low'] == combined_copy['Close']) &
    (combined_copy['Volume'] == 0)
)

print("Non trading days after removing them : ", check_non_trading.sum())


#  --- Detect Outliers in Price and Volume using IQR Method  ---

cols = ['Open', 'High', 'Low', 'Close', 'Volume']
outlier_masks = {}

for col in cols:
    Q1 = combined_copy[col].quantile(0.25)
    Q3 = combined_copy[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5*IQR)
    upper_bound = Q3 + (1.5*IQR)

    outlier_masks[col] = (combined_copy[col] < lower_bound) | (combined_copy[col] > upper_bound)
    print(f'{col} of outliers detected : ', outlier_masks[col].sum())


# --- Plotting using BoxPlot ---

plt.figure(figsize=(12,6))
combined_copy[cols].boxplot()
plt.title("Price & Volume Outlier Inspection (Boxplot)")
plt.show()

combined_outliers = np.column_stack(list(outlier_masks.values())).any(axis=1)
print("Total rows with any outlier : ", combined_outliers.sum())


# --- Removing outliers ---

combined_copy = combined_copy[~combined_outliers].reset_index(drop=True)
print("Old shape : ", stock_1.shape, stock_2.shape, combined.shape)
print("Outliers removed, new shape : ", combined_copy.shape)


# --- Exporting the Final File ---
combined_copy.to_csv('D:/Git/IIT-Madras-Data-Science-Project/Data/Cleaned/Quality_Check.csv', index = False)
