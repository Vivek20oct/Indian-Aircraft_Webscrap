
```markdown
# Indian Military Aircraft Data Extraction

This project demonstrates how to extract data from a Wikipedia page that lists active Indian military aircraft and save it into a CSV file using Python.

## Overview

The script utilizes the `requests` library to fetch the HTML content of the Wikipedia page and `BeautifulSoup` from the `bs4` library to parse and extract data from the HTML. The extracted data is then written to a CSV file for further analysis or use.

## Requirements

Before running the script, ensure you have the following Python packages installed:

- `requests`
- `beautifulsoup4`
- `csv`

You can install the necessary packages using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone the repository or download the script.
2. Run the script using Python:

```bash
python extract_indian_military_aircraft.py
```

3. The script will create a CSV file named `indian_military_aircraft.csv` in the same directory as the script.

## Description of Code

- **Import Libraries**: The necessary libraries are imported.
- **Fetch Webpage**: An HTTP GET request is sent to the specified Wikipedia URL.
- **Parse HTML Content**: The HTML content is parsed using BeautifulSoup.
- **Extract Data**: The script identifies the first table with the class `wikitable` and extracts the headers and row data.
- **Save as CSV**: The extracted data is saved into a CSV file.

## Output

Upon successful execution, the following will be printed:

```
Table extracted and saved to 'indian_military_aircraft.csv'.
Preview:
['Header1', 'Header2', 'Header3', ...]
['Row1Value1', 'Row1Value2', 'Row1Value3', ...]
['Row2Value1', 'Row2Value2', 'Row2Value3', ...]
...
```

The CSV file will contain all extracted aircraft data.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Acknowledgments

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/en/master/)
```
