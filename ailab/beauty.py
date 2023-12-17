import requests
from bs4 import BeautifulSoup

def find_and_add_headers(url, headers_list):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    header_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    headers_list.extend(header.text.strip() for header in header_tags)
    return headers_list

def main():
    website_url = input("Enter the URL of the website: ")
    headers_list = []
    headers_list=find_and_add_headers(website_url, headers_list)
    print("Headers found on the website:")
    for header in headers_list: 
        print(header)


main()