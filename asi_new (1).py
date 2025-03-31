import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
import urllib3
import boto3

# Disable SSL warnings (not recommended for production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# AWS S3 Bucket name
S3_BUCKET = "gsb521"
CSV_FILE = "occupancy_data.csv"

# Initialize S3 client
s3 = boto3.client("s3")

def scrape_and_save():
    url = "https://www.asi.calpoly.edu/asi-current-space-activity/"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        location_tags = soup.find_all('h2', class_='splitContent__title')
        occupancy_tags = soup.find_all('div', class_='occupancyBar__progressWrapper')

        locations = []
        occupancy_levels = []

        for location_tag, occupancy_tag in zip(location_tags, occupancy_tags):
            location = location_tag.text.strip()
            locations.append(location)

            style = occupancy_tag.get('style')
            occupancy_level = style.split('width:')[-1].split(';')[0].strip() if style and 'width' in style else "N/A"
            occupancy_levels.append(occupancy_level)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_data = {'Timestamp': [timestamp] * len(locations), 'Location': locations, 'Occupancy Level': occupancy_levels}
        new_df = pd.DataFrame(new_data)

        try:
            # Download existing data from S3
            obj = s3.get_object(Bucket=S3_BUCKET, Key=CSV_FILE)
            existing_df = pd.read_csv(obj['Body'])
            updated_df = pd.concat([existing_df, new_df], ignore_index=True)
        except s3.exceptions.NoSuchKey:
            updated_df = new_df  # If the file doesn't exist, use new data

        # Save updated data back to S3
        updated_df.to_csv("/tmp/" + CSV_FILE, index=False)
        s3.upload_file("/tmp/" + CSV_FILE, S3_BUCKET, CSV_FILE)

        print(f"Scraped data at {timestamp}:")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

def lambda_handler(event, context):
    scrape_and_save()
    return {"statusCode": 200, "body": "Scraping complete!"}
