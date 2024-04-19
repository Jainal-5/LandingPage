from bs4 import BeautifulSoup
import requests

url = "https://rog.asus.com/ph/phones/rog-phone-8-pro/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)  # Corrected

soup = BeautifulSoup(response.content, 'html.parser')

price = soup.find('h4')
