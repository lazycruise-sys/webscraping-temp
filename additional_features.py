# import statements
from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

# requests for users information
print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>> ')
print(f'Filtering out {unfamiliar_skill}')

# create function
def request_python_jobs():
    now = datetime.now()
    current_time = now.strftime("%H_%M_%S")
    
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    count = 0
    
    # or send to email, every 6 hours or telegram
    with open(f'exports/{current_time}_current_jobs_without_{unfamiliar_skill}.txt', 'w') as f:
        for index, job in enumerate(jobs):
            post_date = job.find('span', class_ = 'sim-posted').text.strip()
            if post_date == "Posted few days ago" or post_date == 'Posted today':
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '').strip()
                more_info = job.header.h2.a['href']
                if unfamiliar_skill not in skills:
                    count += 1
                    f.write(f"Number: {count}\n")
                    f.write(f"Company Name: {company_name}\n")
                    f.write(f"Required Skills: {skills}\n")
                    f.write(f"More Information: {more_info}\n\n")
    print(f'File saved: {current_time}_current_jobs_without_{unfamiliar_skill}.txt')
 
# specify that functions only runs if this is file is run alone               
if __name__ == '__main__':
    while True:
        request_python_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
        # delete previous file.
        # or rewrite existing file
        