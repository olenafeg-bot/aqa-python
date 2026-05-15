
import requests
import logging

# логер
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_URL = "http://127.0.0.1:8080"


# upload
def upload_image(filename):
    with open(filename, "rb") as image_file:
        files = {"image": image_file}

        response = requests.post(f"{BASE_URL}/upload", files=files)
        response.raise_for_status()

        logging.info(f"Upload status: {response.status_code}")
        logging.info(response.json())

        return response.json()


# get JSON
def get_image(filename):
    response = requests.get(
        f"{BASE_URL}/image/{filename}",
        headers={"Content-Type": "text"}
    )

    response.raise_for_status()

    logging.info(f"GET TEXT status: {response.status_code}")
    logging.info(response.json())

    return response.json()


# download image
def download_image(filename, save_as):
    response = requests.get(
        f"{BASE_URL}/image/{filename}",
        headers={"Content-Type": "image"}
    )

    response.raise_for_status()

    with open(save_as, "wb") as f:
        f.write(response.content)

    logging.info(f"Downloaded: {save_as}")


# delete
def delete_image(filename):
    response = requests.delete(f"{BASE_URL}/delete/{filename}")
    response.raise_for_status()

    logging.info(f"Delete status: {response.status_code}")
    logging.info(response.text)

    return response.text


# ENTRY POINT
if __name__ == "__main__":
    filename = "mars_photo1.jpg"

    upload_image(filename)
    get_image(filename)
    download_image(filename, "downloaded.jpg")
    delete_image(filename)
