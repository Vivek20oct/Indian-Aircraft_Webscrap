# Importing necessary libraries
from bs4 import BeautifulSoup
import requests

# URL of the Wikipedia page containing the list of active Indian military aircraft
url = "https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft"

# Sending an HTTP GET request to fetch the webpage content
responce = requests.get(url)

# Parsing the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(responce.content, 'html.parser')

# Finding the first table with the class "wikitable"
table = soup.find(class_='wikitable')

# Extracting the headers of the table
headers_rows = table.find_all('th')  # Find all header elements
headers = []
for header in headers_rows[0:6]:  # Extract the first six headers
    headers.append(header.text.strip())  # Strip any extra whitespace

# Initializing an empty list to store row data
rows = []

# Iterating over all rows of the table excluding the header row
for row in table.find_all('tr')[1:]:
    cells = row.find_all(['td', 'th'])  # Extract both header and data cells
    row_data = [cell.text.strip() for cell in cells]  # Clean the cell text
    rows.append(row_data)  # Append the cleaned row data to the rows list

# Writing the extracted data into a CSV file
import csv
with open('indian_military_aircraft.csv', 'w', newline="", encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)  # Write the table headers
    csv_writer.writerows(rows)  # Write all rows of the table

# Print confirmation and preview of the extracted data
print("Table extracted and saved to 'indian_military_aircraft.csv'.")
print("Preview:")
print(headers)  # Print the headers
for row in rows[:5]:  # Print the first 5 rows of the table as a preview
    print(row)
