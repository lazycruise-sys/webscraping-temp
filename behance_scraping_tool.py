from bs4 import BeautifulSoup
import requests

# get the html text of the site page
html_text = requests.get('https://www.behance.net/gallery/94876543/Open-Sauce-Sans-Typeface').text
# html_text = requests.get('https://www.behance.net/gallery/66626323/Typographic-Posters').text

# create a BeautifulSoup object using the lxml parser
soup = BeautifulSoup(html_text, 'lxml')

# ID and Class
# ImageElement-image-2K6
# ImageElement-image-2K6 ImageElement-blockPointerEvents-ooR

grid_img_box = soup.find_all('img', class_ = "ImageElement-image-2K6")
for img in grid_img_box:
    img_url = img['src']
    print(img_url)
    
grid_img_box2 = soup.find_all('img', class_ = "ImageElement-image-2K6 ImageElement-blockPointerEvents-ooR")
for img in grid_img_box2:
    img_url = img['src']
    print(img_url)

# grid_img_con = soup.find('div', class_ = "project-lightbox-image-container")
# print(grid_img_con)