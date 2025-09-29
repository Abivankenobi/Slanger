import xlsxwriter
import requests
import pandas as pd

df = pd.read_excel("genz_slang_dataset.xlsx")
non_null_values = df["Slang"].dropna()
result_dict = non_null_values.to_dict()

workbook = xlsxwriter.Workbook('Words.xlsx')
worksheet = workbook.add_worksheet()

headers = ["Word", "Meaning", "Example"]
for col, h in enumerate(headers):
    worksheet.write(0, col, h)

row = 1

def addto(worksheet, row, response):
    if response.status_code == 200:
        data = response.json()
        if data.get("found") and data.get("data"):
            entry = data["data"][0]
            word = entry.get("word")
            meaning = entry.get("meaning")
            example = entry.get("example")

            # Write each field in separate columns
            worksheet.write(row, 0, word)
            worksheet.write(row, 1, meaning)
            worksheet.write(row, 2, example)

    return row + 1  # return updated row


slang_list = ["ts", "pmo", "icl", "ong", "fr", "nigga","tmkc","atmkbfj","ambatakum", "ball",".s","fag","femboy"]

for slang in result_dict.values():
    url = f"https://unofficialurbandictionaryapi.com/api/search?term={slang}&strict=true&limit=1&page=1&multiPage=false"
    response = requests.get(url)
    row = addto(worksheet, row, response)

workbook.close()
