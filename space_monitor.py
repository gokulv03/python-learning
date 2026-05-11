import requests
import time

url = "http://api.open-notify.org/iss-now.json"

while True:
    try:
        print("Pinging the ISS...")
        response = requests.get(url)
        iss_data = response.json()
        
        lat = iss_data['iss_position']['latitude']
        lon = iss_data['iss_position']['longitude']
        
        print(f"The ISS is currently located at Latitude: {lat} and Longitude: {lon}")

    except Exception as e:
        # This acts as the safety net if the internet drops
        print(f"Connection lost: {e}. Retrying...")
        
    # Notice how time.sleep is aligned with try and except!
    time.sleep(5)