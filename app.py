from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/scrape_mars.py")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    mars_data = mongo.db.collection.find_one()
    return render_template('index.html', mars = mars_data)

@app.route('/scrape')
def scrapePage():
   
    # Run the scrape function
    mars_data = scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == '__main__':
    app.run()

