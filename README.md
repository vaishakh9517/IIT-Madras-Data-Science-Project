This repository contains the deliverables and documentation for a stock market data preprocessing project for “Mine Dime,” a stock trend forecasting company. The aim is to clean, validate and prepare 10 years of stock price and volume data for reliable predictive modeling and trend analysis.

📁 Project Structure

/Mine-Dime-Stock-Data-Preprocessing/
│
├── Data/ # Raw and cleaned stock data
│ ├── Stock_File_1.csv
│ ├── Stock_File_2.txt
│ └── Cleaned_Stock_Data.csv
│
├── Python_Scripts/ # Python scripts used for preprocessing
│ └── stock_data_preprocessing.py
│
└── README.md # This file

📊 Project Overview
🔍 Objective

Prepare high-quality stock market data and ensure data its quality and integrity before performing predictive modelign or trend analysis : 

Ensuring chronological integrity of stock prices

Validating price and volume data

Handling missing values, duplicates, non-trading days and outliers

🧮 Data Summary

Source: Two separate stock datasets spanning 10 years of monthly prices

Key Features:

Date – Trading date

Open – Stock price at market opening

High – Maximum stock price during trading hours

Low – Minimum stock price during trading hours

Close – Stock price at market closing

Volume – Number of shares traded

Note: Some rows represent non-trading days where Open = High = Low = Close and Volume = 0.

🛠️ Procedure Followed

Data Loading and Merging:

Loaded CSV and TXT files and merged them into a single DataFrame.

Sorted the dataset chronologically by Date to maintain temporal integrity.

Data Cleaning and Validation:

Converted Date to datetime format (YYYY-MM-DD) and verified for nulls.

Converted Open, High, Low, Close to float and Volume to numeric (int/float).

Removed any currency symbols or non-numeric strings.

Handling Missing or Null Values:

Dropped rows with nulls in critical columns.

Imputed missing Volume values using rolling median over the previous 5 valid trading days.

Validating Price Relationships:

Ensured logical consistency: Low ≤ Open ≤ High and Low ≤ Close ≤ High.

Removed rows violating these conditions unless justified by special corporate actions.

Handling Duplicates:

Removed exact duplicate rows to maintain dataset uniqueness.

Removing Non-Trading Days:

Filtered out rows where Open = High = Low = Close and Volume = 0.

Outlier Detection and Treatment:

Identified extreme outliers in Price and Volume using the IQR method.

Verified outliers visually using boxplots.

Removed data errors while retaining legitimate market movements.

📈 Key Outcomes

Clean Dataset:
Chronologically sorted, with consistent numerical types and no nulls in critical columns.

Non-Trading Days Removed:
Removed placeholder rows with no trading activity to prevent distortion in analysis.

Duplicates Removed:
Ensured each trading day appears only once in the dataset.

Outliers Treated:
Removed erroneous extreme values in Price and Volume while retaining real market spikes.

The preprocessed dataset is now ready for trend analysis, predictive modeling, or machine learning applications.

📌 Conclusion

By following a professional data preprocessing workflow:

The dataset is accurate, consistent and reliable for stock trend prediction.

Price relationships and trading logic have been verified to prevent model errors.

The workflow ensures that non-trading days, duplicates and outliers do not impact analysis.

This clean and validated dataset provides a strong foundation for high-quality machine learning modeling and forecasting.

🙋‍♂️ About Me

Vaishakh K
Data Analyst | Python | Pandas | NumPy | Matplotlib | Power BI
[LinkedIn](https://www.linkedin.com/in/vaishakh-k-0b2bb8202/) • [Portfolio](https://github.com/vaishakh9517)
