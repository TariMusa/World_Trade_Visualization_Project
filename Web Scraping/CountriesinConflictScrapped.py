from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML file
with open('Conflict Index Results_ July 2024 - ACLED.html', 'r', encoding='utf-8') as html_file:
    content = html_file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'lxml')

# Find all tables in the document
tables = soup.find_all('table')

# Initialize a list to store cleaned data
cleaned_data = []

# Process each table
for table in tables:
    # Find all rows in the table
    rows = table.find_all('tr')

    for row in rows:
        # Find all cells in the row
        cells = row.find_all('td')

        # Debugging: Print each row and its cells
        print(f"Row: {[cell.text.strip() for cell in cells]}")

        # Check if the row has the correct number of cells (5 columns)
        if len(cells) == 5:
            # Extract the country name and conflict index information
            rank = cells[0].text.strip()  # First column (Rank)
            country = cells[1].text.strip()  # Second column (Country)
            severity = cells[2].text.strip()  # Third column (Severity)
            status = cells[3].text.strip()  # Fourth column (Status)
            change = cells[4].text.strip()  # Fifth column (Change)

            # Append cleaned data to the list
            cleaned_data.append({
                'Rank': rank,
                'Country': country,
                'Severity': severity,
                'Status': status,
                'Change': change
            })

# Debugging: Print the cleaned data before saving
print("Cleaned Data:", cleaned_data)

# Optionally, save the cleaned data to a CSV file
df = pd.DataFrame(cleaned_data)
df.to_csv('cleaned_conflict_data.csv', index=False)
