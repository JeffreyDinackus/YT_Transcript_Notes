import requests
from bs4 import BeautifulSoup


#implement selenium clicking on transcript. get data, parse data. output as a string for input with chatgpt/other AI. 


url = 'https://www.youtube.com/watch?v=PeOC16IxKwg'
r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"})
html_bytes = r.text
soup = BeautifulSoup(html_bytes, 'html.parser')

elements = soup.find_all('div', class_='segment')


print(elements)