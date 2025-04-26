# Requires 'requests' and 'beautifulsoup4': pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

def scrape_github_profile():
    url = input("Enter GitHub profile URL (e.g., https://github.com/username): ")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        profile_img = soup.find('img', class_='avatar-user')
        if profile_img:
            print("Profile image URL:", profile_img['src'])
        else:
            print("Profile image not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_github_profile()