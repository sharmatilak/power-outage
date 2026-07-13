import pandas as pd
from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://cescrajasthan.co.in/besl/pages/event/announcement/power_outage.php"

try:
    page = rq.get(url)
    page.raise_for_status()
except page.exceptions.HTTPError as e:
    if e.response.status_code == 404:
            print("API returned a 404 error: Not Found")
    else:
            print("API returned an error:", e)
except Exception as e:
        print("An error occurred:", e)

soup = bs(page.text, features='html.parser')

try:
    table = soup.find_all('div', class_ = 'body_content_middle')[0]
except:
    print("Currently no data is available!")

power_titles = table.find_all('div', class_ = 'bg-primary')

# print(power_titles)

power_table_titles = [titles.text.strip().split("\n") for titles in power_titles][0]

# print(power_table_titles)
df = pd.DataFrame(columns=power_table_titles)
columns_data = table.find_all('div', class_= 'row')[1:]

# print(columns_data)


for rows in columns_data:
    row_data = rows.find_all('div', class_= ['col-sm-7', 'col-sm-3'])
    # individual_row_data = [data.text.strip() for data in row_data]
    # print(individual_row_data)
    individual_row_data = []
    for data in row_data:
        text = data.text.strip()         # remove leading/trailing spaces
        text = text.replace('\r', '')    # remove carriage returns
        text = text.replace('\n', '')    # remove newlines
        text = text.replace('\xa0', ' ') # replace non-breaking space with normal space
        text = ' '.join(text.split())    # collapse multiple spaces into one
        individual_row_data.append(text)
        # print(individual_row_data)
    length = len(df)
    df.loc[length] = individual_row_data    

df.to_csv(r'C:\Users\Anon\Desktop\MY PERSONAL SPACE\PERSONAL_AGAIN\power-outage\test.csv')


def search_in_outages(df, keyword):
    matches = df[df.iloc[:, 0].str.contains(keyword, case=False, na=False)]
    
    if not matches.empty:
        print(f"Found '{keyword}' in {len(matches)} outage(s):")
        print("=" * 80)
        return matches
    else:
        print(f"'{keyword}' not found in any outage area")
        return None


keyword = 'SAHYOG NAGAR'
search_in_outages(df, keyword)
