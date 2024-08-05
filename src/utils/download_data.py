import requests
import json

def download_ESConv_data():
    url = "https://raw.githubusercontent.com/thu-coai/Emotional-Support-Conversation/main/ESConv.json"
    default_file_path = "./data/raw/ESConv.json"
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON content
            json_data = response.json()

            # Check the size of the JSON data
            print(f"Size of JSON data: {len(json_data)} entries.")
            with open(default_file_path, "w") as f:
                json.dump(json_data, f, indent=4)
            print("Data saved to ESConv.json")

        else:
            print("Failed to retrieve data. Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error:", e)
