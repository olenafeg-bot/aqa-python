
import requests

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"
params = {
    "q": "Curiosity Mars rover",
    "media_type": "image"
}

response = requests.get(search_url, params=params)
response.raise_for_status()

data = response.json()

items = data["collection"]["items"]

nasa_ids = []
for item in items:
    nasa_id = item["data"][0]["nasa_id"]
    nasa_ids.append(nasa_id)

nasa_ids = nasa_ids[:2]

print("NASA IDs:", nasa_ids)

for i, nasa_id in enumerate(nasa_ids, start=1):
    asset_url = f"{BASE_URL}/asset/{nasa_id}"

    asset_response = requests.get(asset_url)
    asset_response.raise_for_status()

    asset_data = asset_response.json()

    files = asset_data["collection"]["items"]

    jpg_url = None
    for file in files:
        image = file["href"]
        if image.endswith(".jpg"):
            jpg_url = image
            break

    if jpg_url:
        print(f"Downloading {jpg_url}")

        img_response = requests.get(jpg_url)
        img_response.raise_for_status()

        filename = f"mars_photo{i}.jpg"
        with open(filename, "wb") as f:
            f.write(img_response.content)

        print(f"Saved {filename}")
    else:
        print(f"No JPG found for {nasa_id}")
