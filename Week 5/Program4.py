import sys
import requests

def check_website_availability():
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The website at {url} is working.")
        else:
            print(f"The website at {url} is not reachable (HTTP Status Code: {response.status_code}).")
    except requests.ConnectionError:
        print(f"Could not connect to {url}. Check your internet connection.")

if __name__ == "__main__":
    check_website_availability()
