from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
count = 0

for job in jobs:
    post_date = job.find('span', class_ = 'sim-posted').text.strip()
    if post_date == "Posted few days ago" or post_date == 'Posted today':
        count += 1
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '').strip()
        more_info = job.header.h2.a['href']
        
        print(f"Number: {count}")
        print(f"Company Name: {company_name}")
        print(f"Required Skills: {skills}")
        print(f"More Information: {more_info}")