# Power Outage Website Scrapping Notebook

Scrapes power outage data from CESC Rajasthan website and saves to CSV.

## What it does

- Fetches live power outage information from official website
- Extracts affected areas and outage duration
- Saves data to CSV file for record keeping

## Tech Used

- Python
- BeautifulSoup (web scraping)
- Requests (HTTP calls)
- Pandas (data handling)

## Output

Creates `test.csv` with columns:
- Affected Area
- Duration (From - To)

## Notes

- Website structure may change over time
- Currently works for CESC Rajasthan (Bharatpur region)
```
