from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import re


#def init_browser():
    #executable_path = {"executable_path": "chromedriver"}
    
    #return Browser("chrome", executable_path, headless=False)

def scrape():
    
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", executable_path, headless=False)


    #mars news
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    soup = bs(browser.html, 'html.parser')

    element = soup.select_one('ul.item_list li.slide')
    import time
    time.sleep(3)
    title = element.find('div', class_='content_title').text
    paragraph = element.find('div', class_='article_teaser_body').text

    #mars images
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    full_image = browser.click_link_by_partial_text('FULL IMAGE')
    more_info = browser.click_link_by_partial_text('more info')

    image = browser.html
    soup = bs(image, "html.parser")

    time.sleep(3)
    image_url = soup.find('figure', class_='lede').a['href']
    featured_image_url = "https://www.jpl.nasa.gov/" + str(image_url)

    #mars facts
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)
    facts_html = browser.html
    time.sleep(3)


    facts_table = pd.read_html(facts_url)
    mars_facts = facts_table[2]

    mars_facts.columns = ['Mars Discription' , 'Values']
    mars_facts = mars_facts.set_index('Mars Discription')

    mars_facts_table = mars_facts.to_html(classes='table table-striped thread-dark')

    #mars hemispheres
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)


    hemi_url = browser.html
    soup = bs(hemi_url, 'html.parser')
    time.sleep(3)

    hemi_img_url = []
    hemi_results = soup.find('div', class_ = 'result-list')
    hemispheres = hemi_results.find_all('div', class_ = 'item')
    
    for hemi in hemispheres:
        title = hemi.find('h3').text
        link = hemi.find('a')['href']
        image_link = 'https://astrogeology.usgs.gov/' + str(link)
        browser.visit(image_link)
        hemi_html = browser.html
        soup = bs(hemi_html, 'html.parser')
        downloads = soup.find('div', class_='downloads')
        img_url = downloads.find('a')['href']
        hemi_img_url.append({'Title': title, 'Image_URL': img_url})
    print(hemi_img_url)

    mars_dictionary = {
        'recenttitle': title,
        'recentparapraph': paragraph,
        'featuredimage': featured_image_url,
        'marsfactstable': mars_facts_table,
        'hemisphereurl': hemi_img_url
    }

    browser.quit()
    return mars_dictionary






















