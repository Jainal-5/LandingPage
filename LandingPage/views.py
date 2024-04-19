from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def home(request):
    url = "https://rog.asus.com/ph/phones/rog-phone-8-pro/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes (e.g., 404, 500)
        soup = BeautifulSoup(response.content, 'html.parser')
        price_element = soup.findAll('h4')
        price = price_element if price_element else 'Price is not available'
      
    except requests.RequestException as e:
        price = f'Error: {e}'
    
    return render(request, "landingpage/home.html", {'lprice': price[0].text,"hprice":price[1].text})
