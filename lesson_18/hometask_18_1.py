import requests
import logging

BASE_URL = "https://images-api.nasa.gov"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ImagesDownloader:

    def __init__(self, query="Curiosity Mars rover"):
        self.query = query
        self.base_url = BASE_URL

    def search_images(self):
        params = {
            "q": self.query,
            "media_type": "image"
        }

        response = requests.get(f"{self.base_url}/search", params=params)
        response.raise_for_status()

        logging.info(f"Search results for '{self.query}' received")
        return response.json()

    def find_nasa_ids(self, data, limit=2):
        items = data["collection"]["items"]

        nasa_ids = [
            item["data"][0]["nasa_id"]
            for item in items
        ][:limit]

        logging.info(f"Found NASA IDs: {nasa_ids}")
        return nasa_ids

    def get_asset_urls(self, nasa_id):
        response = requests.get(f"{self.base_url}/asset/{nasa_id}")
        response.raise_for_status()

        logging.info(f"Fetched assets for {nasa_id}")
        return response.json()["collection"]["items"]

    def get_jpg_url(self, files):
        for file in files:
            image = file["href"]
            if image.endswith(".jpg"):
                logging.info(f"Found JPG: {image}")
                return image

        logging.warning("No JPG found")
        return None

    def download_image(self, url, filename):
        response = requests.get(url)
        response.raise_for_status()

        with open(filename, "wb") as f:
            f.write(response.content)

        logging.info(f"Saved {filename}")

    def run(self):
        data = self.search_images()
        nasa_ids = self.find_nasa_ids(data)

        for i, nasa_id in enumerate(nasa_ids, start=1):
            files = self.get_asset_urls(nasa_id)
            jpg_url = self.get_jpg_url(files)

            if jpg_url:
                filename = f"mars_photo{i}.jpg"
                self.download_image(jpg_url, filename)
            else:
                logging.warning(f"No image for {nasa_id}")


if __name__ == "__main__":
    downloader = ImagesDownloader()
    downloader.run()
