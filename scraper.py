import requests

APIFY_TOKEN = "YOUR_APIFY_TOKEN"

url = f"https://api.apify.com/v2/acts/compass/google-maps-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"

payload = {
    "searchStringsArray": ["restaurants in nairobi"],
    "maxCrawledPlaces": 10
}

response = requests.post(url, json=payload)
data = response.json()

for place in data:
    print({
        "name": place.get("title"),
        "rating": place.get("rating"),
        "reviews": place.get("reviewsCount"),
        "address": place.get("address"),
        "phone": place.get("phone"),
        "website": place.get("website")
    })
