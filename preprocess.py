import pandas as pd

def clean_data():
    file_path = 'sales_data_sample.csv'
    data = pd.read_csv(file_path, encoding='latin1')

    # Step 1: Handle Missing Values
    columns_to_drop = ['ADDRESSLINE2', 'PHONE', 'CONTACTLASTNAME', 'CONTACTFIRSTNAME']
    data_cleaned = data.drop(columns=columns_to_drop)

    data_cleaned['STATE'] = data_cleaned['STATE'].fillna('Unknown')
    data_cleaned['POSTALCODE'] = data_cleaned['POSTALCODE'].fillna('N/A')

    # Step 2: Standardize Date Format
    # Convert ORDERDATE and handle invalid dates
    data_cleaned['ORDERDATE'] = pd.to_datetime(data_cleaned['ORDERDATE'], errors='coerce', dayfirst=False)
    # data_cleaned['ORDERDATE'] = data_cleaned['ORDERDATE'].fillna(pd.Timestamp('1970-01-01'))

    # Step 3: Type Conversion
    data_cleaned['POSTALCODE'] = data_cleaned['POSTALCODE'].astype(str)

    # Step 4: Feature Engineering
    data_cleaned['ORDER_YEAR'] = data_cleaned['ORDERDATE'].dt.year
    data_cleaned['ORDER_MONTH'] = data_cleaned['ORDERDATE'].dt.month
    data_cleaned['ORDER_QUARTER'] = data_cleaned['ORDERDATE'].dt.quarter

    return data_cleaned

def main():
    preprocessed_file = clean_data()
    preprocessed_file.to_csv('final_data.csv')
    
if __name__ == "__main__":
    main()