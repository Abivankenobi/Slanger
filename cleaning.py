import pandas as pd
import re

def clean_text_column(input_file, output_file, column_to_clean):
    """
    Reads a CSV file, cleans a specified text column, and saves the result to a new CSV file.

    Args:
        input_file (str): The path to the input CSV file.
        output_file (str): The path to save the cleaned CSV file.
        column_to_clean (str): The name of the column to be cleaned.
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_excel(input_file, header=1)

        # Function to clean the text
        def clean_sentence(sentence):
            if isinstance(sentence, str):
                # Convert to lowercase
                sentence = sentence.lower()
                # Remove leading/trailing white spaces
                sentence = sentence.strip()
                # Remove special characters and punctuation
                sentence = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)
            return sentence

        # Apply the cleaning function to the specified column
        df[f'cleaned_{column_to_clean}'] = df[column_to_clean].apply(clean_sentence)

        # Save the DataFrame with the new cleaned column to a new CSV file
        df.to_excel(output_file, index=False)
        print(f"Successfully cleaned the file and saved it as '{output_file}'")
        print("\nHere's a preview of the cleaned data:")
        print(df[[column_to_clean, f'cleaned_{column_to_clean}']].head())

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found. Please make sure the file is in the correct directory.")
    except KeyError:
        print(f"Error: The column '{column_to_clean}' was not found in the file. Please check the column name.")

# --- How to use the function ---

# 1. Make sure you have pandas installed:
#pip install pandas

# 2. Define your file names and the column you want to clean
input_filename = 'Words.xlsx'
output_filename = 'cleaned_words.xlsx'
column_name = 'sentence'

# 3. Call the function
clean_text_column(input_filename, output_filename, column_name)