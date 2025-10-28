import requests
import os

# input
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,  # Martian Day
    'camera': 'fhaz',  # Camera
    'api_key': 'DEMO_KEY'
}

# Sending a GET request to the API
response = requests.get(url, params=params)

# Checking the success of the request
if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    if not photos:
        print("No photo found matching your criteria.")
    else:
        # Create a folder for photos if it doesn't exist.
        os.makedirs('mars_photos', exist_ok=True)

        for i, photo in enumerate(photos[:2], start=1):
            img_url = photo['img_src']
            img_data = requests.get(img_url).content

            file_path = f'mars_photos/mars_photo{i}.jpg'

            with open(file_path, 'wb') as f:
                f.write(img_data)

            print(f"Скачано {file_path}")
else:
    print(f"Request error: {response.status_code}")
