# Google Maps Lead Scraper (Apify API)

Automation pipeline that extracts local business leads from Google Maps and outputs structured datasets for prospecting and market research.

## Features
- Extracts business name, rating, reviews, address, phone, and website
- Uses Apify Google Maps scraping API
- Outputs structured JSON datasets

## Tech Stack
Python • API Integration • Apify • Data Pipelines

## Use Cases
- Lead generation
- Sales prospecting
- Local business research
- Market intelligence

## Sample Output

[
 {
    "name": "Golden Gate Restaurant",
    "rating": 4.6,
    "reviews": 342,
    "address": "123 Market St, San Francisco, CA",
    "phone": "+1 415-555-1234",
    "website": "https://goldengaterestaurant.com"
  },
  {
    "name": "Bay Area Dental Group",
    "rating": 4.8,
    "reviews": 198,
    "address": "456 Mission St, San Francisco, CA",
    "phone": "+1 415-555-5678",
    "website": "https://bayareadental.com"
  },
  {
    "name": "SF Fitness Hub",
    "rating": 4.7,
    "reviews": 275,
    "address": "789 Howard St, San Francisco, CA",
    "phone": "+1 415-555-9012",
    "website": "https://sffitnesshub.com"
  }
]

## Setup

pip install -r requirements.txt

Add your Apify token in scraper.py and run:

python scraper.py
