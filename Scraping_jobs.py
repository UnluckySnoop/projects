from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://fr.indeed.com/jobs?q=python&l=Toulouse+%2831%29&from=searchOnHP&vjk=13820917c0fcb9ea').text
soup = BeautifulSoup(html_text, 'lxml')

jobs_date = soup.find_all('title')

print(jobs_date)

#CloudFare