# Web Scraping Homework - Mission to Mars

In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Step 1 - Scraping

* Completed the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

  * Used Python and Pandas to scrape a paragraph and a featured image off of NASA's website. 

  * Scraped a Mars Facts table and turned it into a dataframe using Panads and then converted the data into an HTML string.

  * Then I used a "clicking" function to click on each image of the Mars hemisphere to display on the website.


## Step 2 - MongoDB and Flask Application

* I used MongoDB with Flask templating to create a new HTML page that displayed all of the information that was scraped from the NASA's website.

* Started by converting the Jupyter notebook file into a Python script called `scrape_mars.py` with a function called `scrape` that executed all of the scraping code from the Jupyter notebook file and return one Python dictionary containing all of the scraped data.

* Next, I created a route called `/scrape` that imported `scrape_mars.py` script and called the `scrape` function.

* Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` that queried Mongo database and pass the mars data into an HTML template to display the data.

* Used Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Used Pymongo for CRUD applications for the database.

* Lastly I used Bootstrap to structure the HTML template.

