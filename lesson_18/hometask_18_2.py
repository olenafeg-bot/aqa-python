import requests

import os
print(os.getcwd())

from pathlib import Path

#base_path = Path(r"C:\Users\Olena.Fehetsyn\PycharmProjects\PythonProject\aqa-python\lesson_18")

#image = base_path / "mars_photo1.jpg",

with open('mars_photo1.jpg', 'rb') as image_file:
    files = {'image': image_file}
    response = requests.post('http://127.0.0.1:8080/upload', files=files)
    print(response.status_code)
    print(response.content)

response = requests.get('http://127.0.0.1:8080/image/mars_photo1.jpg',
                        headers={'Content-Type': 'text'})
print(response.status_code)
print(response.json())

response = requests.delete('http://127.0.0.1:8080/delete/mars_photo1.jpg')
print(response.status_code)
print(response.text)